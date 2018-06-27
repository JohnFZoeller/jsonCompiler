from Token import Token
from HeteroAST import *
import sys


class SyntaxParser(object):
	def __init__(self, lexer):
		self.__lexer = lexer
		self.__token = self.__lexer.get_next_token()
		self.__root = HeteroAST(Token(Token.Token_Type.NULL))
		self.__curr_node = self.__root

	def parse(self):
		#while self.__token != None:
		while self.__token.value() != "endTest":
			if self.__token.type() == Token.Token_Type.COMMAND:
				pass
			elif (self.__token.type() == Token.Token_Type.OPERATOR
				and self.__token.value() == '{'):
				self.__Object()
			else:
				raise ValueError('Unexpected Token: ' + 
					self.__token.value())

	"""HELPERS"""
	def __match_operator(self, expect):
		print(self.__token)
		if self.__token.value() == expect:
			self.__set_token()
		else:
			raise ValueError('Expected a : ' + expect + ' Got: ' +
				self.__token)

	def __match(self, expect):
		value_node = self.__get_value_node(expect)
		self.__curr_node.add_child(value_node)

		#temp
		print(self.__token)
		sys.exit(1) if self.__token.value() == "endTest" else None
		#temp

		if self.__token.type() == expect:
			self.__set_token()
		else:
			raise ValueError('Expected a : ' + expect)

	def __set_token(self):
		self.__token = self.__lexer.get_next_token()
		pass

	def __get_value_node(self, type):
		if type == Token.Token_Type.INT:
			return IntNode(self.__token)
		elif type == Token.Token_Type.STRING:
			return StringNode(self.__token)
		elif type == Token.Token_Type.BOOL:
			return BoolNode(self.__token)
		else:
			return None

	"""TOKEN CHECKS"""
	def __has_members(self):
		return self.__token.value() != '}'
		pass

	def __has_more_members(self):
		return self.__token.value() == ','
		pass


	"""RULES"""
	def __Object(self):
		self.__match_operator('{')
		obj_node = ObjectNode()
		temp_node = self.__curr_node
		self.__curr_node = obj_node

		if self.__has_members():
			self.__Members()

		self.__curr_node = temp_node
		self.__curr_node.add_child(obj_node)
		self.__match_operator('}')

	def __Members(self):
		mems_node = MembersNode()
		temp_node = self.__curr_node
		self.__curr_node = mems_node

		self.__Pair() 

		while self.__has_more_members():
			self.__match_operator(',')
			self.__Members()

		self.__curr_node = temp_node
		self.__curr_node.add_child(mems_node)

	def __Pair(self):
		pair_node = PairNode()
		temp_mems_node = self.__curr_node
		self.__curr_node = pair_node

		self.__match(Token.Token_Type.STRING)
		self.__match_operator(':')

		value_type = self.__token.type()
		self.__match(value_type)

		self.__curr_node = temp_mems_node






