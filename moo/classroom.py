"""
6, Apr 2013

Example domain logic for the RESTful web service example.

This class provides basic configuration, storage, and logging.
"""

import sys
import os
import socket
import StringIO
import json

# moo 
from data.storage import Storage

#
# Room (virtual classroom -> Domain) functionality - note this is separated 
# from the RESTful implementation (bottle)
#
# TODO: only return objects/data and let moo.py handle formatting through 
# templates
#
class Room(object):
   json, xml, html, text = range(1,5)
   
   #
   # setup the configuration for our service
   #
   def __init__(self,base,conf_fn):
      self.host = socket.gethostname()
      self.base = base
      self.conf = {}
      
      # should emit a failure (file not found) message
      if os.path.exists(conf_fn):
         with open(conf_fn) as cf:
            for line in cf:
               name, var = line.partition("=")[::2]
               self.conf[name.strip()] = var.strip()
      else:
         raise Exception("configuration file not found.")

      # create storage
      self.__store = Storage()
   

   #
   # example: find data
   #
   def find(self,name):
      print '---> classroom.find:',name
      return self.__store.find(name)

   #
   # example: add data
   #
   def add(self,name,value):
      try:
         self.__store.insert(name,value)
         self.__store.names();
         return 'success'
      except:
         return 'failed'


#-----------------------------------------------------------------------------------------

   #
   #--------registration data----------------Manushi Doshi
   #
   def addUser(self,name,username,password):
      print "In Classroom"
      try:
         self.__store.register(name,username,password)
         return "Registration successful"
      except:
         return 'error: Registration Failed'


   #
   #-----------login data-----------------Manushi Doshi
   #
   def login(self,username,password):
      try:
         doc_id=self.__store.login(username,password)
         return "Login Successful for "+doc_id
      except:
         return 'error: Login failed'


   #
   #-----------UserInfo data-----------------Dhrumit Sheth
   #
   def getUserInfo(self,user_id):
      try:
         return self.__store.getUserInfo(user_id)

      except:
         return "error: User Info retrieval failed"


   #
   #--------create board data-----------------Darshit Kuwadia
   #
   def addBoard(self,user_id,board_id,board_name):
      try:
         self.__store.addBoard(user_id,board_id,board_name)
         return "New Board Created"
      except:
         return 'error: Board creation failed'


   #
   #--------- add Pin data-----------------Rajvi Shah
   #
   def addPin(self,user_id,pin_name,pin_path):
      try:
         self.__store.addPin(user_id,pin_name,pin_path)
         return "Pin Created"
      except:
         return 'error: Pin Creation failed'


   #
   #------------ attach pin data-----------------Rajvi Shah
   #
   def attachPin(self,user_id,board_id,pin_id):
      try:
         self.__store.attachPin(user_id,board_id,pin_id)
         return 'Pin attached to the board'
      except:
         return 'error: Attachment failed'



   #
   #-------------- get all boards data-----------------Darshit Kuwadia
   #
   def getAllBoards(self):
      try:
         return self.__store.getAllBoards()
      except:
         print "error: Get All boards failed"


   #
   #-------------- get all Pins data-----------------Rajvi Shah
   #
   def getAllPins(self):
      try:
         return self.__store.getAllPins()
      except:
         print "error: Get All pins failed"



   #
   #-------------- get board by ID data-----------------Darshit Kuwadia
   #
   def getBoard(self,board_id):
      try:
         return self.__store.getBoard(board_id)
      except:
         print "error: GetBoard failed"



   #
   #-------------- get Pin by ID data----------------Kavish Parikh
   #
   def getPin(self,pin_id):
      try:
         return self.__store.getPin(pin_id)
      except:
         print "error: Get Pin failed"



   #
   #-------------- delete board data-----------------Dhrumit Sheth
   #
   def deleteBoard(self,user_Id,board_Id):
      try:
         return self.__store.deleteBoard(user_Id,board_Id)

      except:
         return 'error: Board deletion failed'


   #
   #-------------- addComment data-----------------Kavish Parikh
   #
   def addComment(self,user_id,pin_id,comment):
      try:
         return self.__store.addComment(user_id,pin_id,comment)
      except:
         print "error:Comment not added"


   def dump_conf(self,format):
      if format == Room.json:
         return self.__conf_as_json()
      elif format == Room.html:
         return self.__conf_as_html()
      elif format == Room.xml:
         return self.__conf_as_xml()
      elif format == Room.text:
         return self.__conf_as_text()
      else:
         return self.__conf_as_text()

   #
   # output as xml is supported through other packages. If
   # you want to add xml support look at gnosis or lxml.
   #
   def __conf_as_json(self):
      return "xml is hard"

   #
   #
   #
   def __conf_as_json(self):
      try:
         all = {}
         all["base.dir"] = self.base
         all["conf"] = self.conf
         return json.dumps(all)
      except:
         return "error: unable to return configuration"

   #
   #
   #
   def __conf_as_text(self):
      try:
        sb = StringIO.StringIO()
        sb.write("Room Configuration\n")
        sb.write("base directory = ")
        sb.write(self.base)
        sb.write("\n\n")
        sb.write("configuration:\n")
        
        for key in sorted(self.conf.iterkeys()):
           print >>sb, "%s=%s" % (key, self.conf[key])
        
        str = sb.getvalue()
        return str
      finally:
        sb.close()

#
      return "text"

   #
   #
   #
   def __conf_as_html(self):
      try:
        sb = StringIO.StringIO()
        sb.write("<html><body>")
        sb.write("<h1>")
        sb.write("Rooms Configuration")
        sb.write("</h1>")
        sb.write("<h2>Base Directory</h2>\n")
        sb.write(self.base)
        sb.write("\n\n")
        sb.write("<h2>Configuration</h2>\n")
        
        sb.write("<pre>")
        for key in sorted(self.conf.iterkeys()):
           print >>sb, "%s=%s" % (key, self.conf[key])
        sb.write("</pre>")
     
        sb.write("</body></html>")

        str = sb.getvalue()
        return str
      finally:
        sb.close()

#
# test and demonstrate the setup
#
if __name__ == "__main__":
  if len(sys.argv) > 2:
     base = sys.argv[1]
     conf_fn = sys.argv[2]
     svc = Room(base,conf_fn)
     svc.dump_conf()
  else:
     print "usage:", sys.argv[0],"[base_dir] [conf file]"
