#!/usr/bin/python
# -*- coding: utf-8 -*-
import http.client 
import template
################################################################################
#
#
#	Empty request test
#		Expected response : a) Without User-agent : BAD_REQUEST(400)
#							b) With User-agend : OK (200) and some data
#
#
################################################################################
class hh_vacancies_empty_request_test(template.http_template):
	def __init__(self, test_name) :
		template.http_template.__init__(self, test_name, "api.hh.ru");

	def run(self):
		if self.connect() == False:
			return;

		self.handle.putrequest("GET","/vacancies");
		self.handle.endheaders();
		response  = self.handle.getresponse();
		self.handle.close();
		if response.status != http.client.BAD_REQUEST:
			return self.fail("invalid response code " + str(response.status));

		self.handle.putrequest("GET","/vacancies");
		self.handle.putheader("User-agent", self.userAgent);
		self.handle.endheaders();
		response  = self.handle.getresponse();
		json = response.read();
		self.handle.close();
		if response.status != http.client.OK:
			return self.fail("invalid response code " + str(response.status) + " : " + json);

		return self.success();
		
