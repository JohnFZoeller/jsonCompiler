from enum import Enum

class Token(object):
	#public static
	Token_Type = Enum('Token_Type', 
		'INT BOOL STRING OBJECT OPERATOR NULL COMMAND EOF')

	def __init__(self, token_type, value):
		#non-static private
		self.__type = token_type
		self.__value = value

	def __str__(self):
		typeName = self.Token_Type(self.__type.value).name
		return "[" + typeName + "] -> " + self.__value + ""

	def type(self):
		return self.__type

	def value(self):
		return self.__value


