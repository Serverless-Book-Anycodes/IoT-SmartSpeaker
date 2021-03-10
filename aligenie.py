# -*- coding: utf-8 -*-

import bottle
import random


@bottle.route('/', method='POST')
def test():
    return {
        "returnCode": "0",
        "returnErrorSolution": "",
        "returnMessage": "",
        "returnValue": {
            "reply": random.choice(['1', '2', '3', '4', '5', '6']),
            "resultType": "RESULT",
            "executeCode": "SUCCESS",
            "msgInfo": ""
        }
    }


@bottle.route('/aligenie/eaf3f19e4fcac40131ee278cdb0284dd.txt', method='GET')
def token():
    return 'Jfc4Z4Ur15JwUBuvUQD5wg7Nu8+l+HscqYlfofbyJdYyLiBpubYhF9sbUIH/ig6g'


app = bottle.default_app()
if __name__ == "__main__":
    bottle.run(host='localhost', port=8080)
