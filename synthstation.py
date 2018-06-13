my_file = open("hst.py","r") #ability that reads your voice document 
docread = my_file.read() #reads entire document, used to be 'thing'
#docread2 = my_file.readline() #reads line and subsequent lines when repeated
my_file.close()

register = 0 #reports the number as string is counted from begninning to end
lock = 0 #reports word length
#name = "The Beats"

key = raw_input("What would you like to add?") #entry written to music.txt
key2 = raw_input("What would you like to addz?")
key3 = raw_input("What would you like to addb?")

def write(access):
    print "It's been written " + access

def loop():
    hs = open("music.txt","a") #a means append
    hs.write("loop do \n") #how to add newline wriiting messages
    #hs.write(list_word)
    hs.close()

def hello():
    hs = open("music.txt","a") #a means append
    hs.write("play " + key+"\n")
    hs.write("play " + key2+"\n") #how to add newline wriiting messages
    hs.write("play " + key3+"\n")
    #hs.write(list_word)
    hs.close()

def end():
    hs = open("music.txt","a") #a means append
    hs.write("end \n") #how to add newline wriiting messages
    #hs.write(list_word)
    hs.close()

def sleep():
    hs = open("music.txt","a")
    hs.write("sleep ")
    hs.close()

def number(setnumber):
    hs = open("music.txt","a")
    hs.write(setnumber)
    hs.close()

def space():
    hs = open("music.txt","a")
    hs.write(" ")
    hs.close()

def close():
    hs = open("music.txt","a")
    hs.write("\n")
    hs.close()

def divide():
    hs = open("music.txt","a")
    hs.write("/")
    hs.close()

def thread():
    hs = open("music.txt","a")
    hs.write("in_thread do \n")
    hs.close()

    
list_word = {"loop":loop,"hello":hello,"end":end, "sleep":sleep, "space":space,
             "close":close, "divide":divide, "thread":thread}
#list_func = [workerz(), worker(), workerz(), workerz(), workerz(),workerz()]

for target in docread: #target rolls through the entire document
    if target != " ": #is target a space or character
        lock += 1 #begins the words length grapple, adding as characters continue
    else: #aka when target == " "
        if docread[register-lock:register].isalpha():
            print target #per letter basis of docread
            print docread[register-lock:register] # per word basis
            list_word[docread[register-lock:register]]()
            lock = 0
        elif docread[register-lock:register].isalnum():
            print target
            print "number: " + docread[register-lock:register]
            number(docread[register-lock:register])
            lock = 0
        else:
            print target
            print "something else: " + docread[register-lock:register]
            lock = 0
    register += 1
