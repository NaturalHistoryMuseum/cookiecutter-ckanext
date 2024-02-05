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

You might also be able to use `cookiecutter gh:NaturalHistoryMuseum/cookiecutter-ckanext` (without having to clone anything).

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

## Other steps

**Don't forget** to add the secrets: `PERSONAL_ACCESS_TOKEN` (create one [here](https://github.com/settings/tokens?type=beta)) and `COVERALLS_REPO_TOKEN` (get it from the individual coveralls repo page - [here's all the NHM repos](https://coveralls.io/github/NaturalHistoryMuseum)).
