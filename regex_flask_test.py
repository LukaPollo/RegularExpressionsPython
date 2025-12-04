import unittest
from validator import *

# 1 negative | 1 positive for each validation function 
class TestValidators(unittest.TestCase):
    def test_name_valid(self):
        self.assertTrue(name_validation("John Doe"))

    def test_name_invalid(self):
        self.assertFalse(name_validation("John123"))

    def test_email_valid(self):
        self.assertTrue(email_validation("test@gmail.com"))

    def test_email_invalid(self):
        self.assertFalse(email_validation("invalid.email"))

    def test_iban_valid(self):
        self.assertTrue(bankszamla_validation("HU42117730161111101800000000"))

    def test_iban_invalid(self):
        self.assertFalse(bankszamla_validation("HU123"))

    def test_uuid_valid(self):
        self.assertTrue(uuid_validation("48018487-4f77-4eaa-baaf-a929bb52a66a"))

    def test_uuid_invalid(self):
        self.assertFalse(uuid_validation("48018487-4f77-4eaa-baaf-a929bb52a66"))

    def test_phone_valid(self):
        self.assertTrue(telefonszam_validation("06 70 4040342"))

    def test_phone_invalid(self):
        self.assertFalse(telefonszam_validation("0620-1234567"))

    def test_isbn_valid(self):
        self.assertTrue(isbn_validation("978-0-439-02348-1"))

    def test_isbn_invalid(self):
        self.assertFalse(isbn_validation("0-439-02348-1"))

    def test_imei_valid(self):
        self.assertTrue(imei_validation("123456789012345"))

    def test_imei_invalid(self):
        self.assertFalse(imei_validation("12345678901234"))

    def test_url_valid(self):
        self.assertTrue(url_validation("https://example.com"))

    def test_url_invalid(self):
        self.assertFalse(url_validation("example.com"))


if __name__ == "__main__":
    unittest.main()
