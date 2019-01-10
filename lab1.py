import requests

# prints the version of the request package
print(requests.__version__)

# This makes a get request to the google homepage
r = requests.get("http://www.google.com")
print(r.status_code)

# This gets this script from its direct link on github and prints it
r = requests.get("https://raw.githubusercontent.com/rsauvehoover/CMPUT404-lab-1/master/lab1.py")
print(r.text)

