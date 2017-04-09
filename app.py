#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, send_file, jsonify, request
from sendgrid.helpers.mail import *
import sendgrid

app = Flask(__name__)


@app.route('/')
def index():
    return send_file('templates/index.html')


@app.route('/sendMail', methods=['POST'])
def send_simple_messageend():
    try:
        json_data = request.json
        from_email = Email(str(json_data['from_email']))
        to_email = Email(str(json_data['to_email']))
        subject = str(json_data['subject'])
        msg = str(json_data['message']) + '<br/> <br/>' + 'Regards,' \
              + '<br/> ' + str(json_data['name'])
        message = Content('text/html', msg)
        api_key = str(json_data['api_key'])
        sg = sendgrid.SendGridAPIClient(api_key=api_key)
        mail = Mail(from_email, subject, to_email, message)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return jsonify(status='SUCCESS')
    except:
        print('Message not sent')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

