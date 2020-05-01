# WordWeaver

<!-- [![Coverage Status](https://codecov.io/gh/nrc-cnrc/wordweaver/branch/master/graph/badge.svg)](https://codecov.io/gh/nrc-cnrc/wordweaver)
[![Documentation Status](https://readthedocs.org/projects/wordweaver/badge/?version=latest)](https://wordweaver.readthedocs.io/en/latest/?badge=latest) -->
<!-- [![Build Status](https://travis-ci.org/nrc-cnrc/wordweaver.svg?branch=master)](https://travis-ci.org/nrc-cnrc/wordweaver) -->
[![license](https://img.shields.io/github/license/nrc-cnrc/wordweaver.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/nrc-cnrc/wordweaver)

> Create a Database and API for your verb conjugator

:warning: :construction: This repo is currently **under construction** :construction: :warning:

<!-- Please visit the [docs](https://wordweaver.readthedocs.io/en/latest/?badge=latest) for more information! -->

## Table of Contents
- [WordWeaver](#wordweaver)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [Maintainers](#maintainers)
  - [Contributing](#contributing)
  - [License](#license)

## Background

This project is the outcome of an idea from Owennatékha Brian Maracle to create an online verb conjugator for Kanyen'kéha. The first iteration of this project required the use of a Finite State Transducer as the language model. This version is decoupled and instead uses CouchDB to store the data needed for the conjugator front-end. This was decided on for the following reasons:

- It vastly simplifies the codebase. FSTs can be written in a variety of creative ways, and the process of having a modular plugin-architecture for them was difficult to maintain.
- It improves the speed. Querying an FST in production is fast, but still not as fast as querying a database (generally speaking)
- Offline use. FSTs cannot run offline on mobile devices. Thanks to PouchDB and IndexedDB, conjugators made with WordWeaver are fully offline compatible

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- Python 3

1. After making sure you have the prerequisite technologies, clone this repo
2. In the root of the repo, make the following changes:
    * Create a new folder in `wwapi/wwapi/data/` (ideally with the ISO code of your language)
    * Add an empty `__init__.py` file
    * Copy one of the `models.py` files in the other data directories and past it into your folder
    * Create four JSON files, `conjugations.json`, `options.json`, `pronouns.json` and `verbs.json`
    * Populate the files with the data required for your language
    * Update the `models.py` file to reflect your data structure
    * Pip install `wwapi` (`cd wwapi && pip install -e .`)
    * Validate your data: `wwapi validate-data` and fix any type errors
    * Once the validation passes, go back to the root and run `docker-compose build`
    * Then, to run your local version, `docker-compose up`
    * You can stop the service by running `docker-compose down`
    * Then, visit `http://localhost:5200/docs` to see the details of using your API.
3. Head over to **wordweaver-UI** repo and configure that for usage with this API.

## Usage

Please visit the docs for more information.

## Maintainers

[@roedoejet](https://github.com/roedoejet).


## Contributing

Feel free to dive in! [Open an issue](https://github.com/nrc-cnrc/wordweaver/issues/new) or submit PRs.

This repo follows the [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) Code of Conduct.


## License

[MIT](LICENSE)
