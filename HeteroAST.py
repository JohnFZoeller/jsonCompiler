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
		print(level + self.__class__.__name__ + ": CLASS")

		for c in self._children:
			if not c._token:
				c.print_tree(level + '++')
			else:
				print(level + str(c._token))

	def define_declarations(self, global_symbol_table):
		self._scope = global_symbol_table.global_scope
		[node._declare(self._scope) for node in self._children]

	def _declare(self, enclosing_scope):
		print("no implementation")
		pass

	def _has_one_child(self):
		return len(self._children) == 1

	def _has_children(self):
		return len(self._children) > 0
		pass

	def _has_two_children(self):
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

		if self._has_two_children():
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
			self._children[elems_node]._declare(self._scope, self._symbol)

		return self._symbol

class ElementsNode(HeteroAST):
	def __init__(self):
		super(ElementsNode, self).__init__()

	def _declare(self, enclosing_scope, array_symbol):
		self._scope = enclosing_scope
		value_node, elems_node = 0, 1

		elem = self._children[value_node]._declare(self._scope)
		array_symbol.append(elem)

		if self._has_two_children():
			self._children[elems_node]._declare(self._scope, array_symbol)

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
	"""A CommandNode has at most 2 children: a cmd_node(its name)
	and either an int node, another command (or nothing)"""

	def __init__(self, token):
		super(CommandNode, self).__init__(token)

	def _resolve_command(self, enclosing_scope):
		self._scope = enclosing_scope
		cmd_node_idx, child_node_idx = 0, 1
		cmd_name = self._children[cmd_node_idx]._token.value()

		if self._scope.contains_objects():
			self._scope = self._scope.peek_object()
			self._symbol = self._scope.resolve(cmd_name)

			if self._symbol:
				if self._has_one_child():
					self._print_value_symbol()
				else:
					child_node = self._children[child_node_idx]

					if self._is_int_node(child_node):
						int_symbol = child_node._declare(self._scope)
						self._print_array_element(self._symbol, int_symbol.name())
					else:
						child_node._resolve_command(self._scope)
			else:
				print("Failed to resolve: " + str(cmd_name))
		else:
			print("Scope Storage Error")

	def _declare(self, enclosing_scope):
		self._resolve_command(enclosing_scope)

	def _print_value_symbol(self):
		print("Result: " + str(self._symbol.value_symbol.name()))

	def _print_array_element(self, key_value_symbol, idx):
		print("Result: " + str(key_value_symbol.value_symbol.
			get_array_element(idx).name()))

	def _is_int_node(self, symbol):
		return symbol.__class__.__name__ == "IntNode"

	def temp(self):
		symbol_resolved = False

		for obj_scope in self._scope.objects:
			self._symbol = self._scope.resolve(cmd_name)

			if not self._symbol:
				continue
			else:
				symbol_resolved = True
				pass
				#rest of code
				pass

		if not symbol_resolved:
			print("Failed to resolve: " + str(cmd_name))





















