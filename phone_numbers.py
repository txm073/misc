import phonenumbers
from phonenumbers import geocoder, carrier
from text import number

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))
isp = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(isp, "en"))
