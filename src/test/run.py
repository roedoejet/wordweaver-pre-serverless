# -*- coding: utf-8 -*-

""" Execution script for running tests
"""

import os
import sys
from unittest import TestLoader, TestSuite, TextTestRunner

# Unit tests
from test_main import MainTest

LOADER = TestLoader()

ROUTE_TESTS = [
    LOADER.loadTestsFromTestCase(test) for test in [MainTest]
]

PROD_TESTS = ROUTE_TESTS

DEV_TESTS = ROUTE_TESTS

def run_tests(suite):
    '''Run tests'''
    if suite == 'all':
        suite = LOADER.discover(os.path.dirname(__file__))
    elif suite == 'prod':
        suite = TestSuite(PROD_TESTS)
    elif suite == 'dev':
        suite = TestSuite(DEV_TESTS)

    runner = TextTestRunner(verbosity=3)
    runner.run(suite)


if __name__ == "__main__":
    try:
        run_tests(sys.argv[1])
    except IndexError:
        print("Please specify a test suite to run: i.e. 'dev' or 'all'")
