#!/usr/bin/python
# -*- coding: utf-8 -*-
from http.client import *
################################################################################
#
#
#	Test template class
#
#
################################################################################
class http_template:
	name = "none";
	handle = "none";
	userAgent = "textTester/1.0";

	def __init__(self, name, host):
		self.handle = HTTPSConnection(host, timeout = 3);
		self.name =  name;

	def success(self):
		print("   {:<30s} : SUCCESS".format(self.name));
		return True;

	def fail(self, reason=""):
		print(" ! {:<30s} : FAIL".format(self.name), end="");
		if reason != "":
			print(" (" + reason +")", end="");
		print();
		return False;

	def connect(self):
		try:
			self.handle.connect();
		except :
			return self.fail("connection error");
