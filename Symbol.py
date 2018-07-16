from Scope import Scope

class Symbol(object):
	def __init__(self, name = None, s_type = None):
		self.__name = name if name else "Object at -> " + str(id(self))
		self.__type = s_type

	def __str__(self):
		return ("Name: " + str(self.__name) + " Type: "+
		 	str(self.__type))

	@property
	def name(self):
		return self.__name

	@property
	def type(self):
		return self.__type

	@property
	def value_symbol(self):
		return None

	def is_object(self):
		return False

class BuiltInTypeSymbol(Symbol):
	def __init__(self, name):
		super(BuiltInTypeSymbol, self).__init__(name, 
			self.__class__)

	def __str__(self):
		return "BuiltIn(" + str(self.name) + ")"
		

class ObjectSymbol(Symbol, Scope):
	def __init__(self, enclosing_scope):
		Symbol.__init__(self)
		scope_name = self.make_name(enclosing_scope.scope_name)
		Scope.__init__(self, scope_name, enclosing_scope)

	def is_object(self):
		return True

	def make_name(self, enclosing_scope_name):
		return (str(enclosing_scope_name) + " : " + 
			str(self.name))

class ArraySymbol(Symbol):
	def __init__(self):
		super(ArraySymbol, self).__init__()
		self.__size = 0
		self.__elements = list()

	def __str__(self):
		result = ""
		for e in self.__elements:
			result += str(e) + ', '
		return result

	def append(self, symbol):
		self.__elements.append(symbol)
		self.__size += 1

	def get_array_element(self, idx):
		return self.__elements[int(idx)]


class KeyValueSymbol(Symbol):
	def __init__(self, name, type, value_symbol):
		super(KeyValueSymbol, self).__init__(name, type)
		self.__value_symbol = value_symbol

	@property
	def value_symbol(self):
		return self.__value_symbol


