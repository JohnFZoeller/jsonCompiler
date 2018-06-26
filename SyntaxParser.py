
class SyntaxParser(object):
	def __init__(self, lexer):
		self.__lexer = lexer
		#self.lexer_test(self.__lexer)

	def lexer_test(self, lexer):
		token = lexer.get_next_token()
		while token != None:
			print(token)
			token = lexer.get_next_token()
