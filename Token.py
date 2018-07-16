from enum import Enum

class Token(object):
	#public static
	Token_Type = Enum('Token_Type', 
		'INT BOOL STRING OBJECT OPERATOR NULL COMMAND EOF')

	def __init__(self, token_type, value = "root"):
		#non-static private
		self.__type = token_type
		self.__value = value

	#replaces str, needed so that I can hash 
	def __repr__(self):
		# FIXME: <totally unreadable>
		typeName = self.Token_Type(self.type.value).name
		return "[" + typeName + "] -> " + self.value + ""

	def __eq__(self, other):
		if self.__type != Token.Token_Type.OPERATOR:
			return True
		return ((self.type, self.value) ==
					 (other.type, other.value))

	def __hash__(self):
		hash_tuple = ((self.type) 
			if self.type != self.Token_Type.OPERATOR 
			else (self.type, self.value))

		return hash(hash_tuple)

	def copy(self):
		return Token(self.type, self.value)

	@property
	def type(self):
		return self.__type

	@property
	def value(self):
		return self.__value

	def is_eof(self):
		return self.type == self.Token_Type.EOF

