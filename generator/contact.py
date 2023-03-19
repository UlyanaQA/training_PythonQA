import json
import os.path
import string
import random
import getopt
import sys
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for opt, val in opts:
    if opt == "-n":
        n = int(val)
    elif opt == "-f":
        f = val

def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address():
    return random_string(20) + "," + random_string(20)


def random_phone():
    return "+" + "".join([random.choice(string.digits) for i in range(random.randrange(4, 10))])


def random_email():
    domen = [".ru", ".org", ".com"]
    return random_string(10) + "@" + random_string(10) + random.choice(domen)


def random_site():
    domen = [".ru", ".org", ".com", "etu"]
    return random_string(10) + random.choice(domen)


testdata = [Contact(firstname=random_string(10), middlename=random_string(10),
                    lastname=random_string(10), nickname=random_string(10),
                    title=random_string(10), company=random_string(10),
                    address=random_address(), homephone=random_phone(),
                    mobilephone=random_phone(), workphone=random_phone(),
                    fax=random_phone(), email1=random_email(),
                    email2=random_email(), email3=random_email(),
                    site=random_site(), address2=random_address(),
                    secondaryphone=random_phone(), notes=random_string(20)) for i in range(5)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
