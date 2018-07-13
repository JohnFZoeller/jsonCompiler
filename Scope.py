
class Scope(object):
	def __init__(self, name = None, enclosing_scope = None):
		self.__scope_name = name
		self.__symbols = {}
		self.__scope = enclosing_scope
		self._objects = list()

	def __str__(self):
		return "scope: " + str(self.__scope_name)
		pass

	def build_global(self, built_ins):
		self.__symbols = {sym.name() : sym for sym in built_ins}
		pass

	def define(self, symbol):
		self.__symbols[symbol.name()] = symbol

		if symbol.is_object():
			self._objects.append(symbol)

	def resolve(self, symbol_name):
		resolved_symbol = self.__symbols.get(symbol_name)

		if resolved_symbol:
			return resolved_symbol
		if self.__scope:
			return self.__scope.resolve(symbol_name)
		return None

	def scope_name(self):
		return self.__scope_name
		pass

	#@deprecated
	def contains_objects(self):
		return len(self._objects) > 0
		pass

	def pop_object(self):
		return self._objects.pop()
		pass

	def peek_object(self):
		return self._objects[len(self._objects) - 1]

	#should have been doing this since the beginning...
	@property
	def objects(self):
		return self._objects
