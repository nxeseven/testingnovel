sudo apt update -y
sudo apt-get install git -y
git config --global user.name "nxeseven"
git config --global user.email "nxe7llc@gmail.com"
mkdir Mytest
git init Mytest/
cd Mytest/
nano hello.txt
git add hello.txt 
git commit -m "first try"
git remote add origin https://github.com/nxeseven/testingbook.git
git push origin master
git pull origin master
ls
git push origin master
git status
git remote add origin https://github.com/nxeseven/testingworld.git
cd
mkdir Myworld
git init Myworld
cd Myworld/
nano world.txt
git commit -m "first commit"
git add world.txt
git commit -m "first commit"
git remote add origin https://github.com/nxeseven/testingnovel.git
git push -u origin master
cd
ls -a
