import unittest

from templer.plone.tests.test_templates import test_suite as doc_test_suite


def test_suite():
    """ wrap all tests in a single test suite, doctests must come last
    """
    suite = unittest.TestSuite([
        doc_test_suite(),
    ])
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
