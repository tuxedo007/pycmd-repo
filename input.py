



def currency_converter(rate,canDollars):
    usDollars = rate*canDollars
    return usDollars

r=input("Enter rate: ")
c=input("Enter Canadian $: ")
print(currency_converter(float(r), float(c)))