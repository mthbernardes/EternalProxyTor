# -*- coding: utf-8 -*-
from TorCtl import TorCtl
import requests,json

proxies = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050'}

class TorProxy(object):

	def __init__(self,):
		pass

	def connect(self, url, method):
		r = getattr(requests, method)(url,proxies=proxies)
		return r

	def new_ip(self,):
		self.conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="RTFM_FODAO")
		self.conn.send_signal("NEWNYM")
		self.conn.close()

	def check_ip(self,):
		self.url = "http://ipinfo.io"
		self.r = requests.get(self.url,proxies=proxies)
		try:
			return json.loads(self.r.content)['ip']
		except:
			return 'Error to get your IP'

if __name__ == '__main__':
	tor = TorProxy()
	print tor.check_ip()
	print tor.new_ip()
	print tor.check_ip()
