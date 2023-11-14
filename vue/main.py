import os
import openai
from flask import Flask, request, make_response
from flask_cors import *


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/makeimg',methods=['GET'])
def makeimg():
  print("makeimg")
  openai.api_key = "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"
  textMsg = request.args.get('textMsg')

  pro="\""+textMsg +"\""
  response = openai.Image.create(
    prompt=pro,
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']

  print(image_url)
  # resp = make_response(image_url)
  # resp.headers['Access-Control-Allow-Origin'] = '*'

  return  image_url


@app.route('/startimg',methods=['GET'])

def startimg():
  print("startimg")
  openai.api_key = "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"

  response = openai.Image.create(
    prompt="A clear uncomplicated picture，It can be described in short sentences",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']

  print(image_url)

  resp = make_response(image_url)
  resp.headers['Access-Control-Allow-Origin'] = '*'

  return resp


if __name__ == '__main__':
   app.run()