from enum import Enum

class Token(object):
	#public static
	Token_Type = Enum('Token_Type', 
		'INT BOOL STRING OBJECT OPERATOR NULL COMMAND EOF')

	def __init__(self, token_type, value = "root"):
		#non-static private
		self.__type = token_type
		self.__value = value

	#replaces str
	def __repr__(self):
		typeName = self.Token_Type(self.__type.value).name
		return "[" + typeName + "] -> " + self.__value + ""

	def __eq__(self, other):
		if self.__type != Token.Token_Type.OPERATOR:
			return True
		return ((self.__type, self.__value) ==
					 (other.__type, other.__value))

	def __hash__(self):
		hash_tuple = ((self.__type) 
			if self.__type != self.Token_Type.OPERATOR 
			else (self.__type, self.__value))

		return hash(hash_tuple)

	def copy(self):
		return Token(self.__type, self.__value)

	#@property
	def type(self):
		return self.__type

	def value(self):
		return self.__value

	def is_eof(self):
		return self.__type == self.Token_Type.EOF

