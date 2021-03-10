# -*- coding: utf-8 -*-

import bottle
import random


@bottle.route('/', method='POST')
def test():
    return {
        "is_session_end": True,
        "version": "1.0",
        "response": {
            "open_mic": True,
            "to_speak": {
                "type": 0,
                "text": random.choice(['1', '2', '3', '4', '5', '6'])},
        }
    }


app = bottle.default_app()
