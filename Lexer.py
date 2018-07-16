from Token import Token

class Lexer(object):
	#public static
	ops = {'{', '}', ':', ',', '.','[', ']'}

	#non-static inside __init__
	def __init__(self, file_name):
		self.__file = open(file_name)
		self.__curr_char = ''
		self.__file_readable = True

	def get_next_token(self):
		try:
			if self.__file_readable:
				self.__set_curr_char()
			self.__eat_whitespace()
		except EOFError:
			return Token(Token.Token_Type.EOF, 'x')

		self.__file_readable = True

		if self.__curr_char in self.ops:
			return Token(Token.Token_Type.OPERATOR, 
				self.__curr_char)
		elif self.__curr_char == '"':
			return self.__string()
		elif self.__curr_char.isalnum():
			return self.__word()
		else:
			return None

	def __string(self):
		value = ""
		self.__match('"')

		while self.__curr_char != '"':
			value += self.__curr_char
			self.__set_curr_char()
		#intentionally not match end quote
		return Token(Token.Token_Type.STRING, value) 

	def __word(self):
		value = u""
		self.__file_readable = False

		while self.__curr_char.isalnum():
			value += self.__curr_char
			self.__set_curr_char()

		if value == "null":
			return Token(Token.Token_Type.NULL, value)
		elif value == "true" or value == "false":
			return Token(Token.Token_Type.BOOL, value)
		elif value.isnumeric():
			return Token(Token.Token_Type.INT, value)
		else:
			return Token(Token.Token_Type.COMMAND, value)

	def __match(self, expect):
		if expect == self.__curr_char:
			self.__set_curr_char()
		else:
			raise ValueError('Expected : ' + expect +
				'got : ' + self.__curr_char)

	def __set_curr_char(self):
		self.__curr_char = self.__file.read(1)
		if self.__curr_char == '':
			raise EOFError('End of input reached unexpectedly')

	def __is_escape(self, c):
		return c == '\t' or c == ' ' or c == '\n' or c == '\r'

	def __eat_whitespace(self):
		while self.__is_escape(self.__curr_char):
			self.__set_curr_char()




