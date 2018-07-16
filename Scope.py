
class Scope(object):
	def __init__(self, name = None, enclosing_scope = None):
		self.__scope_name = name
		self.__symbols = {}
		self.__scope = enclosing_scope
		self._objects = list()

	def __str__(self):
		return "scope: " + str(self.__scope_name)
		pass

	@property
	def scope_name(self):
		return self.__scope_name
	
	@property
	def objects(self):
		return self._objects

	def build_global(self, built_ins):
		self.__symbols = {sym.name : sym for sym in built_ins}
		pass

	def define(self, symbol):
		self.__symbols[symbol.name] = symbol

		if symbol.is_object():
			#you want the most recent objects to resolve first
			self._objects.insert(0, symbol)

	def resolve(self, symbol_name):
		resolved_symbol = self.__symbols.get(symbol_name)

		if resolved_symbol:
			return resolved_symbol
		# if self.__scope:
		# 	return self.__scope.resolve(symbol_name)
		#doesnt apply here
		#you wouldent want address.address to resolve...
		return None

	def contains_objects(self):
		return len(self._objects) > 0
		pass

	def pop_object(self):
		return self._objects.pop()
		pass

	def peek_object(self):
		return self._objects[0]
