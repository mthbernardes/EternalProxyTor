# EternalProxyTor
Use tor as proxy to bypass IP limit querys

#Dependencies
<pre>
pip install requests
pip install git+https://github.com/aaronsw/pytorctl.git
apt-get install tor privoxy
</pre>

#Install and configure TOR
<pre>
<b>Restart tor</b>
/etc/init.d/tor restart

<b>Enable Cotrole port</b>
Edit the file /etc/tor/torrc and remove the # from,
ControlPort 9051

<b>Restart tor</b>
/etc/init.d/tor restart

<b>Privoxy</b>
Make privoxy use tor, edit the file /etc/privoxy/config and remove the # from,
forward-socks5 / localhost:9050 .

<b>Restart Privoxy</b>
/etc/init.d/privoxy restart
</pre>

#Usage
<pre>
#import lib
>>>from ept import ProxyTor

#Create object from ProxyTor
>>>tor = ProxyTor()

#Check your current IP
>>>tor.check_ip()
89.187.144.122

#Get new IP from a specific country
>>>tor.signal(country='NL')

>>>tor.check_ip()
77.247.181.163

#Connect to a website using tor, this function is based on lib requests.
>>>r = tor.connect('https://google.com',method='post')
>>>r.status_code
200
</pre>
