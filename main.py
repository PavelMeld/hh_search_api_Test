#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

sys.path.append('./tests');

import	empty_request
import	long_request
import	simple_request
import	negative_search
import	syntax_request
from	http.client import *



tests = [
	empty_request.hh_vacancies_empty_request_test("Connection test"),
	simple_request.hh_vacancies_simple_request_test("Cyrillic request test", "Программист"),
	simple_request.hh_vacancies_simple_request_test("Latin request test", "Programmer"),
	long_request.hh_vacancies_long_request_test("100-byte request test", 100),
	long_request.hh_vacancies_long_request_test("31k-byte request test", 31*1024),
	long_request.hh_vacancies_long_request_test("32k-byte request test", 32*1024),
	long_request.hh_vacancies_long_request_test("50k-byte request test", 50*1024),
	long_request.hh_vacancies_long_request_test("100k-byte request test", 100*1024),
	negative_search.hh_vacancies_negative_search_test("Negative search", "flkfjwelfkjwflwk"),
	syntax_request.hh_vacancies_syntax_test("Syntax test", "Менедж*", "Менеджер"),
	syntax_request.hh_vacancies_syntax_test("Injection test", "Programmer'", "Program")
];

for test in tests:
	test.run();
