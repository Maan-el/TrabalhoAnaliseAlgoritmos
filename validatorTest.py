import unittest

import validator


class TestValidator(unittest.TestCase):

    def test_normal_url(self):
        v = validator.Validator()
        url = "https://www.amazon.com.br/"
        self.assertTrue(v.is_url(url))

    def test_invalid_url(self):
        v = validator.Validator()
        url = "asdfdghjkdfghkj"
        self.assertFalse(v.is_url(url))

    def test_empty_url(self):
        v = validator.Validator()
        url = ""
        self.assertFalse(v.is_url(url))

    def test_not_http(self):
        v = validator.Validator()
        url = "ftp://ftp.seusite.com.br"
        self.assertFalse(v.is_url(url))

if __name__ == '__main__':
    unittest.main()
