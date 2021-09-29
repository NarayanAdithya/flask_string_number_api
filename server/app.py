from re import UNICODE
from flask import Flask, json, jsonify, abort, make_response, request

app = Flask(__name__)

@app.route('/check/palindrome/<string>')
def chk_palindrome(string):
    val=bool(string==string[::-1])
    return jsonify({'result':val})

@app.route('/check/anagram/<string1>/<string2>')
def chk_anagram(string1,string2):
    if(sorted(string1)== sorted(string2)):
        return jsonify({'result':1})
    else:
        return jsonify({'result':0})

@app.route('/check/prime/<int:n>')
def chk_prime(n):
    flag = False
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                flag = True
                break
    if flag:
        return jsonify({'result':0})
    else:
        return jsonify({'result':1})

@app.route('/check/armstrong/<int:n>')
def chk_armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        return jsonify({'result':1})
    else:
        return jsonify({'result':0})