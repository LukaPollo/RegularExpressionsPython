import re
from regex_constants import *


def name_validation(value):
    return bool(value and re.match(PERSON_NAME_REGEX, value))


def email_validation(value):
    return bool(value and re.match(EMAIL_REGEX, value))


def bankszamla_validation(value):
    return bool(value and re.match(IBAN_REGEX, value))


def uuid_validation(value):
    return bool(value and re.match(UUID_REGEX, value))


def telefonszam_validation(value):
    return bool(value and re.match(HUNGARIAN_PHONE_REGEX, value))


def isbn_validation(value):
    return bool(value and re.match(ISBN_REGEX, value))


def imei_validation(value):
    return bool(value and re.match(IMEI_REGEX, value))


def url_validation(value):
    return bool(value and re.match(URL_REGEX, value))
