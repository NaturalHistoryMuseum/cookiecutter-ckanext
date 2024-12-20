<!--header-start-->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://data.nhm.ac.uk/images/nhm_logo.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://data.nhm.ac.uk/images/nhm_logo_black.svg">
  <img alt="The Natural History Museum logo." src="https://data.nhm.ac.uk/images/nhm_logo_black.svg" align="left" width="150px" height="100px" hspace="40">
</picture>

# {{ cookiecutter.slug }}

[![Tests](https://img.shields.io/github/actions/workflow/status/NaturalHistoryMuseum/{{ cookiecutter.slug }}/tests.yml?style=flat-square)](https://github.com/NaturalHistoryMuseum/{{ cookiecutter.slug }}/actions/workflows/tests.yml)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/{{ cookiecutter.slug }}/main?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/{{ cookiecutter.slug }})
[![CKAN](https://img.shields.io/badge/ckan-2.9.7-orange.svg?style=flat-square)](https://github.com/ckan/ckan)
[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue.svg?style=flat-square)](https://www.python.org/)
[![Docs](https://img.shields.io/readthedocs/{{ cookiecutter.slug }}?style=flat-square)](https://{{ cookiecutter.slug }}.readthedocs.io)

_{{ cookiecutter.summary }}_

<!--header-end-->

# Overview
<!--overview-start-->

{{ cookiecutter.description }}

<!--overview-end-->

# Installation
<!--installation-start-->

Path variables used below:
- `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g. `/usr/lib/ckan/default`
- `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

## Installing from PyPI

```shell
pip install {{ cookiecutter.slug }}
```

## Installing from source

1. Clone the repository into the `src` folder:
   ```shell
   cd $INSTALL_FOLDER/src
   git clone https://github.com/NaturalHistoryMuseum/{{ cookiecutter.slug }}.git
   ```

2. Activate the virtual env:
   ```shell
   . $INSTALL_FOLDER/bin/activate
   ```

3. Install via pip:
   ```shell
   pip install $INSTALL_FOLDER/src/{{ cookiecutter.slug }}
   ```

### Installing in editable mode

Installing from a `pyproject.toml` in editable mode (i.e. `pip install -e`) requires `setuptools>=64`; however, CKAN 2.9 requires `setuptools==44.1.0`. See [our CKAN fork](https://github.com/NaturalHistoryMuseum/ckan) for a version of v2.9 that uses an updated setuptools if this functionality is something you need.

## Post-install setup

1. Add '{{ cookiecutter.short_name }}' to the list of plugins in your `$CONFIG_FILE`:
   ```ini
   ckan.plugins = ... {{ cookiecutter.short_name }}
   ```
   
{% if cookiecutter.use_less -%}
2. Install `lessc` globally:
   ```shell
   npm install -g "less@~4.1"
   ```
{%- endif -%}

<!--installation-end-->

# Configuration
<!--configuration-start-->
These are the options that can be specified in your .ini config file.

| Name | Description | Options |
|------|-------------|---------|
| ``   |             | ``      |

<!--configuration-end-->

# Usage
<!--usage-start-->

<!--usage-end-->

# Testing
<!--testing-start-->
There is a Docker compose configuration available in this repository to make it easier to run tests. The ckan image uses the Dockerfile in the `docker/` folder.

To run the tests against ckan 2.9.x on Python3:

1. Build the required images:
   ```shell
   docker compose build
   ```

2. Then run the tests.
   The root of the repository is mounted into the ckan container as a volume by the Docker compose
   configuration, so you should only need to rebuild the ckan image if you change the extension's
   dependencies.
   ```shell
   docker compose run ckan
   ```

<!--testing-end-->
