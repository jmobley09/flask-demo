#!/usr/bin/python3
from flask import Flask,jsonify,request,render_template

#this line is used to instaniate the Flask object
#Look into OOP for more info
app = Flask(__name__)

#add default route to "/"
@app.route('/')

#get /store

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)


###
# CHALLENGES -- Will get to if time permits
###


#get /store/<name> data: {name :}


#post /store/<name> data: {name :}

#get /store/<name>/item data: {name :}

#This line starts the server on port 5000
app.run(port=5000)