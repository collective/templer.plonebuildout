import os
import unittest

from templer.core.tests.test_templates import doc_suite


current_dir = os.path.abspath(os.path.dirname(__file__))


def test_suite():
    """returns the test suite"""
    suite = doc_suite(current_dir)
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
