#!/usr/bin/python
# -*- coding: utf-8 -*-
import http.client 
from urllib.parse import urlencode
import template

################################################################################
#
#
#	Empty request test
#		Input			  : <nothing>
#		Action			  : Search vacancies with 256kb input
#		Expected response : 200(OK) and <empty list> of vacancies
#
#
################################################################################
class hh_vacancies_long_request_test(template.http_template):
		
	block_size = 100;

	def __init__(self, test_name, block_size = 100) :
		template.http_template.__init__(self, test_name, "api.hh.ru");
		self.block_size = block_size;

	def run(self):
		if self.connect() == False:
			return;

		parameters = urlencode(
			{
				"text" : "a" * self.block_size
			}
		);

		self.handle.putrequest("GET","/vacancies?"+parameters);
		self.handle.putheader("User-agent", self.userAgent);
		self.handle.endheaders();
		response = self.handle.getresponse();
		status = response.status;
		responseBody = response.read();
		self.handle.close();
		if response.status != http.client.OK and \
			response.status != http.client.REQUEST_URI_TOO_LONG :
			return self.fail("invalid response code " + str(response.status));

		return self.success();
