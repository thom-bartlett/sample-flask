from flask import Flask, request
from flask import render_template
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

import logging

logging.basicConfig(level=logging.DEBUG)

app = App()

@app.event("app_mention")
def event_test(body, say, logger):
    logger.info(body)
    say("What's up?")

@app.event("message")
def handle_message():
    pass

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

@flask_app.route("/", methods=["POST"])
def slack_events():
    print("testing")
    return handler.handle(request)
