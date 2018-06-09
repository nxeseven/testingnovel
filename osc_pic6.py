from subprocess import * 
import uinput 
import time 

device = uinput.Device([
        uinput.KEY_DOWN
        ])

cam1 = Popen(['node osc-examples/print.js'], shell=True, stdin=PIPE, stdout=PIPE) 
print("starting")

while cam1.poll() is None: 
    l = cam1.stdout.readline()
    print(l)
    if "push4" in str(l):
        cam2 = Popen(['espeak "one"'], shell=True, stdin=PIPE, stdout=PIPE)
        #cam2 = Popen(['play -n synth 4 pluck C3'], shell=True, stdin=PIPE, stdout=PIPE)
        #cam2 = Popen(['sudo DISPLAY=:0 fbi -T 1 MM2FlashMan.jpg'], shell=True, stdin=PIPE, stdout=PIPE)        
    if "push2" in str(l):
        
        #cam3 = Popen(['sudo DISPLAY=:0 fbi -T 1 MM2WoodMan.jpg'], shell=True, stdin=PIPE, stdout=PIPE)
        #cam3 = Popen(['play -n synth 4 pluck D3'], shell=True, stdin=PIPE, stdout=PIPE)
    if "down" in str(l):
        time.sleep(0.5) 
        device.emit_click(uinput.KEY_DOWN)
    if "clear" in str(l):
        cam4 = Popen(['espeak "clear"'], shell=True, stdin=PIPE, stdout=PIPE)
        #cam4 = Popen([''], shell=True, stdin=PIPE, stdout=PIPE)
    
