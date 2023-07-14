from __future__ import annotations
from abc import ABC
from PyLox.tokens import Token
from typing import Any

class Expr(ABC):
	def accept(self, visitor: Visitor):
		...

class Visitor(ABC):
	def visit_binary(self, expr: Binary):
		...

	def visit_grouping(self, expr: Grouping):
		...

	def visit_literal(self, expr: Literal):
		...

	def visit_unary(self, expr: Unary):
		...


class Binary(Expr):
	def __init__(self, left: Expr, operator: Token, right: Expr):
		self.left = left
		self.operator = operator
		self.right = right

	def accept(self,visitor: Visitor):
		return visitor.visit_binary(self)

class Grouping(Expr):
	def __init__(self, expression: Expr):
		self.expression = expression

	def accept(self,visitor: Visitor):
		return visitor.visit_grouping(self)

class Literal(Expr):
	def __init__(self, value: Any):
		self.value = value

	def accept(self,visitor: Visitor):
		return visitor.visit_literal(self)

class Unary(Expr):
	def __init__(self, operator: Token, right: Expr):
		self.operator = operator
		self.right = right

	def accept(self,visitor: Visitor):
		return visitor.visit_unary(self)
