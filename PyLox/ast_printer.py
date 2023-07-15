from ast import List
from PyLox.expr import Binary, Grouping, Literal, Unary, Visitor, Expr
from PyLox.tokens import Token, TokenType


class AstPrinter(Visitor):
    def print(self, expr: Expr):
        return expr.accept(self)

    def visit_binary(self, expr: Binary):
        return self.parenthize(expr.operator.lexeme, expr.left, expr.right)

    def visit_grouping(self, expr: Grouping):
        return self.parenthize("group", expr.expression)

    def visit_literal(self, expr: Literal):
        if expr.value is None:
            return "nil"
        return str(expr.value)

    def visit_unary(self, expr: Unary):
        return self.parenthize(expr.operator.lexeme, expr.right)

    def parenthize(self, name: str, *exprs: Expr):
        output = []
        output.append("(")
        output.append(name)

        for expr in exprs:
            output.append(" ")
            output.extend(expr.accept(self))

        output.append(")")

        return "".join(output)


if __name__ == "__main__":
    expression = Binary(
        Unary(
            Token(TokenType.MINUS, "-", None, 1),
            Literal(123)
        ),
        Token(TokenType.PLUS, "+", None, 1),
        Grouping(Literal(312.2))
    )
    printer = AstPrinter()
    print(printer.print(expression))