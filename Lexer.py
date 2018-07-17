"""Lexer.py: Simple charaters-to-JSON-tokens Lexer. 

Tokenizes any file argument.

Version 1: All properties added. Clean Algo's
		   Needs Custom Errors
"""

__author__ = 'Author: John Zoeller, Don Cheadle (Yes, that Don Cheadle)'
__copyright__ = 'Copyright 2018 DaaaBulls'

from Token import Token

class Lexer(object):
	#public static
	ops = {'{', '}', ':', ',', '.','[', ']'}

	#non-static inside __init__
	def __init__(self, file_name):
		self.__file = open(file_name)
		self.__curr_char = ''
		self.__file_readable = True

	@property
	def curr_char(self):
		return self.__curr_char

	@curr_char.setter
	def curr_char(self, value):
		self.__curr_char = value

	@property
	def file_readable(self):
		return self.__file_readable

	@file_readable.setter
	def file_readable(self, value):
		self.__file_readable = value
	
	"""Calls rest of methods to return a token 
		Reads until EOFError is caught"""
	def get_next_token(self):
		try:
			if self.file_readable:
				self.__set_curr_char()
			self.__eat_whitespace()
		except EOFError:
			return Token(Token.Token_Type.EOF, 'x')

		self.file_readable = True

		if self.curr_char in self.ops:
			return Token(Token.Token_Type.OPERATOR, 
				self.curr_char)
		elif self.curr_char == '"':
			return self.__string()
		elif self.__curr_char.isalnum():
			return self.__word()
		else:
			return None

	"""Grammar Rules"""

	def __string(self):
		value = ""
		self.__match('"')

		while self.curr_char != '"':
			value += self.curr_char
			self.__set_curr_char()
		#intentionally not match end quote
		return Token(Token.Token_Type.STRING, value) 

	def __word(self):
		value = u""
		self.file_readable = False

		while self.curr_char.isalnum():
			value += self.curr_char
			self.__set_curr_char()

		if value == "null":
			return Token(Token.Token_Type.NULL, value)
		elif value == "true" or value == "false":
			return Token(Token.Token_Type.BOOL, value)
		elif value.isnumeric():
			return Token(Token.Token_Type.INT, value)
		else:
			return Token(Token.Token_Type.COMMAND, value)

	""""Character Manipulators"""

	def __match(self, expect):
		if expect == self.curr_char:
			self.__set_curr_char()
		else:
			raise ValueError('Expected : ' + expect +
				'got : ' + self.curr_char)

	def __set_curr_char(self):
		self.curr_char = self.__file.read(1)
		if self.curr_char == '':
			raise EOFError('End of input reached unexpectedly')

	"""Utilities"""

	def __is_escape(self, c):
		return c == '\t' or c == ' ' or c == '\n' or c == '\r'

	def __eat_whitespace(self):
		while self.__is_escape(self.curr_char):
			self.__set_curr_char()




