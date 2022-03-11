import os
from random import choice
from time import sleep
 
from urllib.request import urlopen
 
t="https://gist.githubusercontent.com/Skalbeard/e2e55bb3c614e0f6f6456bc5c0bcfdbd/raw/gistfile1.txt"
 
with urlopen(t) as webpage:
        content=webpage.read().decode()
 
with open('targets', 'w') as output:
        output.write(content)
 
 
file=open("targets","r")
chans=file.read().splitlines()
 
reason=["child_abuse","violence","spam","geoirrelevant","fake_account"]

while True:
        cmd="python reper.py -r 1 -t "+choice(chans)+ " -m " + choice(reason)
        print(cmd)
        os.system(cmd )
        sleep(0.5)