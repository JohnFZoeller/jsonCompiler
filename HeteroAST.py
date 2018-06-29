from Token import Token
from Scope import Scope

"""Normalized Heterogeneous Abstract Syntax Tree Node"""
class HeteroAST(object):
	def __init__(self, token = None):
		self._children = list()
		self._token = token.copy() if token != None else None
		self._node_scope = None

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
		self._node_scope = global_symbol_table.global_scope
		
		[child.declare() for child in self._children]

	def declare(self):
		print("no implementation")

class ObjectNode(HeteroAST):
	def __init__(self):
		super(ObjectNode, self).__init__()

	def declare(self):
		print("obj") 

class MembersNode(HeteroAST):
	def __init__(self):
		super(MembersNode, self).__init__()

class PairNode(HeteroAST):
	def __init__(self):
		super(PairNode, self).__init__()


class ArrayNode(HeteroAST):
	def __init__(self):
		super(ArrayNode, self).__init__()

class ElementsNode(HeteroAST):
	def __init__(self):
		super(ElementsNode, self).__init__()


class ValueNode(HeteroAST):
	def __init__(self, token):
		super(ValueNode, self).__init__(token)

	def declare(self):
		pass

class StringNode(ValueNode):
	def __init__(self, token):
		super(StringNode, self).__init__(token)

	def declare(self):
		pass

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

	def declare(self):
		print("cmd")






