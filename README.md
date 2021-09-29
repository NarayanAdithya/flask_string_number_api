# flask_string_number_api
Simple Flask API made to demonstrate CI Pipeline in Jenkins using Python

## About the API

The API has 4 endpoints which can be categorised under 2 majore operations

1. String Operations
2. Number Operations

### String Operations

1. Check Anagrams -  GET `/check/anagram/<string1>/<string2>`
2. Check Palindrome - GET `/check/palindrome/<string>`

### Number Operations

1. Check Prime - GET `/check/prime/<number>`
2. Check Armstrong Number - GET `/check/armstrong/<number>`

## Jenkins CI Actions

1. Build Job  - `pip install -r requirements.txt`
2. Test Job - `python3 -m pytest .`
3. Packing Job - `python3 -m zipapp server`

The final artifact collected from the CI pipeline is a server.pyz file.

The `__main__` file runs on calling `python server.pyz`
