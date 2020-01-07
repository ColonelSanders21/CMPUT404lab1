import requests

print(requests.__version__)

# google = requests.get('https://www.google.com/')
# print(google)

raw = requests.get('https://raw.githubusercontent.com/ColonelSanders21/CMPUT404lab1/master/404lab1.py')
print(raw.content)