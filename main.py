'''
Hey boi I'm Ashrafi Abir :")

Author : Dark Hunter 141

If u want to copy this tools , I have no problem  . But follow our page and github :")

'''

import os
os.system("rm -rf cloudflare")

#clear 

os.system("clear")

#install nes pkgs

os.system("apt install wget php -y") 

# for termux 

os.system("pkg install proot -y")
os.system("pkg install proot resolv-conf -y")

#create folder

os.system("mkdir cloudflare")

#getsysteminfo 

sysInfo = os.popen("uname -m")
sysData = sysInfo.read().replace("\n","")

# Download cloudflare


if sysData=="aarch64" or sysData =="Android":
     os.system("cd cloudflare && wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm")
elif sysData=="arm64":
     os.system("cd cloudflare && wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64")
elif sysData =="x86_64":
     os.system("cd cloudflare && wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64")
else :
     os.system("cd cloudflare && wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386")
     
#permisson

os.system("cd cloudflare && chmod +x *")

# get file name

getFileby = os.popen("ls cloudflare")
getFilename = getFileby.read().replace("\n","")

# change filename & setup cloudflare  pkg

os.system(f"cd cloudflare && mv {getFilename} cldf")
os.system("cd cloudflare && cp cldf $PREFIX/bin/")
os.system("chmod +X $PREFIX/bin/cldf")
os.system("rm -rf cloudflare")

# done

os.system("clear")
print (" [*] Setup Done :)")
print (" Run :: cldf --help ")
