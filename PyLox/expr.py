from abc import ABC
from PyLox.tokens import Token

class Expr(ABC):
	...

class Binary(Expr):
	def __init__(self, left: type, operator: type, right: type):
		self.left  = left
		self.operator  = operator
		self.right  = right

class Grouping(Expr):
	def __init__(self, expression: type):
		self.expression  = expression

class Literal(Expr):
	def __init__(self, value: type):
		self.value  = value

class Unary(Expr):
	def __init__(self, operator: type, right: type):
		self.operator  = operator
		self.right  = right
