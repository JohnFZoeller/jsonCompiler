from Token import Token
from Scope import Scope

"""Normalized Heterogeneous Abstract Syntax Tree Node"""
class HeteroAST(object):
	def __init__(self, token = None):
		self._children = list()
		self._token = token.copy() if token != None else None
		self._scope = None

	def add_child(self, tree_node):
		self._children.append(tree_node)
		pass

	def print(self, level):
		print(level + self.__class__.__name__)

		for c in self._children:
			if c._token == None:
				c.print(level + '++')
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

	def _has_two_children(self):
		return len(self._children) == 2
		pass

class ObjectNode(HeteroAST):
	def __init__(self):
		super(ObjectNode, self).__init__()

	def _declare(self, enclosing_scope):
		self._scope = Scope("Object Scope", enclosing_scope)
		mems_node = 0;

		if self._has_children():
			self._children[mems_node]._declare(self._scope)

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
		string_node, value_node = 0, 1
		self._children[string_node]._declare(self._scope)
		self._children[value_node]._declare(self._scope)

class ArrayNode(HeteroAST):
	def __init__(self):
		super(ArrayNode, self).__init__()

class ElementsNode(HeteroAST):
	def __init__(self):
		super(ElementsNode, self).__init__()


class ValueNode(HeteroAST):
	def __init__(self, token):
		super(ValueNode, self).__init__(token)

	def _declare(self, enclosing_scope):
		pass

class StringNode(ValueNode):
	def __init__(self, token):
		super(StringNode, self).__init__(token)

	def _declare(self, enclosing_scope):
		self._scope = enclosing_scope
		symbol_name = self._token.value()
		print(symbol_name)
		symbol = self._scope.resolve(symbol_name)
		print("left off")


		

class IntNode(ValueNode):
	def __init__(self, token):
		super(IntNode, self).__init__(token)

class BoolNode(ValueNode):
	def __init__(self, token):
		super(BoolNode, self).__init__(token)

class NullNode(ValueNode):
	def __init__(self, token):
		super(NullNode, self).__init__(token)


class CommandNode(ValueNode):
	def __init__(self, token):
		super(CommandNode, self).__init__(token)





