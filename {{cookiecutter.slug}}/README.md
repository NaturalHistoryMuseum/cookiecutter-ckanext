<!--header-start-->
<img src=".github/nhm-logo.svg" align="left" width="150px" height="100px" hspace="40"/>

# {{ cookiecutter.slug }}

[![Tests](https://img.shields.io/github/workflow/status/NaturalHistoryMuseum/{{ cookiecutter.slug }}/Tests?style=flat-square)](https://github.com/NaturalHistoryMuseum/{{ cookiecutter.slug }}/actions/workflows/main.yml)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/{{ cookiecutter.slug }}/main?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/{{ cookiecutter.slug }})
[![CKAN](https://img.shields.io/badge/ckan-2.9.1-orange.svg?style=flat-square)](https://github.com/ckan/ckan)
[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue.svg?style=flat-square)](https://www.python.org/)
[![Docs](https://img.shields.io/readthedocs/{{ cookiecutter.slug }}?style=flat-square)](https://{{ cookiecutter.slug }}.readthedocs.io)
<!--header-end-->
<!--overview-start-->

_{{ cookiecutter.summary }}_


# Overview

{{ cookiecutter.description }}

<!--overview-end-->
<!--installation-start-->
# Installation

Path variables used below:
- `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g. `/usr/lib/ckan/default`
- `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

1. Clone the repository into the `src` folder:

  ```bash
  cd $INSTALL_FOLDER/src
  git clone https://github.com/NaturalHistoryMuseum/{{ cookiecutter.slug }}.git
  ```

2. Activate the virtual env:

  ```bash
  . $INSTALL_FOLDER/bin/activate
  ```

3. Install the requirements from requirements.txt:

  ```bash
  cd $INSTALL_FOLDER/src/{{ cookiecutter.slug }}
  pip install -r requirements.txt
  ```

4. Run setup.py:

  ```bash
  cd $INSTALL_FOLDER/src/{{ cookiecutter.slug }}
  python setup.py develop
  ```

5. Add '{{ cookiecutter.short_name }}' to the list of plugins in your `$CONFIG_FILE`:

  ```ini
  ckan.plugins = ... {{ cookiecutter.short_name }}
  ```
<!--installation-end-->
<!--configuration-start-->
# Configuration

These are the options that can be specified in your .ini config file.

Name|Description|Options
--|--|--
|||

<!--configuration-end-->
<!--usage-start-->
# Usage


<!--usage-end-->
<!--testing-start-->
# Testing

There is a Docker compose configuration available in this repository to make it easier to run tests.

To run the tests against ckan 2.9.x on Python3:

1. Build the required images
```bash
docker-compose build
```

2. Then run the tests.
   The root of the repository is mounted into the ckan container as a volume by the Docker compose
   configuration, so you should only need to rebuild the ckan image if you change the extension's
   dependencies.
```bash
docker-compose run ckan
```

The ckan image uses the Dockerfile in the `docker/` folder.
<!--testing-end-->
