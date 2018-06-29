
class Symbol(object):
	def __init__(self, name = None, s_type = None):
		self.__name = name
		self.__type = s_type

	def name(self):
		return self.__name

	def type(self):
		return self.__type

class BuiltInTypeSymbol(Symbol):
	def __init__(self, name):
		super(BuiltInTypeSymbol, self).__init__(name) 

class ObjectSymbol(Symbol):
	def __init__(self, name, scope):
		super(ObjectSymbol, self).__init__(name)

class ArraySymbol(Symbol):
	def __init__(self, name):
		super(ArraySymbol, self).__init__(name)