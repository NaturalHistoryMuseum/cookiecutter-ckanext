This is a template for NHM CKAN extensions.

## Requirements
- [cookiecutter](https://cookiecutter.io)
- [pre-commit](https://pre-commit.com)
- [commitizen](https://commitizen-tools.github.io/commitizen)

Other relevant tools:
- [black](https://black.readthedocs.io)
- [docformatter](https://docformatter.readthedocs.io)
- [pylint](https://pylint.pycqa.org)

## Usage
To create a new extension using this template:

1. `git clone` this repo somewhere sensible (e.g. `~/.biscuits`)
2. `cd` to the directory you'd like to make the new extension in (e.g. `/path/to/ckan/src/`)
3. `cookiecutter ~/.biscuits/cookiecutter-ckanext`

You might also be able to use `cookiecutter gh:NaturalHistoryMuseum/cookiecutter-ckanext`, but I don't know if it works
with private repos.

Once created, init the git repo and install the pre-commit hooks:
```shell
git init
pre-commit install
```

To run all the pre-commit hooks manually:
```shell
pre-commit run --all-files
```

To make a commit:
```shell
git add .  # or whatever
cz c
```
