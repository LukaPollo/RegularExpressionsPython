from flask import Flask, render_template, request
from regex_constants import *
from validator import *

app = Flask(__name__)

#error messages grouped nicely :)
fields = [
    ("name", name_validation, "The name is invalid"),
    ("iban", bankszamla_validation, "The Iban number is invalid"),
    ("phone", telefonszam_validation, "The phone number is invalid"),
    ("isbn", isbn_validation, "The ISBN is invalid"),
    ("email", email_validation, "The email address is invalid"),
    ("uuid", uuid_validation, "The UUID is invalid"),
    ("url", url_validation, "The URL is invalid"),
    ("imei", imei_validation, "The IMEI is invalid"),
]

#get
@app.route("/", methods=["GET"])
def show_form():
    return render_template("index.html",
            patterns={"email": EMAIL_REGEX,"name": PERSON_NAME_REGEX,"iban": IBAN_REGEX,"uuid": UUID_REGEX,"phone": HUNGARIAN_PHONE_REGEX,"isbn": ISBN_REGEX,"imei": IMEI_REGEX,"url": URL_REGEX,},
    )

#post
@app.route("/submit", methods=["POST"])
def submit_form():
    submitted = {name: request.form.get(name, "").strip() for name, *_ in fields}

    error_messages = []
    for name, validator, msg in fields:
        value = submitted.get(name, "")
        if not validator(value):
            error_messages.append(msg)

    if error_messages:
        return render_template("index.html",
            patterns={"email": EMAIL_REGEX,"name": PERSON_NAME_REGEX,"iban": IBAN_REGEX,"uuid": UUID_REGEX,"phone": HUNGARIAN_PHONE_REGEX,"isbn": ISBN_REGEX,"imei": IMEI_REGEX,"url": URL_REGEX,},
            errors=error_messages,
        )

    return render_template("end.html")


if __name__ == "__main__":
    app.run(debug=True)