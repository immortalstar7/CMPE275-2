"""
6, Apr 2013

Example bottle (python) RESTful web service.

This example provides a basic setup of a RESTful service

Notes
1. example should perform better content negotiation. A solution is
   to use minerender (https://github.com/martinblech/mimerender)
"""

import time
import sys
import socket
import couchdb
import data.storage
# bottle framework
from bottle import request, response, route, run, template

# moo
from classroom import Room

# virtual classroom implementation
room = None

def setup(base,conf_fn):
   print '\n**** service initialization ****\n'
   global room 
   global server
   global db
   room = Room(base,conf_fn)
   server = couchdb.Server()

#
# setup the configuration for our service
@route('/')
def root():
   print "--> root"
   return 'welcome'


@route('/moo/ping', method='GET')
def ping():
   return 'ping %s - %s' % (socket.gethostname(),time.ctime())

#
# Development only: echo the configuration of the virtual classroom.
#
# Testing using curl:
# curl -i -H "Accept: application/json" http://localhost:8082/moo/conf
#
# WARN: This method should be disabled or password protected - dev only!
#

@route('/moo/conf', method='GET')
def conf():
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   return room.dump_conf(fmt)

#
# example of a RESTful method. This example is very basic, it does not 
# support much in the way of content negotiation.
#
@route('/moo/echo/:msg')
def echo(msg):
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   if fmt == Room.html:
      return '<h1>%s</h1>' % msg
   elif fmt == Room.json:
      rsp = {}
      rsp["msg"] = msg
      return json.dumps(all)
   else:	
      return msg


#
# example of a RESTful query
#
@route('/moo/data/:name', method='GET')
def find(name):
   print '---> moo.find:',name
   print db[name]

#
# example adding data using forms
#
@route('/moo/data', method='POST')
def add():
   print '---> moo.add'

   # example list form values
   for k,v in request.forms.allitems():
      print "form:",k,"=",v

   name = request.forms.get('name')
   value = request.forms.get('value')
   return room.add(name,value)

#
# Determine the format to return data (does not support images)
#
# Accept-Datetime, etc should also exist
#
def __format(request):
   #for key in sorted(request.headers.iterkeys()):
   #   print "%s=%s" % (key, request.headers[key])

   types = request.headers.get("Accept",'')
   subtypes = types.split(",")
   for st in subtypes:
      sst = st.split(';')
      if sst[0] == "text/html":
         return Room.html
      elif sst[0] == "text/plain":
         return Room.text
      elif sst[0] == "application/json":
         return Room.json
      elif sst[0] == "*/*":
         return Room.json

      # TODO
      # xml: application/xhtml+xml, application/xml
      # image types: image/jpeg, etc

   # default
   return Room.html

#
# The content type on the reply
#
def __response_format(reqfmt):
      if reqfmt == Room.html:
         return "text/html"
      elif reqfmt == Room.text:
         return "text/plain"
      elif reqfmt == Room.json:
         return "application/json"
      else:
         return "*/*"


#------------Registration --------------------------Manushi Doshi
@route('/v1/reg', method='POST')
def registration():
   db = server['users']
   print '---> moo.addingUser'
   name = request.POST.get('name')
   username = request.POST.get('username')
   password = request.POST.get('password')
   return room.addUser(name,username,password)



#-------------Login --------------------------Manushi Doshi
@route('/v1/login', method='POST')
def login():
   db = server['users']
   print '---> moo.signIn'
   username = request.POST.get('username')
   password = request.POST.get('password')
   return room.login(username,password)



#-------------Get User Info --------------------------Dhrumit Sheth
@route('/v1/user/<user_id>', method='GET')
def getUserInfo(user_id):
   db = server['users']
   print '---> moo.UserInfo'
   return room.getUserInfo(user_id)



#------------Create Board--------------------------Darshit Kuwadia
@route('/v1/user/<user_id>/board', method='POST')
def addBoard(user_id):
   db = server['boards']
   print '---> moo.addingBoard'
   board_name = request.POST.get('board_name')
   board_id = request.POST.get('board_id')
   return room.addBoard(user_id,board_id,board_name)



#------------Create Pin--------------------------Rajvi Shah
@route('/v1/user/<user_id>/pin', method='POST')
def addPin(user_id):
   db = server['pins']
   print '---> moo.uploading Pin'
   pin_name = request.POST.get('pin_name')
   pin_path = request.POST.get('pin_path')
   return room.addPin(user_id,pin_name,pin_path)



#------------Attach Pin--------------------------Rajvi Shah
@route('/v1/user/<user_id>/board/<board_id>', method='POST')
def attachPin(user_id,board_id):
   db = server['pins']
   print '---> moo.attaching Pin'
   pin_id = request.POST.get('pin_id')
   return room.attachPin(user_id,board_id,pin_id)



#---------------Get Boards --------------------------Darshit Kuwadia
@route('/v1/boards', method='GET')
def getAllBoards():
   db = server['boards']
   print '---> moo.getAllBoards'
   return room.getAllBoards()



#---------------Get Pins --------------------------Rajvi Shah
@route('/v1/pins', method='GET')
def getAllPins():
   db = server['pins']
   print '---> moo.getAllPins'
   return room.getAllPins()



#---------------Get Board by Id --------------------------Darshit Kuwadia
@route('/v1/boards/<board_id>', method='GET')
def getBoard(board_id):
   db = server['boards']
   print '---> moo.getBoardById'
   return room.getBoard(board_id)



#-----------------Get Pin by Id --------------------------Kavish Parikh
@route('/v1/pins/<pin_id>', method='GET')
def getPin(pin_id):
   db = server['pins']
   print '---> moo.getPinById'
   return room.getPin(pin_id)



#------------------Delete Board --------------------------Dhrumit Sheth
@route('/v1/deleteBoard/<user_id>/<board_id>', method='DELETE')
def deleteBoard(user_id,board_id):
   db = server['boards']
   print '---> moo.deleteBoard'
   return room.deleteBoard(user_id,board_id)



#-------------------Add Comment--------------------------Kavish Parikh
@route('/v1/<user_id>/boards/<board_id>/pins/<pin_id>/comment', method='POST')
def addComment(user_id,board_id,pin_id):
   db = server['pins']
   print '---> moo.addComment'
   comment=request.POST.get('comment')
   return room.addComment(user_id,pin_id,comment)
