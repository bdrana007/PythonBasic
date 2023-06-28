# Phone Number County & Carrier Locator
# pip install phonenumbers

import phonenumbers
from test import number
from test import number1
from test import number2

# For Number
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
print('\n')
# For Number 2:
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number1, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number1, "RO")
print(carrier.name_for_number(service_number, "en"))
print('\n')
# For Number3
from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number2, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number2, "RO")
print(carrier.name_for_number(service_number, "en"))