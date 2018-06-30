from Token import Token
from HeteroAST import *
from Scope import Scope
from Symbol import *
import sys

class SymbolTable(object):
	def __init__(self):
		self.global_scope = Scope("global")
		self.global_scope.build_global([ 
			BuiltInTypeSymbol("String"), 
			BuiltInTypeSymbol("Int"), 
			BuiltInTypeSymbol("Bool"), 
			BuiltInTypeSymbol("Null"),
			ArraySymbol("Array") 
		])
		self.global_scope.define(ObjectSymbol("Object",
			self.global_scope))

class SyntaxParser(object):
	def __init__(self, lexer):
		self.__lexer = lexer
		self.__token = self.__lexer.get_next_token()
		self.__root = HeteroAST(Token(Token.Token_Type.NULL))
		self.__curr_node = self.__root

	def parse(self):
		while not self.__token.is_eof():
			if self.__token.type() == Token.Token_Type.COMMAND:
				self.__Command()
			elif (self.__token.type() == Token.Token_Type.OPERATOR
				and self.__token.value() == '{'):
				self.__Object()
			else:
				raise ValueError('Unexpected Token: ' + 
					self.__token.value())

		self.__root.print('+')

	def decorate_AST(self):
		global_symbol_table = SymbolTable()
		self.__root.define_declarations(global_symbol_table)

	"""HELPERS"""
	def __match_operator(self, expect):
		if self.__token.value() == expect:
			self.__set_token()
		else:
			raise ValueError('Expected a : ' + expect + ' Got: ' +
				self.__token)

	def __match(self, expect):
		value_node = self.__get_value_node(expect)
		self.__curr_node.add_child(value_node)

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
		elif type == Token.Token_Type.NULL:
			return NullNode(self.__token)
		elif type == Token.Token_Type.COMMAND:
			return CommandNode(self.__token)
		else:
			return None

	"""TOKEN CHECKS"""
	def __has_members(self):
		return self.__token.value() != '}'
		pass

	def __has_elements(self):
		return self.__token.value() != ']'
		pass

	def __has_more_members(self):
		return self.__token.value() == ','
		pass

	def __is_basic_type(self, type):
		return (type != Token.Token_Type.OBJECT and
						type != Token.Token_Type.OPERATOR)

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
		operator = self.__token.value()

		if self.__is_basic_type(value_type):
			self.__match(value_type)
		else:
			self.__Object() if operator == '{' else self.__Array()

		self.__curr_node = temp_mems_node
		self.__curr_node.add_child(pair_node)

	def __Array(self):
		self.__match_operator('[')
		array_node = ArrayNode()
		temp_pair_node = self.__curr_node
		self.__curr_node = array_node

		if self.__has_elements():
			self.__Elements()

		self.__curr_node = temp_pair_node
		self.__curr_node.add_child(array_node)
		self.__match_operator(']')

	def __Elements(self):
		elems_node = ElementsNode()
		temp_node = self.__curr_node
		self.__curr_node = elems_node

		value_type = self.__token.type()
		operator = self.__token.value()

		if self.__is_basic_type(value_type):
			self.__match(value_type)
		else:
			self.__Object() if operator == '{' else self.__Array()

		while self.__has_more_members():
			self.__match_operator(',')
			self.__Elements()

		self.__curr_node = temp_node
		self.__curr_node.add_child(elems_node)

	def __Command(self):
		cmd_node = CommandNode(None)
		temp_node = self.__curr_node
		self.__curr_node = cmd_node

		self.__match(Token.Token_Type.COMMAND)

		if self.__token.value() == '.':
			self.__match_operator('.')
			self.__Command()

		self.__curr_node = temp_node
		self.__curr_node.add_child(cmd_node)









