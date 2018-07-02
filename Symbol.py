from Scope import Scope

class Symbol(object):
	def __init__(self, name = None, s_type = None):
		self.__name = name if name else id(self)
		self.__type = s_type

	def __str__(self):
		return ("Name: " + str(self.__name) + " Type: "+
		 	str(self.__type))

	def name(self):
		return self.__name

	def type(self):
		return self.__type

	def is_object(self):
		return False

	def get(self):
		return None

class BuiltInTypeSymbol(Symbol):
	def __init__(self, name):
		super(BuiltInTypeSymbol, self).__init__(name, 
			self.__class__)

	def __str__(self):
		return "BuiltIn(" + str(self.name()) + ")"
		

class ObjectSymbol(Symbol, Scope):
	def __init__(self, enclosing_scope):
		Symbol.__init__(self)
		scope_name = self.make_name(enclosing_scope.scope_name())
		Scope.__init__(self, scope_name, enclosing_scope)

	def is_object(self):
		return True

	def make_name(self, enclosing_scope_name):
		return (str(enclosing_scope_name) + " : " + 
			str(self.name()))

class ArraySymbol(Symbol):
	def __init__(self):
		super(ArraySymbol, self).__init__()

class KeyValueSymbol(Symbol):
	def __init__(self, name, type, value_symbol):
		super(KeyValueSymbol, self).__init__(name, type)
		self.__value_symbol = value_symbol

	def get(self):
		return self.__value_symbol


