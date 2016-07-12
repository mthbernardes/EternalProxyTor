# EternalProxyTor
Use tor as proxy to bypass IP limit querys

#Dependencies
<pre>
pip install requests
pip install git+https://github.com/aaronsw/pytorctl.git
apt-get install tor privoxy
</pre>

#Install and configure TOR
http://sacharya.com/crawling-anonymously-with-tor-in-python/

#Usage
<pre>
>>>from ept import ProxyTor
>>>tor.check_ip()
89.187.144.122
>>>tor.signal()
>>>tor.check_ip()
77.247.181.163
>>>tor.connect('https://google.com','post')
</pre>
