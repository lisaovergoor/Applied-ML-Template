# Applied ML Template 🛠️
## Explanation to each other for code:
**Set-Up each time:**
Pull the latest updates to the repository
```bash
    git pull
```
- Make sure to check that you are in the right branch!

Activate the virtual environment in the terminal:
```bash
    pipenv shell
```
Now you can run any code!

**Making new branch**
The following makes a new branch ("branch_name"), and moves you onto that branch
```bash
    git checkout -b branch_name
```
And only checkout moves you to the branch "branch_name"

```bash
    git checkout branch_name
```
**Pushing when finishing coding**
```bash
    git add .
    git commit -m "name of commit"
    git push
```
Make the name easy to understand for others in case we need to got back to the commits

When the commit is good to be merged onto the main branch, leave the master branch as it is! This one is protected, and only things can be put on this branch by pull requests that have been reviewed!

**Installing New Dependencies**
```bash
    pipenv install scikit-learn
```

**Running code in notebooks**
When clicking on `run`, or the triangle, choose the python interpreter (pipenv) for this repository: `C:\Users\Lisa\.virtualenvs\Applied_ML-Bx5bJ9NX`. 

If it automatically runs, then make sure you have the right interpreter by clicking on the interpreter chooser which is all the way on the right on the same height as "Generate +Code, etc."

## While coding ##
**Unittesting**
Everything that you code, make sure to write unittests on them. They can be run using the following line in the terminal:
```bash
    python -m unittest tests/data/test_data.py
```
To see specific test names you can run: `python -m unittest -v tests/data/test_data.py`
**Flake 8**
Make sure that you have the Flake8 extension on VScode enabled, so that we can keep the stylecheck on!

## Welcome to Applied Machine Learning!
This template is designed to streamline the development process and boost the quality of your code.

Before getting started with your projects, we encourage you to carefully read the sections below and familiarise yourselves with the proposed tools.

## Prerequisites
Make sure you have the following software and tools installed:

- **PyCharm**: We recommend using PyCharm as your IDE, since it offers a highly tailored experience for Python development. You can get a free student license [here](https://www.jetbrains.com/community/education/#students/).

- **Pipenv**: Pipenv is used for dependency management. This tools enables users to easily create and manage virtual environments. To install Pipenv, use the following command:
    ```bash
    $ pip install --user pipenv
    ```
    For detailed installation instructions, [click here](https://pipenv.pypa.io/en/latest/installation.html).

- **Git LFS**: Instead of committing large files to your repository, you should store and manage them using Git LFS. For installation information, [click here](https://github.com/git-lfs/git-lfs?utm_source=gitlfs_site&utm_medium=installation_link&utm_campaign=gitlfs#installing).

## Getting Started
### Setting up your own repository
1. Fork this repository.
2. Clone your fork locally.
3. Configure a remote pointing to the upstream repository to sync changes between your fork and the original repository.
   ```bash
   git remote add upstream https://github.com/ivopascal/Applied-ML-Template
   ```
   **Don't skip this step.** We might update the original repository, so you should be able to easily pull our changes.
   
   To update your forked repo follow these steps:
   1. `git fetch upstream`
   2. `git rebase upstream/main`
   3. `git push origin main`
      
      Sometimes you may need to use `git push --force origin main`. Only use this flag the first time you push after you rebased, and be careful as you might overwrite your teammates' changes.
### Git LFS
1. Set it up for your user account (only once, not each time you want to use it).
    ```bash
    git lfs install
    ```
2. Select the files that Git LFS should manage. To track all files of a certain type, you can use a wildcard as in the command below.
    ```bash
   git lfs track "*.psd"
    ```
3. Add _.gitattributes_ to the staging area.
    ```bash
    git add .gitattributes
    ```
That's all, you can commit and push as always. The tracked files will be automatically stored with Git LFS.

### Pipenv
This tool is incredibly easy to use. Let's **install** our first package, which you will all need in your projects.

```bash
pipenv install pre-commit
```

After running this command, you will notice that two files were created, namely, _Pipfile_ and _Pipfile.lock_. _Pipfile_ is the configuration file that specifies all the dependencies in your virtual environment.

To **uninstall** a package, you can run the command:
```bash
pipenv uninstall <package-name>
```

To **activate** the virtual environment, run `pipenv shell`. You can now use the environment as you wish. To **deactivate** the environment run the command `exit`.

If you **already have access to a Pipfile**, you can install the dependencies using `pipenv install`.

For a comprehensive list of commands, consult the [official documentation](https://pipenv.pypa.io/en/latest/cli.html).

### Unit testing
You are expected to test your code using unit testing, which is a technique where small individual components of your code are tested in isolation.

An **example** is given in _tests/test_main.py_, which uses the standard _unittest_ Python module to test whether the function _hello_world_ from _main.py_ works as expected.

To run all the tests developed using _unittest_, simply use:
```bash
python -m unittest discover tests
```
If you wish to see additional details, run it in verbose mode:
```bash
python -m unittest discover -v tests
```

### Pre-commit
Another good coding practice is using pre-commit hooks. This is used to inspect the code before committing to ensure it matches your standards.

In this course, we will be using two hooks (already configured in _.pre-commit-config.yaml_):
- Unit testing
- Flake8 (checks your code for errors, styling issues and complexity)

Since we have already configured the hooks, all you need to do is run:
```bash
pre-commit install
```
Now `pre-commit` will automatically run whenever you want to commit something to the repository.

## Get Coding
You are now ready to start working on your projects.

We recommend following the same folder structure as in the original repository. This will make it easier for you to have cleaner and consistent code, and easier for us to follow your progress and help you.

Your repository should look something like this:
```bash
├───data  # Stores .csv
├───models  # Stores .pkl
├───notebooks  # Contains experimental .ipynbs
├───project_name
│   ├───data  # For data processing, not storing .csv
│   ├───deployment # For model deployment
│   ├───models # For model creation, not storing .pkl
│   └───preprocessing  
├───reports
├───tests
│   ├───data # Contains a test file for each "normal file"
│   ├───features
│   └───models
├───.gitignore
├───.pre-commit-config.yaml
├───main.py
├───train_model.py
├───Pipfile
├───Pipfile.lock
├───README.md
```

**Good luck and happy coding! 🚀**
