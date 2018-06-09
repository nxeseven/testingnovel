#from subprocess import Popen, PIPE
from subprocess import *
from time import sleep
import re
#call('tail -n 1 nukkit/server.log',shell=True)
#sleep(3)
#call('tail -n 1 nukkit/server.log',shell=True)
#output = check_output('cd nukkit; ls',shell=True)
#print(output)
#word = raw_input('what are you looking for?')

#if word in output:
#    print 'file found'
#report = 0
# Run "cat", which is a simple Linux program that prints it's input.
process = Popen(['sudo java -jar nukkit.jar'], shell=True, stdin=PIPE, stdout=PIPE)
#print (process.stdout.read())
# process = Popen(['ls nukkit/'], stdin=PIPE, stdout=PIPE)
#sout = process.communicate()[0]
#print 'STDOUT:{}'.format(sout)
#print (process.stdout.readline())
#print(str(report))
#while report < 23:
#    print (str(report))
#    scanoutline =  process.stdout.readline()
#    print (scanoutline)
#    report += 1
# appended region

while process.poll() is None:
    l = process.stdout.readline() # This blocks until it receives a newline.
    print l
    if "Done" in l:
        break
# When the subprocess terminates there might be unconsumed output 
# that still needs to be processed.

#print process.stdout.read()
#^^appended region

#6 times counting this one, maybe, I think proceeding after
#print (process.stdout.readline())

#sleep for 20 seconds
sleep(20)

process.stdin.write('say hello\n')
print (process.stdout.readline())
process.stdin.write('time set day\n')
print (process.stdout.readline())

process.stdin.write('weather clear\n')
print (process.stdout.readline())

#print (process.stdout.readline())
for x in range(10):
    sleep(1)
    process.stdin.write('sudo Steve lightning\n')
    print (process.stdout.readline())

sleep(5)
process.stdin.write('sudo Steve tp 200 100 200\n')
print (process.stdout.readline())
location = process.stdout.readline()
print("location")
print(location)
print(location)
print (process.stdout.readline())
sleep(10)
process.stdin.write('coords Steve\n')
#while process.stdout.readline() != "":
#    print (process.stdout.readline())

#7 times counting this one
# print (process.stdout.readline())

while process.poll() is None:
    l = process.stdout.readline() # This blocks until it receives a newline.
    print l
    if "positioned" in l:
        placement = l[-28:]
        print placement
        locext = re.findall(r"[-+]?\d*\.\d+|\d+", placement)
        print locext
        print locext[0]
        
        #for item in placement:
        #    if
        break



#print (location[14:-10])
#sleep(10)
#output = check_output('tail -n 1 nukkit/server.log', shell=True)
#print (output)

sleep(10)

process.stdin.write('sudo Steve tp 100 100 1000\n')
sleep(10)
process.stdin.write('sudo Steve /pos1 100,100,1000\n')
sleep(1)
process.stdin.write('sudo Steve /pos2 110,110,1010\n')
sleep(1)
process.stdin.write('sudo Steve /set 1\n')
sleep(0.5)
process.stdin.write('sudo Steve /set 40\n')
sleep(0.5)
process.stdin.write('sudo Steve /set 1\n')
sleep(0.5)
process.stdin.write('sudo Steve /set 40\n')
sleep(0.5)
process.stdin.write('sudo Steve /set 2\n')
sleep(0.5)
process.stdin.write('sudo Steve /set 1\n')
sleep(0.5)
process.stdin.write('sudo Steve /set 2\n')
sleep(0.5)
process.stdin.write('sudo Steve /set 1\n')
sleep(0.5)
process.stdin.write('sudo Steve /set 2\n')
sleep(0.5)
process.stdin.write('sudo Steve /set air\n')
sleep(0.5)
print ("blink")

process.stdin.write('stop\n')
#print (process.stdout.readline())

# "cat" will exit when you close stdin.  (Not all programs do this!)
process.stdin.close()
#print 'Waiting for cat to exit'
process.wait()
print 'server finished with return code %d' % process.returncode
