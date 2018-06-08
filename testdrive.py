import os
from time import sleep

#update system
os.system("sudo apt-get update -y")

#upgrade requires human interaction
#os.system('sudo apt-get upgrade -y')
#os.system('sudo apt-get dist-upgrade -y)

#copy a backup of keyboard
os.system("sudo cp /etc/default/keyboard /etc/default/keyboardbackup")

#edit in place the international keyboard setting.  By default, gb
#changing to us with the sed command
#will require a reboot in order to implement the changes
os.system("sudo sed -i -e 's/gb/us/' /etc/default/keyboard")

#install espeak to tell you the steps
os.system("sudo apt-get install espeak -y")

#receive greeting message from scripted robot
os.system("sudo espeak \"hello from your robot friend\"")
sleep(0.1)

#robot says it will install imagemagick
os.system("sudo espeak \"I will download a command line software called image magic\"")

#install imagemagick
os.system("sudo apt-get install imagemagick -y")

#imagemagick draw a rectangle on a series of jpg's
os.system("convert -size 800x800 xc:skyblue -fill white -stroke black -draw \"rectangle 20,10 80,50\" draw01.jpg")
os.system("convert -size 800x800 xc:skyblue -fill white -stroke black -draw \"rectangle 30,20 90,60\" draw02.jpg")
os.system("convert -size 800x800 xc:skyblue -fill white -stroke black -draw \"rectangle 40,30 100,70\" draw03.jpg")
os.system("convert -size 800x800 xc:skyblue -fill white -stroke black -draw \"rectangle 50,40 110,80\" draw04.jpg")

#install libav-tools to convert/merge the image sequence into an mp4 file
os.system("sudo apt-get -y install libav-tools -y")

#convert image sequence into an mp4
os.system("avconv -r 10 -i draw0%d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4 -y")

#download a video player for the mp4 file
os.system("sudo apt-get install mplayer -y")

#robot introduces playing a video file
os.system("sudo espeak \"I I put together a video demonstrating the conversion of an image sequence to a video file\"")

#play video
os.system("sudo mplayer timelapse.mp4")

#install sox
os.system("sudo apt-get install sox -y")

#install xdotool for keyboard and mouse emulation
#os.system("sudo apt-get install xdotool -y")

#reboot system
#os.system("sudo reboot")

#remove old dependencies
os.system("sudo apt-get autoremove -y")

#install terminal youtube downloader
os.system("sudo apt-get install youtube-dl -y")

#download nes walkthrough
os.system("youtube-dl -f 18 https://www.youtube.com/watch?v=RvYPsa1Pbrs")

#trim the first 10 seconds of the video
os.system("sudo avconv -i Clash\ At\ Demonhead\ NES\ 1_9\!\!\!-RvYPsa1Pbrs.mp4 -ss 0.0 -t 10.0 -codec copy intro.mp4")

#play the video
os.system("sudo mplayer intro.mp4")

#extract audio from video
os.system("avconv -i intro.mp4 -vn -acodec copy audio.aac")

#convert aac audio file to mp4
os.system("sudo avconv -i audio.aac audio2.wav")

#play audio file
os.system("sudo mplayer audio2.wav")

#robot announces that it is going to record you
os.system("sudo espeak \"I I am going to record audio for 10 seconds\"")

#record audio for ten seconds
os.system("sudo rec -c 2 test.aiff trim 0 10")

#play result
os.system("play test.aiff")

#install openscad
os.system("sudo apt-get install openscad -y")

#copy example 001 into the home directory and name it differently
os.system("sudo cp /usr/share/openscad/examples/example024.scad hollowsphere.scad")

#openscad create 2d image from scad file
os.system("sudo openscad -o hollowsphere.png hollowsphere.scad  --camera=0,0,0,60,0,35,500 --projection=p --imgsize=800,800")

