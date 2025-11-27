import re

class Validator:
    def validate_hungarian_phone_number(phone_number):
        return re.match(r"^(\+36|06)(\s|-)?(29|30|31|70)(\s|-)?\d{7}$", phone_number)

    def validate_persons_name(name):
        return re.match(r"^[a-zA-Z ]{1,567}$", name) 

    def validate_imei(imei):
        return re.match(r"^\d{15}$", imei)

    def validate_iban(iban):
        return re.match(r"^HU\d{2}(\s|-)?\d{4}(\s|-)?\d{4}(\s|-)?\d{4}(\s|-)?\d{4}(\s|-)?\d{4}(\s|-)?\d{4}$", iban) 
