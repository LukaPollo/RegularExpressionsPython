"""
Phone Number validation
+36 / 06 
https://www.sent.dm/resources/hu#technical-requirements-checklist

Iban, HU
https://wise.com/hu/iban/hungary

IMEI
https://rayanzayat.com/ultimate-guide-for-imei-numbers-step-by-step/#understanding-the-imei-number-structure

Persons names
first letters capital, titles included, maritial status
"""

from validator import Validator

def regex_feladat():
    phone_number_input = input("Enter your phone number: ")
    if Validator.validate_hungarian_phone_number(phone_number_input):
        print("Valid Phone Number!")
    else:
        print("Invalid Phone Number!")

    persons_name_input = input("Enter your name: ")
    if Validator.validate_persons_name(persons_name_input):
        print("Valid Name!")
    else:
        print("Invalid Name!")

    imei_input = input("Enter your IMEI number: ")
    if Validator.validate_imei(imei_input):
        print("Valid IMEI number!")
    else:
        print("Invalid IMEI number!")

    iban_input = input("Enter your IBAN number: ")
    if Validator.validate_iban(iban_input):
        print("Valid IBAN number!")
    else:
        print("Invalid IBAN number!")

regex_feladat()
