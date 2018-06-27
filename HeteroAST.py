from Token import Token

class HeteroAST(object):
	def __init__(self, token = None):
		self._children = list()
		self._token = token.copy() if token != None else None

	def add_child(self, tree_node):
		self._children.append(tree_node)
		pass

class ObjectNode(HeteroAST):
	def __init__(self):
		super(ObjectNode, self).__init__()

class MembersNode(HeteroAST):
	def __init__(self):
		super(MembersNode, self).__init__()

class PairNode(HeteroAST):
	def __init__(self):
		super(PairNode, self).__init__()

class ValueNode(HeteroAST):
	def __init__(self, token):
		super(ValueNode, self).__init__(token)

class StringNode(ValueNode):
	def __init__(self, token):
		super(StringNode, self).__init__(token)

class IntNode(ValueNode):
	def __init__(self, token):
		super(IntNode, self).__init__(token)

class BoolNode(ValueNode):
	def __init__(self, token):
		super(BoolNode, self).__init__(token)








