

class Scope(object):
	def __init__(self, name = None, enclosing_scope = None):
		self.__name = name
		self.__symbols = {}
		self.__scope = enclosing_scope

	def build_global(self, built_ins):
		self.__symbols = {sym.name() : sym for sym in built_ins}

	def define(self, symbol):
		self.__symbols[symbol.name()] = symbol

	def resolve(self, symbol_name):
		resolved_symbol = self.__symbols.get(symbol_name)

		if resolved_symbol:
			return resolved_symbol
		if self.__scope:
			return self.__scope.resolve(symbol_name)
		return None
