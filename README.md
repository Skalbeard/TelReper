***Noone is going to track you. This is a legal developer feature that we are using through the Telegram public API***
***AND YES. You get added to the channel that you are reporting. But you are an observer, can't post there or get associated with it in any way.***

instructions

* clone or download zipped project from https://github.com/Skalbeard/TelReper
* Download and Install python3 from python.org if you dont have it
* Download and install powershell (optional)
* if you have powershell, shift and left click in the directory you cloned the project to
* OR open CMD and change directory to that folder
* if you dont have pip installed get it with running
python get-pip.py
* run    	pip install -r requirements.txt
* run   	python reper.py
* if you dont have Telegram, download it on your phone and register (fast and easy)
* when you have telegram, go to: https://my.telegram.org/auth
* enter your number. this will authorize you as a TG developer to access the API
* click on API development tools
* create your app. put any random numbers into the id and title. set to desktop.
* this will give you API ID and hashID
* keep this next page that will open open
* run  python reper.py -an "YOUR TELEGRAM PHONE NUMBER"
* run  python reper.py -r 1000 -t yurasumy -m child_abuse
* make some tea or coffee
* run python reper.py -r 1000 -t dnepr_partizani -m child_abuse
* at this point the last command can be repeated. we are looking for more channels. The parameter that is 1000 is the times that we report the channel. the name of the channel is after -t and the last part of the command is the criteria by which we report it.
Every report has a message coded into it which reads: "This channel is a Russian propoganda channel, spreading misinformation AND TACTICAL POSITION OF UKRAINIAN FORCES to the Russian military."

The last parameter (the criteria) can also be changed to 'violence', so you can replace 'child_abuse'

CHANNEL LIST
yurasumy
dnepr_partizani
ZeRada1
rezident_ua
spletnicca
ZE_kartel
legitimniy



# TelReper
A tool for reporting telegram channel automatically
<h1>Usage</h1>
<ul>
  <li>
    <h3>Termux (Android):</h3>
    <ul>
    <li><code>apt update</code></li>
    <li><code>apt upgrade</code></li>
    <li><code>pkg install python3 python3-pip git -y</code></li>
    <li><code>git clone https://github.com/e811-py/TelReper</code></li>
    <li><code>cd TelReper</code></li>
    <li><code>pip3 install -r requeirments.txt</code></li>
    <li><code>python3 reper.py</code></li>
    </ul>
  </li>
  <li>
    <h3>Linux:</h3>
    <ul>
    <li><code>sudo apt update</code></li>
    <li><code>sudo apt upgrade</code></li>
    <li><code>sudo apt install python3 python3-pip git -y</code></li>
    <li><code>git clone https://github.com/e811-py/TelReper</code></li>
    <li><code>cd TelReper</code></li>
    <li><code>sudo pip3 install -r requeirments.txt</code></li>
    <li><code>python3 reper.py</code></li>
    </ul>
  </li>
  <li>
    <h3>Windows</h3>
    <ul>
    <li>Install python3 from python.org</li>
    <li>Download source code from https://github.com/e811-py/TelReper</li>
    <li>change directory to source code directory</li>
    <li><code>pip install -r requierments.txt</code></li>
    <li><code>python reper.py</code></li>
    </ul>
  </li>
</ul>

