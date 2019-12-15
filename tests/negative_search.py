#!/usr/bin/python
# -*- coding: utf-8 -*-
import http.client 
import template
from urllib.parse import urlencode
import json
import re

################################################################################
#
#
#	Empty request test
#		Input			  : Vacancy name
#		Action			  : Search vacancies with 'name' containing Input
#		Expected response : 200(OK) and 
#							Vacancy list, each has Input as a part of name
#
#
################################################################################
class hh_vacancies_negative_search_test(template.http_template):
	request_text = "";

	def __init__(self, test_name, request_text) :
		template.http_template.__init__(self, test_name, "api.hh.ru");
		self.request_text = request_text;

	def run(self):
		if self.connect() == False:
			return;

		parameters = urlencode(
			{
				"text" : self.request_text, 
				"search_field" : "name"
			}
		);

		self.handle.putrequest("GET","/vacancies?"+parameters);
		self.handle.putheader("User-agent", self.userAgent);
		self.handle.endheaders();
		response = self.handle.getresponse();
		status = response.status;
		responseBody = response.read();
		self.handle.close();
		if response.status != http.client.OK:
			return self.fail("invalid response code " + str(status));

		responseJson = json.loads(responseBody);
		count = len(responseJson["items"]);

		if count == 0:
			return self.success();

		return self.fail("Item number must be 0, {} items received".format(count));
