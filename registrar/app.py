# app.py
#
# Use this sample code to handle webhook events in your integration.
#
# 1) Paste this code into a new file (app.py)
#
# 2) Install dependencies
#   pip3 install flask
#   pip3 install requests
#
# 3) Run the server on http://localhost:4242
#   python3 -m flask run --port=4242

import json
import os
import requests

from flask import Flask, jsonify, request

# This is your Stripe CLI webhook secret for testing your endpoint locally.

app = Flask(__name__)

@app.route('/register-instance', methods=['POST'])
def webhook():
    event = None
    ip = request.form["ip"]
    name = request.form["name"]
    print(ip, name)
    try:
        ip_address = ip
        requested_name = name
        url = 'http://localhost:2019/config/apps/http/servers/srv0/routes'
        myobj = {
        'handle': """
[
			                  {
				                  "handler": "subroute",
				                  "routes": [
				                    {
					                    "handle": [
					                      {
						                      "handler": "reverse_proxy",
                                  "upstreams": [
                                    {
                                      "dial": "3.139.105.219:8080"
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
			                  }
			                ]
        """,
        'match': """
[
                        {
                          "host": [
                            "hasura-0012.rocketgraph.app"
                          ]
                        }
            ]
        """,
        "terminal": "true"
        }

        x = requests.post(url, data = myobj)

        print(x.text)
    except ValueError as e:
        # Invalid payload
        raise e
    return jsonify(succeeded=True)

    # try:
    #     event = stripe.Webhook.construct_event(
    #         payload, sig_header, endpoint_secret
    #     )
    # except ValueError as e:
    #     # Invalid payload
    #     raise e
    # except stripe.error.SignatureVerificationError as e:
    #     # Invalid signature
    #     raise e

    # # Handle the event
    # if event['type'] == 'payment_intent.succeeded':
    #   payment_intent = event['data']['object']
    # # ... handle other event types
    # else:
    #   print('Unhandled event type {}'.format(event['type']))

    return jsonify(success=True)