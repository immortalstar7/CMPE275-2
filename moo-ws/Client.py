
import urllib,urllib2
import json
import requests

server=raw_input("Please enter the host to connect: ")
port=raw_input("please enter the port number: ")

choice = int(raw_input("Enter your choice:\n 1. Register\n 2. Login\n 3. UserInfo\n 4. Create New Board\n"
                       " 5. Create New Pin\n 6. Attach Pin to Board\n 7. List Boards\n 8. List Pins\n"
                       " 9. Get Board for id\n 10. Get Pin for id\n 11. Delete Board\n 12. Add comment for a pin\n"))

if choice == 1:
   name = raw_input("Enter your Name: ")
   username = raw_input("Enter UserName :")
   password = raw_input("Enter Password :")
   url = 'http://'+server+':'+port+'/v1/reg'
   params=urllib.urlencode({'name':name,'username':username,'password':password})
   data=urllib.urlopen(url,params).read()
   print data

elif choice == 2:
   uname=raw_input("enter Username ")
   psd=raw_input("enter password ")
   url= 'http://'+server+':'+port+'/v1/login'
   username=uname
   password=psd
   params=urllib.urlencode({'username':username,'password':password})
   data=urllib.urlopen(url,params).read()
   print data

elif choice == 3:
   userid = raw_input("Enter user id: ")
   param=urllib.urlencode({'user_id':userid})
   url = 'http://'+server+':'+port+'/v1/user/'+userid
   data = urllib.urlopen(url).read()
   print data

elif choice == 4:
   userid = raw_input("Enter your user_id: ")
   url = 'http://'+server+':'+port+'/v1/user/'+userid+'/board'
   boardname = raw_input("Enter board name: ")
   board_id = raw_input("Enter board id: ")
   params=urllib.urlencode({'board_name':boardname,'board_id':board_id})
   data=urllib.urlopen(url,params).read()
   print data

elif choice == 5:
   userid = raw_input("Enter your user_id: ")
   url = 'http://'+server+':'+port+'/v1/user/'+userid+'/pin'
   pin_name = raw_input("Enter pin name: ")
   pin_path = raw_input("Enter file Location: ")
   params=urllib.urlencode({'pin_name':pin_name,'pin_path':pin_path})
   data=urllib.urlopen(url,params).read()
   print data

elif choice == 6:
   userid = raw_input("Enter your user_id: ")
   boardid = raw_input("Enter Board_id: ")
   url = 'http://'+server+':'+port+'/v1/user/'+userid+'/board/'+boardid
   pin_id = raw_input("Enter pin_id to be attached to "+boardid+": ")
   params=urllib.urlencode({'pin_id':pin_id})
   data=urllib.urlopen(url,params).read()
   print data

elif choice == 7:
   url = 'http://'+server+':'+port+'/v1/boards'
   data = urllib.urlopen(url).read()
   print data

elif choice == 8:
   url = 'http://'+server+':'+port+'/v1/pins'
   data = urllib.urlopen(url).read()
   print data

elif choice == 9:
   board_id = raw_input("Enter Board_id: ")
   url = 'http://'+server+':'+port+'/v1/boards/'+board_id
   data = urllib.urlopen(url).read()
   print data

elif choice == 10:
   pin_id = raw_input("Enter Pin id: ")
   url = 'http://'+server+':'+port+'/v1/pins/'+pin_id
   data = urllib.urlopen(url).read()
   print data

elif choice == 11:
   user_id = raw_input("Enter your user_id: ")
   board_id = raw_input("Enter Board_id: ")
   url = 'http://'+server+':'+port+'/v1/deleteBoard/'+user_id+'/'+board_id
   response=requests.delete(url)
   print response

elif choice == 12:
   user_id = raw_input("Enter user_id: ")
   board_id = raw_input("Enter Board_id: ")
   pin_id = raw_input("Enter Pin_id: ")
   comment = raw_input("Enter comment: ")
   url = 'http://'+server+':'+port+'/v1/'+user_id+'/boards/'+board_id+'/pins/'+pin_id+'/comment'
   param=urllib.urlencode({'comment':comment})
   data = urllib.urlopen(url,param).read()
   print data