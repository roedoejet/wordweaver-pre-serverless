from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))

long_description = "long description"
# with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

with open(path.join(this_directory, "requirements.txt")) as f:
    REQS = f.read().splitlines()

setup(
    name="wordweaver",
    python_requires=">=3.6",
    license="MIT",
    author="Aidan Pine, Anna Kazantseva",
    author_email="aidan.pine@nrc-cnrc.gc.ca, anna.kazantseva@nrc-cnrc.gc.ca",
    version="0.1",
    url="https://github.com/nrc-cnrc/wordweaver",
    description="WordWeaver: A tool for creating verb conjugators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["wordweaver = wordweaver.cli:cli"]},
    install_requires=REQS,
)
