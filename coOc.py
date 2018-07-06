#!/usr/bin/env python3
from Token import Token
import sys, pprint

#co-occurrence window
K = 3

class Queue:
	def __init__(self, max_size):
		self.queue = list()
		self.max_size = max_size

	def __str__(self):
		return str(self.queue)

	def enqueue(self, token):
		self.queue.insert(0, token)
		return self

	def dequeue(self):
		return self.queue.pop()

	def peek(self):
		return self.queue[-1]

	def size(self):
		return len(self.queue)

	def isEmpty(self):
		return self.queue == []

	def enforce(self):
		if self.size() > self.max_size:
			self.dequeue()

class tokenData(object):
	def __init__(self, token = None):
		self.__count = 1
		self.__token = token
		self.__is_paired = false

def co_occurrence(desired_tokens, token_stream):
	word_count_map, co_oc_map = {}, {}

	build_maps(word_count_map, co_oc_map, token_stream)
	#pprint.pprint(word_count_map, width = 1)
	save_co_ocs(desired_tokens, word_count_map, co_oc_map)

def build_maps(word_count, co_oc_map, token_stream):
	token = token_stream.get_next_token()
	token_data_map = {}
	queue = Queue(K + 1)

	while not token.is_eof():
		word_count[token] = word_count.get(token, 0) + 1
		co_oc_map[token] = co_oc_map.get(token, dict())
		token_data_map[token] = token_data_map.get(token, set())

		queue.enqueue(token).enforce()
		parse_tokens_queue(queue, word_count, token_data_map)

		token = token_stream.get_next_token()

	print(token_data_map)

def parse_tokens_queue(q, w, t):
	

def save_co_ocs(desired_tokens, word_count, co_oc):
	pass
