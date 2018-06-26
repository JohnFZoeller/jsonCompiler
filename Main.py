#!/usr/bin/env python3
from Lexer import Lexer
from SyntaxParser import SyntaxParser
import sys

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('No File argument. Terminating')
	else:
		lexer = Lexer(sys.argv[1])
		syntax_parser = SyntaxParser(lexer)

	