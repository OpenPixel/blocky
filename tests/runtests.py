#!/usr/bin/env python
import os
import sys
import unittest

import django
from django.conf import settings
from django.test.utils import get_runner


def run_django_tests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.blocky_django.settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests([])
    return failures


def run_flask_tests():
    from tests.blocky_flask import FlaskBlockyTestCase
    suite = unittest.TestLoader().loadTestsFromTestCase(
        FlaskBlockyTestCase
    )
    result = unittest.TextTestRunner().run(suite)
    return result.failures


def runtests():
    django_failures = run_django_tests()
    flask_failures = run_flask_tests()
    sys.exit(any([bool(django_failures), bool(flask_failures)]))


if __name__ == "__main__":
    runtests()
