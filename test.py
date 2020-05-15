import sys
import requests

print(sys.version)
print(sys.executable)


def currency_converter(rate, dollars):
    usDollars = rate * dollars
    return usDollars


print(currency_converter(0.7, 25))


r = requests.get("https://pairadice.pythonanywhere.com/")
print(r.status_code)
