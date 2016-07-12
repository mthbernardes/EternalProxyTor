# -*- coding: utf-8 -*-
from TorCtl import TorCtl
import requests,json,os,re

proxies = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050'}

class TorProxy(object):
	def __init__(self,):
		pass

	def connect(self, url, method,data=None,headers=None,cookies=None,auth=None,params=None,json=None,files=None,timeout=None):
		r = getattr(requests, method)(url,proxies=proxies,data=data,headers=headers,cookies=cookies,auth=auth,params=params,json=json,files=files,timeout=timeout)
		return r

	def signal(self,cmd="NEWNYM",country=None):
		self.conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051)
		self.conn.send_signal('HUP')
		if country:
			country = '{%s}' %country.upper()
		self.conn.set_option("ExitNodes", country)
		self.conn.send_signal(cmd)
		self.conn.close()

	def check_ip(self,):
		self.url = "http://myexternalip.com/json"
		self.r = requests.get(self.url,proxies=proxies)
		try:
			return json.loads(self.r.content)['ip']
		except:
			return 'Error to get your IP'

if __name__ == '__main__':
	tor = TorProxy()
	print tor.check_ip()
	tor.signal(country='Br')
	r = tor.connection('http://google.com',method='get')
	print r.status_code
	print tor.check_ip()
