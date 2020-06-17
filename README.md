# WordWeaver

<!-- [![Coverage Status](https://codecov.io/gh/nrc-cnrc/wordweaver/branch/master/graph/badge.svg)](https://codecov.io/gh/nrc-cnrc/wordweaver)
[![Documentation Status](https://readthedocs.org/projects/wordweaver/badge/?version=latest)](https://wordweaver.readthedocs.io/en/latest/?badge=latest) -->
<!-- [![Build Status](https://travis-ci.org/nrc-cnrc/wordweaver.svg?branch=master)](https://travis-ci.org/nrc-cnrc/wordweaver) -->
[![license](https://img.shields.io/github/license/nrc-cnrc/wordweaver.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/nrc-cnrc/wordweaver)

> Create an API for your WordWeaver verb conjugator

:warning: :construction: This repo is currently **under construction** :construction: :warning:

<!-- Please visit the [docs](https://wordweaver.readthedocs.io/en/latest/?badge=latest) for more information! -->

## Table of Contents
- [WordWeaver](#wordweaver)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
  - [Local Development & Deployment](#local-development--deployment)
  - [Usage](#usage)
  - [Maintainers](#maintainers)
  - [Contributing](#contributing)
  - [License](#license)

## Background

This project is the outcome of an idea from Owennatékha Brian Maracle to create an online verb conjugator for Kanyen'kéha. The first iteration of this project required the use of a Finite State Transducer as the language model. This version is decoupled and instead uses flat-file, gzipped JSON to store the data needed for the conjugator front-end. This was decided on for the following reasons:

- It vastly simplifies the codebase. FSTs can be written in a variety of creative ways, and the process of having a modular plugin-architecture for them was difficult to maintain.
- It improves the speed. Querying an FST in production is fast, but still not as fast as querying this API.
- Less overhead. There's no need to index your data or do other performance-enhancing things that you would need to do with a database or with sorting out the serialization/deserialization architecture with an FST.
- Offline use. FSTs cannot run offline on mobile devices. Because the endpoints are fixed, the WordWeaver-UI can cache them with a service worker to allow complete offline functionality (except for file requests like returning docx, latex or csv files for conjugations)

Note: there is a limitation with using a flat file architecture. We have some optimizations in place so all you should need to do is drop your un-zipped, plain ol' JSON in here. Most conjugators that we have built fall somewhere in the 10,000 conjugations (French) to 300,000 (Mohawk) range. There are some variables here, like how many morphemes are defined for each conjugation etc. But generally speaking, after compression, our small French-type conjugators weigh in at around ~40KiB and our big Mohawk-type conjugators weigh in at < 2MiB which for most connections is perfectly fine. Especially considering this is only sent potentially once over the wire. If you have a monstrously large conjugator, say 1,000,000+ conjugations, you may have to look into other options. For more information, please visit the docs!

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- Python 3

1. After making sure you have the prerequisite technologies, clone this repo
2. In the root of the repo, make the following changes:
    * Create a new folder in `wordweaver/wordweaver/data/` (ideally with the ISO code of your language)
    * Add an empty `__init__.py` file
    * Copy one of the `models.py` files in the other data directories and past it into your folder
    * Create four JSON files, `conjugations.json`, `options.json`, `pronouns.json` and `verbs.json`
    * Populate the files with the data required for your language
    * Update the `models.py` file to reflect your data structure
    * Pip install `wordweaver` (`cd wordweaver && pip install -e .`)
    * Validate your data: `wordweaver validate-data` and fix any type errors
    * Once the validation passes, go back to the root and run `docker-compose build`
    * Then, to run your local version, `docker-compose up`
    * You can stop the service by running `docker-compose down`
    * Then, visit `http://localhost:5200/docs` to see the details of using your API.
    * Change the `WWLANG` environment variable in `env-backend.env` to the name of your language folder
  
3. Head over to **wordweaver-UI** repo and configure that for usage with this API.

## Local Development & Deployment

The following instructions are for deploying using docker compose.

To run locally and deploy a basic service, you must have Docker installed, and then follow the steps from above:

* Once the validation passes, go back to the root and run `docker-compose build`
* Then, to run your local version, `docker-compose up`
* You can stop the service by running `docker-compose down`

To build the production version:

Requirements:
  - VPS
  - Domain
  - DNS control

* Set up DNS to point to your VPS that will host the site.
* Clone this repo
* Change the email and domain in `.env`
* run `init-letsencrypt.sh` to get an SSL cert for your site
* run `docker-compose -f docker-compose.prod.yml up` to spin up your site 

## Usage

Please visit the docs for more information.

## Maintainers

[@roedoejet](https://github.com/roedoejet).


## Contributing

Feel free to dive in! [Open an issue](https://github.com/nrc-cnrc/wordweaver/issues/new) or submit PRs.

This repo follows the [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) Code of Conduct.


## License

[MIT](LICENSE)
