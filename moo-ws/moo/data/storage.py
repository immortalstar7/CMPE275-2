"""
Storage interface
"""

import time
import couchdb


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
            return "added"
        except:
            return "error: data not added"

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
            return rtn
        else:
            return None

#-------------------Add New User----------------------Manushi Doshi
    def register(self, name, username, password):
        couch = couchdb.Server()
        db = couch['users']
        print "---> Connected to users"
        try:
           doc = {"name": name, "username": username, "password": password}
           doc_id, doc_rev = db.save(doc)
           return "Success: User added"
        except:
           return "error: User not added"


#------------------Sign In----------------------------Manushi Doshi
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
                    return doc['name']
                 else:
                    continue
        except:
           print "error: Login Failed"


#-------------------Get User Info by ID--------------------Dhrumit Sheth

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
           print "error: User Info not found"

        db = couch['boards']
        print "---> Connected to boards"
        try:
            for index in db:
               doc = db[index]
               if(doc['user_id'] == user_id):
                  doc2.append(`doc['board_id']`+`doc['board_name']`+"\n")
                  print ''.join(doc2)
                  return ''.join(doc2)
               else:
                  continue
        except:
            print "error: User Info not found"



#-------------------Add New Board----------------------Darshit Kuwadia

    def addBoard(self,user_id,board_id,board_name):
        couch = couchdb.Server()
        db = couch['boards']
        print "---> Connected to boards"
        try:
           doc = {"user_id": user_id, "board_id": board_id, "board_name": board_name}
           doc_id, doc_rev = db.save(doc)
           return "Success: Board added in db"
        except:
           return "error: Board not added"

#------------------- Upload a Pin --------------------Rajvi Shah

    def addPin(self,user_id,pin_name,pin_path):
        couch = couchdb.Server()
        db = couch['pins']
        print "---> Connected to pins"
        try:
           doc = {"user_id":user_id, "pin_name": pin_name, "pin_path": pin_path}
           doc_id, doc_rev = db.save(doc)
           print "Success: Pin added in db"
           return doc_id
        except:
           return "error: Pin not added"

#------------------- Attach a Pin --------------------Rajvi Shah

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
                    return "Success: Pin attached to board"
                 else:
                    return "Pin not attached"
        except:
           return "error: Unauthorized user"



#---------------------Get Boards-------------------------Darshit Kuwadia

    def getAllBoards(self):
        doc2=[]
        couch = couchdb.Server()
        db = couch['boards']
        print "---> Connected to boards"
        try:
            for index in db:
               doc = db[index]
               doc2.append(`doc['board_name']`+"\n")
            return ''.join(doc2)
        except:
            print "error: Boards not found"

#----------------------Get Pins--------------------------Rajvi Shah

    def getAllPins(self):
        doc2=[]
        couch = couchdb.Server()
        db = couch['pins']
        print "---> Connected to pins"
        try:
            for index in db:
               doc = db[index]
               doc2.append(`doc['pin_name']`+"\n")
            return ''.join(doc2)
        except:
            print "error: Pins not found"



#-------------------Get Board by ID--------------------Darshit Kuwadia

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
                  return ''.join(doc2)
        except:
            print "error: Board not found"


#-------------------Get Pin by ID-----------------------Kavish Parikh
    def getPin(self,pin_id):
        couch = couchdb.Server()
        db = couch['pins']
        print "---> Connected to pins"
        try:
            for index in db:
               doc2=[]
               doc = db[index]
               if(doc['_id'] == pin_id):
                  return doc
        except:
            print "error: pin not found"


#-------------------Delete Board --------------------Dhrumit Sheth

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
                    print "deleted"
                    break
           return "Board deleted"
        except:
            print "error: Board not deleted"


#-------------------Add Comment for pin --------------------Kavish Parikh

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
            print "error: user problem"

        db = couch['pins']
        print "---> Connected to pins"
        try:
           for index in db:
              doc = db[index]
              if(doc['_id']==pin_id):
                 doc['comment']=db[index]['comment']+"\n"+username+":"+comment
                 db[index]=doc
                 break
           return "Success: Comment added for the Pin"
        except:
           return "error: Failed to add comment"