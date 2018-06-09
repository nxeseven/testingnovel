from subprocess import *
from time import sleep


cam1 = Popen(['sudo java -jar nukkit.jar'], shell=True, stdin=PIPE, stdout=PIPE)
#cam2 = Popen(['sudo apt-get update -y'], shell=True, stdin=PIPE, stdout=PIPE)

while cam1.poll() is None:
    l = cam1.stdout.readline()
    print l
    if "Done" in l:
        cam2 = Popen(['sudo apt-get update -y'], shell=True, stdin=PIPE, stdout=PIPE)
        while cam2.poll() is None:
            q = cam2.stdout.readline()
            print q
        break
print("two time")
sleep(30)
print("closing")
cam1.stdin.write('stop\n')
cam1.stdin.close()
cam1.wait()
#while cam2.poll() is None:
#    r = cam2.stdout.readline()
#    print r

#print (cam1.stdout.readline())
#print (cam2.stdout.readline())

#print (cam2.stdout.readline())
#sleep(10)
#cam1.stdin.write('Yes\n')
#cam2.stdin.write('Yup\n')
