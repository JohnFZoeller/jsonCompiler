from Token import Token
from Scope import Scope
from Symbol import *

"""Normalized Heterogeneous Abstract Syntax Tree Node"""
class HeteroAST(object):
	def __init__(self, token = None):
		self._children = list()
		self._token = token.copy() if token else None
		self._scope = None
		self._symbol = None

	def add_child(self, tree_node):
		self._children.append(tree_node)
		pass

	def print_tree(self, level):
		#print(level + self.__class__.__name__)

		for c in self._children:
			if c._token == None:
				c.print_tree(level + '++')
			else:
				print(level + str(c._token))

	def define_declarations(self, global_symbol_table):
		self._scope = global_symbol_table.global_scope
		[node._declare(self._scope) for node in self._children]

	def _declare(self, enclosing_scope):
		print("no implementation")
		pass

	def _has_children(self):
		return len(self._children) > 0
		pass

	def _has_more_children(self):
		return len(self._children) == 2
		pass

class ObjectNode(HeteroAST):
	def __init__(self):
		super(ObjectNode, self).__init__()

	def _declare(self, enclosing_scope):
		mems_node = 0;
		self._symbol = self._scope = ObjectSymbol(enclosing_scope)

		if self._has_children():
			self._children[mems_node]._declare(self._scope)

		enclosing_scope.define(self._symbol)

class MembersNode(HeteroAST):
	def __init__(self):
		super(MembersNode, self).__init__()

	def _declare(self, enclosing_scope):
		self._scope = enclosing_scope
		pair_node, mems_node = 0, 1

		self._children[pair_node]._declare(self._scope)

		if self._has_more_children():
			self._children[mems_node]._declare(self._scope)

class PairNode(HeteroAST):
	def __init__(self):
		super(PairNode, self).__init__()

	def _declare(self, enclosing_scope):
		self._scope = enclosing_scope

		key_node, val_node = 0, 1


		key_symbol = self._children[key_node]._declare(self._scope, True)
		val_symbol = self._children[val_node]._declare(self._scope)
		key_name, key_type = key_symbol.name(), key_symbol.type()

		# print("SCOPE: " + str(self._scope.scope_name()))
		# print('\t' + str(key_symbol) + '\n\t' + str(val_symbol))

		self._symbol = KeyValueSymbol(key_name, key_type, val_symbol)
		self._scope.define(self._symbol)

class ArrayNode(HeteroAST):
	def __init__(self):
		super(ArrayNode, self).__init__()

	def _declare(self, enclosing_scope):
		self._scope = enclosing_scope
		self._symbol = ArraySymbol()
		elems_node = 0

		if self._has_children():
			self._children[elems_node]._declare(self._scope,
																					self._symbol)

		return self._symbol

class ElementsNode(HeteroAST):
	def __init__(self):
		super(ElementsNode, self).__init__()

	def _declare(self, enclosing_scope, array_symbol):
		self._scope = enclosing_scope
		value_node, elems_node = 0, 1

		elem = self._children[value_node]._declare(self._scope)
		array_symbol.append(elem)

		if self._has_more_children():
			self._children[elems_node]._declare(self._scope,
																					array_symbol)


class ValueNode(HeteroAST):
	def __init__(self, token):
		super(ValueNode, self).__init__(token)

class BuiltInTypeNode(ValueNode):
	def __init__(self, token):
		super(BuiltInTypeNode, self).__init__(token)

	def _declare(self, enclosing_scope):
		self._scope = enclosing_scope
		value = self._token.value()
		type = self._scope.resolve(self._token.type().name)
		self._symbol = Symbol(value, type)
		return self._symbol

class StringNode(BuiltInTypeNode):
	def __init__(self, token):
		super(StringNode, self).__init__(token)

	def _declare(self, enclosing_scope, is_key = False):
		self._scope = enclosing_scope
		token_name = self._token.value()
		token_type = self._token.type().name
		symbol_type = self._scope.resolve(token_type)

		if is_key:
			self._symbol = self._scope.resolve(token_name)

			if self._symbol != None:
				raise ValueError('Symbol Already Defined')

		self._symbol = Symbol(token_name, symbol_type)

		return self._symbol

class IntNode(BuiltInTypeNode):
	def __init__(self, token):
		super(IntNode, self).__init__(token)

class BoolNode(BuiltInTypeNode):
	def __init__(self, token):
		super(BoolNode, self).__init__(token)

class NullNode(BuiltInTypeNode):
	def __init__(self, token):
		super(NullNode, self).__init__(token)


class CommandNode(ValueNode):
	def __init__(self, token):
		super(CommandNode, self).__init__(token)

	def _resolve_command(self, enclosing_scope):
		#print("resolve command  called")
		self._scope = enclosing_scope
		cmd_node = 0
		cmd_name = self._children[cmd_node]._token.value()


		if self._scope.contains_objects():
			self._scope = self._scope.peek_object()
			self._symbol = self._scope.resolve(cmd_name)

			if self._symbol:

				
				for i in range(1, len(self._children)):
					child_symbol = self._children[i]._declare(self._scope)

					#if is array symbol
					if not self._is_command_symbol(child_symbol):
						self.__print_array_element(self._symbol, child_symbol.name())


				#if theres only one child, the for loop never executes
				if self._is_value_symbol(self._symbol):
					print("Result: " + str(self._symbol.get_value_symbol().name()))
					return self._symbol
					#return self._symbol
			else:
				print("Failed to resolve: " + str(cmd_name))
		else:
			print("Scope Storage Error")

	def _declare(self, enclosing_scope):
		self._resolve_command(enclosing_scope)
		# self._scope = enclosing_scope
		# cmd_node = 0
		# cmd_name = self._children[cmd_node]._token.value()


		# if self._scope.contains_objects():
		# 	self._scope = self._scope.peek_object()
		# 	self._symbol = self._scope.resolve(cmd_name)

		# 	if self._symbol:
		# 		#skips cmd_node, check if symbol 
		# 		for i in range(1, len(self._children)):
		# 			idx_symbol = self._children[i]._declare(self._scope)

		# 			if idx_symbol:
		# 				self.__print_array_element(self._symbol, idx_symbol.name())

		# 		if len(self._children) == 1:
		# 			print("Result: " + str(self._symbol.get().name()))
		# 			return
		# 	else:
		# 		print("Failed to resolve: " + str(cmd_name))
		# else:
		# 	print("Scope Storage Error")


	def __print_array_element(self, key_value_symbol, idx):
		print("Result: " + str(key_value_symbol.get_value_symbol().
					get_array_element(idx).name()))

	def _is_command_symbol(self, symbol):
		if symbol:
			if (symbol.type().__class__.__name__ == "BuiltInTypeSymbol"):
				return False
			return True
		return True

	def _is_value_symbol(self, symbol):
		return len(self._children) == 1
		#need to implement check for whether the symbol is 
		#actually a value symbol of a keyValuesymbol
		#this is a cheat

	def temp(self):
		for obj in self._scope.objects:
			temp_scope = obj
			self._symbol = temp_scope.resolve(cmd_name)






















