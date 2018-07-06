#!/usr/bin/env python3
from Token import Token
import sys, pprint

K, MaxWindow = 3, 4

class Queue:
	def __init__(self):
		self.queue = list()

	def enqueue(self, token):
		self.queue.insert(0, token)

	def dequeue(self):
		return self.queue.pop()

	def peek(self):
		return self.queue[-1]

	def size(self):
		return len(self.queue)

	def isEmpty(self):
		return self.queue == []

class tokenData(object):
	def __init__(self, token = None):
		self.__count = 1
		self.__token = token
		self.__is_paired = false

def build_maps(word_count, co_oc, token_stream):
	token = token_stream.get_next_token()
	token_data_map = {}
	queue = Queue()
	print("called")
	while not token.is_eof():
		word_count[token] = word_count.get(token, 0) + 1


		token = token_stream.get_next_token()


def co_occurrence(desired_tokens, token_stream):
	word_count_map, co_oc_map = {}, {}

	build_maps(word_count_map, co_oc_map, token_stream)
	#pprint.pprint(word_count_map, width = 1)

	print(sys.argv)



