#!/usr/bin/env python3
from Lexer import Lexer
from SyntaxParser import SyntaxParser
from coOc import *
import sys

def update_co_occurrence():
	if len(sys.argv) != 3:
		print('No Co-Occurrence input')
	else:
		desired_tokens = Lexer(sys.argv[2])
		token_stream = Lexer(sys.argv[1])
		co_occurrence(desired_tokens, token_stream)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('No File argument. Terminating')
	else:
		update_co_occurrence()
		lexer = Lexer(sys.argv[1])
		syntax_parser = SyntaxParser(lexer)
		syntax_parser.parse()
		syntax_parser.decorate_AST()

	