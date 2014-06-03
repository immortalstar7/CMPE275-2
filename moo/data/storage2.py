"""
Storage interface
"""

import time
import couchdb
from rest_framework import status
from rest_framework.response import Response
from django.core.handlers.wsgi import STATUS_CODE_TEXT

class Storage(object):
    def __init__(self):
        # initialize our storage, data is a placeholder
        self.data = {}

        # for demo
        #self.data['created'] = time.ctime()

    def insert(self, name, value):
        print "---> insert:", name, value
        try:
            self.data[name] = value
            return Response("added", status=status.HTTP_201_CREATED)
        except:
            return Response("error: data not added", status=status.HTTP_501_NOT_IMPLEMENTED)

    def remove(self, name):
        print "---> remove:", name

    def names(self):
        print "---> names:"
        for k in self.data.iterkeys():
            print 'key:', k

    def find(self, name):
        print "---> storage.find:", name
        if name in self.data:
            rtn = self.data[name]
            print "---> storage.find: got value", rtn
            return Response(rtn, status=status.HTTP_200_OK)
        else:
            return Response(None, status=status.HTTP_204_NO_CONTENT)

#-------------------Add New User----------------------Rajvi
    def register(self, name, username, password):
        couch = couchdb.Server()
        db = couch['users']
        print "---> Connected to users"
        try:
           doc = {"name": name, "username": username, "password": password}
           doc_id, doc_rev = db.save(doc)
           return Response("Success: User added", status=status.HTTP_201_CREATED)
        except:
           return Response("error: User not added", status=status.HTTP_501_NOT_IMPLEMENTED)



#------------------Sign In----------------------------Rajvi
    def login(self, username, password):
        couch = couchdb.Server()
        db = couch['users']
        print "---> Connected to users"
        try:
           for index in db:
              doc = db[index]
              if(doc['username'] == username):
                 if(doc['password'] == password):
                    doc_id=doc['_id']
                    return Response(doc['name'], status=status.HTTP_202_ACCEPTED)
                 else:
                    continue
        except:
           print "error: Login Failed"


#-------------------Get User Info by ID--------------------Rajvi

    def getUserInfo(self,user_id):
        couch = couchdb.Server()
        db=couch['users']
        print"---> Connected to users"
        doc2=[]
        try:
           for index in db:
              doc=db[index]
              if(index == user_id):
                 doc2.append("Name: "+`doc['username']`+"\n"+"Boards: "+"\n")
                 print ''.join(doc2)
                 break
        except:
           print Response("error: User Info not found" , status=status.HTTP_200_OK)

        db = couch['boards']
        print "---> Connected to boards"
        try:
            for index in db:
               doc = db[index]
               if(doc['user_id'] == user_id):
                  doc2.append(`doc['board_id']`+`doc['board_name']`+"\n")
                  print ''.join(doc2)
               else:
                  continue

        except:
            print Response("error: User Info not found" , status=status.HTTP_204_NO_CONTENT)



#-------------------Add New Board----------------------Rajvi

    def addBoard(self,user_id,board_id,board_name):
        couch = couchdb.Server()
        db = couch['boards']
        print "---> Connected to boards"
        try:
           doc = {"user_id": user_id, "board_id": board_id, "board_name": board_name}
           doc_id, doc_rev = db.save(doc)
           return Response("Success: Board added in db" , status=status.HTTP_200_OK)
        except:
           return Response("error: Board not added" , status=status.HTTP_400_BAD_REQUEST)

#------------------- Upload a Pin --------------------Darshit

    def addPin(self,user_id,pin_name,pin_path):
        couch = couchdb.Server()
        db = couch['pins']
        print "---> Connected to pins"
        try:
           doc = {"user_id":user_id, "pin_name": pin_name, "pin_path": pin_path}
           doc_id, doc_rev = db.save(doc)
           print Response("Success: Pin added in db" , status=status.HTTP_202_ACCEPTED)
           return doc_id
        except:
           return Response("error: Pin not added" , status=status.HTTP_400_BAD_REQUEST)

#------------------- Attach a Pin --------------------Rajvi

    def attachPin(self,user_id,board_id,pin_id):
        couch = couchdb.Server()
        db = couch['pins']
        print "---> Connected to pins"
        try:
           for index in db:
              doc = db[index]
              if(doc['_id']==pin_id):
                 if(doc['user_id']==user_id):
                    doc['board_id']=board_id
                    db[index]=doc
                    return Response("Success: Pin attached to board" , status=status.HTTP_202_ACCEPTED)
                 else:
                    return Response("Pin not attached" , status=status.HTTP_400_BAD_REQUEST)
        except:
           return Response("error: Unauthorized user" , status=status.HTTP_401_UNAUTHORIZED)



#---------------------Get Boards-------------------------Darshit

    def getAllBoards(self):
        doc2=[]
        couch = couchdb.Server()
        db = couch['boards']
        print "---> Connected to boards"
        try:
            for index in db:
               doc = db[index]
               doc2.append(`doc['board_name']`+"\n")
            return Response(''.join(doc2) , status=status.HTTP_200_OK)
        except:
            print Response("error: Boards not found", status=status.HTTP_204_NO_CONTENT)

#----------------------Get Pins--------------------------Darshit

    def getAllPins(self):
        doc2=[]
        couch = couchdb.Server()
        db = couch['pins']
        print "---> Connected to pins"
        try:
            for index in db:
               doc = db[index]
               doc2.append(`doc['pin_name']`+"\n")
            return Response(''.join(doc2) , status=status.HTTP_200_OK)
        except:
            print Response("error: Pins not found" , status=status.HTTP_204_NO_CONTENT)



#-------------------Get Board by ID--------------------Darshit

    def getBoard(self,board_id):
        couch = couchdb.Server()
        db = couch['boards']
        print "---> Connected to boards"
        try:
            for index in db:
               doc2=[]
               doc = db[index]
               if(doc['_id'] == board_id):
                  doc2.append(`doc['board_name']`)
                  return Response(''.join(doc2) , status=status.HTTP_200_OK)
        except:
            print Response("error: Board not found" , status=status.HTTP_204_NO_CONTENT)


#-------------------Get Pin by ID-----------------------Darshit
    def getPin(self,pin_id):
        couch = couchdb.Server()
        db = couch['pins']
        print "---> Connected to pins"
        try:
            for index in db:
               doc2=[]
               doc = db[index]
               if(doc['_id'] == pin_id):
                  doc2.append(`doc['pin_name']`)
                  return Response(''.join(doc2) , status=status.HTTP_200_OK)
        except:
            print Response("error: pin not found" , status=status.HTTP_204_NO_CONTENT)


#-------------------Delete Board --------------------Rajvi

    def deleteBoard(self,user_Id,board_id):
        couch = couchdb.Server()
        db = couch['boards']
        print "---> Connected to boards"
        try:
           for index in db:
              doc = db[index]
              if(doc['board_id'] == board_id):
                 if(doc['user_id'] == user_Id):
                    doc = db[index]
                    db.delete(doc)
                    print Response("deleted" , status=status.HTTP_200_OK)
                    break
           return "Board deleted"
        except:
            print Response("error: Board not deleted" , status=status.HTTP_400_BAD_REQUEST)


#-------------------Add Comment for pin --------------------Rajvi

    def addComment(self,user_Id,pin_id,comment):
        couch = couchdb.Server()
        db=couch['users']
        try:
           for index in db:
              doc = db[index]
              if(doc['_id']==user_Id):
                 username=doc['username']
                 break
        except:
            print Response("error: user problem" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        db = couch['pins']
        print "---> Connected to pins"
        try:
           for index in db:
              doc = db[index]
              if(doc['_id']==pin_id):
                 doc['comment']=db[index]['comment']+"\n"+username+":"+comment
                 db[index]=doc
                 break
           return Response("Success: Comment added for the Pin" , status=status.HTTP_200_OK)
        except:
           return Response("error: Failed to add comment" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
