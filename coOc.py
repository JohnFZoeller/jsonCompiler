#!/usr/bin/env python3
from Token import Token
import sys, pprint
#ALL CONSTS SHOULD BE ALL CAPS WITH UNDERSCORES

#co-occurrence window
K = 3


class Queue:
	"""
	Maximum Size Queue class built with a list. Built 
	backwards. The END of the list is the FIRST in line for the 
	queue. The begging of the list is the back of the queue.  
	Therefore, to peek, look at the last list element. 
	To pop, look at the last element.
	To insert, emplace into the first elemnt
	"""
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

class TokenData(object):
	def __init__(self, token = None):
		self.__count = 1
		self.__token = token
		self.__is_paired = false

def co_occurrence(desired_tokens, token_stream):
	map_word_count, map_co_oc = {}, {}

	build_maps(map_word_count, map_co_oc, token_stream)
	save_co_ocs(desired_tokens, map_word_count, map_co_oc)

def build_maps(map_word_count, map_co_oc, token_stream):
	token = token_stream.get_next_token()
	queue = Queue(K + 1)

	while not token.is_eof():
		map_word_count[token] = map_word_count.get(token, 0) + 1
		map_co_oc[token] = map_co_oc.get(token, dict())					#get(value, default)

		parse_tokens_queue(token, queue, map_word_count, map_co_oc)
		queue.enqueue(token).enforce()
		token = token_stream.get_next_token()

def parse_tokens_queue(token, q, map_word_count, map_co_oc):

	for token_iter in q.queue: 
		current_token_count = iter_token_count = 0

		if token in map_co_oc[token_iter]:
			current_token_count = map_co_oc[token_iter][token]

		if token_iter in map_co_oc[token]:
			iter_token_count = map_co_oc[token][token_iter]
			
		if map_word_count[token_iter] > map_word_count[token]:
			map_co_oc[token_iter][token] = current_token_count + 1
			map_co_oc[token][token_iter] = iter_token_count + 1

def save_co_ocs(desired_tokens, map_word_count, map_co_oc):
	token_left = desired_tokens.get_next_token()
	token_right = desired_tokens.get_next_token()
	count_numerator = count_denominator = 0

	while not token_right.is_eof():
		count_denominator = map_word_count[token_left]
		count_numerator = map_co_oc[token_left][token_right]

		print(str(token_left) + '\n' + str(token_right) + '\t' +
			str(count_numerator / count_denominator) + '\n')

		token_left = desired_tokens.get_next_token()
		token_right = desired_tokens.get_next_token()
















