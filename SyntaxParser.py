from Token import Token
from HeteroAST import *


class SyntaxParser(object):
	def __init__(self, lexer):
		self.__lexer = lexer
		self.__token = self.__lexer.get_next_token()
		self.__root = HeteroAST(self.__lexer)

	def parse(self):
		while self.__token != None:
			print(self.__token)

			if self.__token.type() == Token.Token_Type.COMMAND:
				pass
			elif (self.__token.type() == Token.Token_Type.OPERATOR
			and self.__token.value() == '{'):
				self.__root.add_child(ObjectNode(self.__lexer,
																				 self.__token))
			else:
				raise ValueError('Unexpected Token: ' + 
					self.__token.value())

			self.__set_token()

	def __match_operator(self, expect):
		if self.__token.value() == expect:
			self.__set_token()
		else:
			raise ValueError('Expected a : ' + expect + ' Got: ' +
				self.__token)

	def __set_token(self):
		self.__token = self.__lexer.get_next_token()
		pass
