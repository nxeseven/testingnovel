#from subprocess import Popen, PIPE
from subprocess import *
from time import sleep

#call('tail -n 1 nukkit/server.log',shell=True)
#sleep(3)
#call('tail -n 1 nukkit/server.log',shell=True)
#output = check_output('cd nukkit; ls',shell=True)
#print(output)
#word = raw_input('what are you looking for?')

#if word in output:
#    print 'file found'
report = 0
# Run "cat", which is a simple Linux program that prints it's input.
process = Popen(['sudo java -jar nukkit.jar'], shell=True, stdin=PIPE, stdout=PIPE)
print (process.stdout.read())
# process = Popen(['ls nukkit/'], stdin=PIPE, stdout=PIPE)
#sout = process.communicate()[0]
#print 'STDOUT:{}'.format(sout)
#print (process.stdout.readline())
print(str(report))
while report < 23:
    print (str(report))
    scanoutline =  process.stdout.readline()
    print (scanoutline)
    report += 1

print (process.stdout.readline())
#print (process.stdout.readline())
#print (process.stdout.readline())
#print (process.stdout.readline())
#print (process.stdout.readline())
#print (process.stdout.readline())

#sleep(10)
#process.stdin.write('eng\n')
#process.stdin.write('hello\n')
#sleep(3)
#print (process.stdout.readline()) # Should print 'Hello\n'

sleep(20)

process.stdin.write('say hello\n')
print (process.stdout.readline())
process.stdin.write('time set day\n')
print (process.stdout.readline())

process.stdin.write('weather clear\n')
print (process.stdout.readline())

#print (process.stdout.readline())

sleep(5)
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
print (process.stdout.readline())
print (process.stdout.readline())
print (process.stdout.readline())
print (process.stdout.readline())
print (process.stdout.readline())
print (process.stdout.readline())
print (process.stdout.readline())
print (process.stdout.readline())


#print (location[14:-10])
#sleep(10)
#output = check_output('tail -n 1 nukkit/server.log', shell=True)
#print (output)

sleep(10)

process.stdin.write('stop\n')
#print (process.stdout.readline())

#process.stdin.write('ls')
#print repr(process.stdout.readline()) # Should print 'World\n'
#sleep(3)
#print (process.stdout.readline())

#sleep(3)
#print (process.stdout.readline())

# "cat" will exit when you close stdin.  (Not all programs do this!)
process.stdin.close()
#print 'Waiting for cat to exit'
process.wait()
print 'server finished with return code %d' % process.returncode
