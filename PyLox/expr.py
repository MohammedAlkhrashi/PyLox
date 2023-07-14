from abc import ABC
from PyLox.tokens import Token

class Expr(ABC):
	...

class Visitor(ABC):
	def visit_binary(expr):
		...

	def visit_grouping(expr):
		...

	def visit_literal(expr):
		...

	def visit_unary(expr):
		...


class Binary(Expr):
	def __init__(self, left: type, operator: type, right: type):
		self.left  = left
		self.operator  = operator
		self.right  = right

	def accept(self,visitor: Visitor):
		return visitor.visit_binary()

class Grouping(Expr):
	def __init__(self, expression: type):
		self.expression  = expression

	def accept(self,visitor: Visitor):
		return visitor.visit_grouping()

class Literal(Expr):
	def __init__(self, value: type):
		self.value  = value

	def accept(self,visitor: Visitor):
		return visitor.visit_literal()

class Unary(Expr):
	def __init__(self, operator: type, right: type):
		self.operator  = operator
		self.right  = right

	def accept(self,visitor: Visitor):
		return visitor.visit_unary()
