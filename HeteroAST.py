from Token import Token

class HeteroAST(object):
	def __init__(self, lexer = None, token = None):
		self._children = list()
		self._lexer = lexer
		self._token = token

	def add_child(self, tree_node):
		self._children.append(tree_node)
		pass

	def match_operator(self, expect):
		if self._token.value() == expect:
			self.set_token()
		else:
			raise ValueError('Expected a : ' + expect + ' Got: ' +
				self._token.value())

	def match(self, expect):
		if self._token.type() == expect:
			self.set_token()
		else:
			raise ValueError('Expected a : ' + expect)

	def set_token(self):
		self._token = self._lexer.get_next_token()
		pass

	def has_members(self):
		return self._token.value() != '}'
		pass

class ObjectNode(HeteroAST):
	def __init__(self, lexer, token):
		super(ObjectNode, self).__init__(lexer, token)

		self.match_operator('{')
		print(self._token)

		if self.has_members():
			self.add_child(MembersNode(self._lexer, self._token))

		self.match_operator('}')

class MembersNode(HeteroAST):
	def __init__(self, lexer, token):
		super(MembersNode, self).__init__(lexer, token)

		self.add_child(PairNode(self._lexer, self._token))

		print(self._lexer.get_next_token())

		if self._token.value() != ',':
			return

		match_operator(',')
		self.add_child(MembersNode(self._lexer, self._token))


class PairNode(HeteroAST):
	def __init__(self, lexer, token):
		
		print(lexer.get_next_token())
		print(lexer.get_next_token())

		
		# self.add_child(String(self._token))
		# self.match(Token.Token_Type.STRING)
		# self.match_operator(':')

		# #temp
		# self.match(Token.Token_Type.STRING)
		# print()
		#match value
		pass

class String(HeteroAST):
	def __init__(self, token):
		super(String, self).__init__(token)



