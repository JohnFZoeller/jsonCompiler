from enum import Enum

class Token(object):
	#static public
	Token_Type = Enum('Token_Type', 
		'INT BOOL STRING OBJECT OPERATOR NULL COMMAND')

	def __init__(self):
		#non-static private
		self.__type = 0
		self.__value = ""

	def __init__(self, token_type, value):
		self.__type = token_type.value
		self.__value = value

	def __str__(self):
		typeName = self.Token_Type(self.__type).name
		return "[" + typeName + "] -> " + self.__value + ""



