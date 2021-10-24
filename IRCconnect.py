import socket
import sys
 
server = ""       #settings
channel = ""
botnick = ""
 
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print "connecting to:"+server
irc.connect((server, 6667))                                                         #connects to the server
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n") #user authentication
irc.send("NICK "+ botnick +"\n")                            #sets nick
irc.send("PRIVMSG \r\n")    #auth        #join the chan
#irc.send("JOIN "+ channel +"\n")
 
while 1:    #puts it in a loop
   text=irc.recv(2040)  #receive the text
   print text   #print text to console

  

