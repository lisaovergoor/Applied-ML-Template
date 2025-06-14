import numpy as np
import os
import sys
from tweet_sentiment_analysis.models.save_load_model import ModelSaver
from tweet_sentiment_analysis.preprocessing.baseline_preprocessing import (
    BaselinePreprocessor)
from tweet_sentiment_analysis.preprocessing.bert_preprocessing import (
    MainPreprocessing)
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import joblib
import torch.nn.functional as F
from typing import Tuple
from fastapi import FastAPI
from tqdm import tqdm
from torch.utils.data import DataLoader, TensorDataset
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
)


app = FastAPI()


class PredictEmotion():
    """
    Interface to classify emotions in text using either a baseline
    scikit-learn model or a BERT-based transformer model.
    """
    def __init__(self, baseline: bool = True) -> None:
        """
        Load the chosen model and its preprocessing pipeline.

        Args:
            baseline (bool): If True, loads a scikit-learn
                baseline model. Otherwise loads a HuggingFace
                BERT sequence classification model.
        """
        self.baseline = baseline
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        if baseline:
            model_loader = ModelSaver()
            raw_model = model_loader.load_model("baseline_model")
            self.model = raw_model.to(
                self.device
            ) if hasattr(raw_model, "to") else raw_model

            self.preprocessor = BaselinePreprocessor()
        else:
            bert_model_path = "output/saved_bert/model"
            self.model = (
                AutoModelForSequenceClassification
                .from_pretrained(bert_model_path)
                .to(self.device)
            )
            self.bert_tokenizer = AutoTokenizer.from_pretrained(
                bert_model_path
            )
            self.label_encoder = joblib.load("output/saved_bert/label_encoder")
            self.preprocessor = MainPreprocessing()

    def predict(self, text: str, batch_size: int = 32) -> Tuple[str, float]:
        """
        Predict emotion label and confidence score for preprocessed text.

        Args:
            text (str): Token or string input ready for the model.

        Returns:
            tuple[str, float]: (predicted_label, confidence_score)
        """
        if self.baseline:
            prediction = self.model.predict(text)
            probability = self.model.predict_proba(text)
            confidence = np.max(probability, axis=1)[0]
            return prediction, confidence
        else:
            # Tokenize and batch for BERT
            train_encodings = self.bert_tokenizer(
                text,
                truncation=True,
                padding=True,
                max_length=128,
                return_tensors="pt"
            )
            dataset = TensorDataset(
                train_encodings["input_ids"],
                train_encodings["attention_mask"]
            )
            dataloader = DataLoader(dataset, batch_size=batch_size)

            all_predictions = []
            all_confs = []

            with torch.no_grad():
                for input_ids, attention_mask in tqdm(
                    dataloader, desc="batch prediction"
                ):
                    input_ids = input_ids.to(self.device)
                    attention_mask = attention_mask.to(self.device)

                    logits = self.model(
                        input_ids=input_ids,
                        attention_mask=attention_mask
                    ).logits

                    probability = F.softmax(logits, dim=1)
                    prob_val, predicted_class = torch.max(probability, dim=1)

                    all_confs.extend(prob_val.cpu().tolist())
                    all_predictions.extend(
                        self.label_encoder.inverse_transform(
                            predicted_class.cpu()
                        )
                    )

            return all_predictions[0], all_confs[0]

    def output_emotion(self, text: str) -> Tuple[str, float]:
        """
        Full pipeline: preprocess raw text, predict label, round confidence.

        Args:
            text (str): Original text input (e.g., a tweet).

        Returns:
            tuple[str, float]: (predicted_label,
            confidence_rounded_to_two_decimals)
        """
        tweet_cleaned = self.preprocessor.preprocessing_pipeline(
            at_inference=True, data=text
        )
        if hasattr(tweet_cleaned, "iloc"):
            cleaned_text = tweet_cleaned.iloc[0]
        else:
            cleaned_text = tweet_cleaned

        prediction, confidence = self.predict(cleaned_text)
        if isinstance(prediction, (np.ndarray, list)):
            return str(prediction[0]), float(round(confidence, 2))
        return str(prediction), float(round(confidence, 2))
