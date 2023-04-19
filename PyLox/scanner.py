from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PyLox.lox import Lox

from typing import List, Type

from PyLox.tokens import Token, TokenType


def is_digit(c: str):
    return c in [str(i) for i in range(10)]


def is_alpha(c: str):
    return (c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or c == "_"


def is_alpha_numeric(c: str):
    return is_digit(c) or is_alpha(c)


class Scanner:
    keywords = dict()
    keywords["and"] = TokenType.AND
    keywords["class"] = TokenType.CLASS
    keywords["else"] = TokenType.ELSE
    keywords["false"] = TokenType.FALSE
    keywords["for"] = TokenType.FOR
    keywords["fun"] = TokenType.FUN
    keywords["if"] = TokenType.IF
    keywords["nil"] = TokenType.NIL
    keywords["or"] = TokenType.OR
    keywords["print"] = TokenType.PRINT
    keywords["return"] = TokenType.RETURN
    keywords["super"] = TokenType.SUPER
    keywords["this"] = TokenType.THIS
    keywords["true"] = TokenType.TRUE
    keywords["var"] = TokenType.VAR
    keywords["while"] = TokenType.WHILE

    def __init__(self, source: str, lox_instance: Lox) -> None:
        self.source = source
        self.tokens: List[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.lox = lox_instance

    def advance(self):
        next_char = self.source[self.current]
        self.current += 1
        return next_char

    def add_token(self, token_type: TokenType, literal=None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))

    def match(self, expected: str):
        if self.end():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self):
        if self.end():
            return "\0"
        return self.source[self.current]

    def peekNext(self):
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def end(self) -> bool:
        return self.current >= len(self.source)

    def string(self):
        while self.peek() != '"' and not self.end():
            if self.peek() == "\n":
                self.line += 1
            self.advance()

        if self.end():
            self.lox.error(line_num=self.line, messaage="Unterminated string.")
            return

        self.advance()

        literal = self.source[self.start + 1 : self.current - 1]
        self.add_token(TokenType.STRING, literal=literal)

    def number(self):
        while is_digit(self.peek()):
            self.advance()

        if self.peek() == "." and is_digit(self.peekNext()):
            self.advance()
            while is_digit(self.peek()):
                self.advance()

        literal = float(self.source[self.start : self.current])
        self.add_token(TokenType.NUMBER, literal)

    def identifier(self):
        while is_alpha_numeric(self.peek()):
            self.advance()

        text: str = self.source[self.start : self.current]
        type_: TokenType = Scanner.keywords.get(text, TokenType.IDENTIFIER)
        return self.add_token(type_)

    def scan_token(self):
        c: str = self.advance()
        match c:
            case "(":
                self.add_token(TokenType.LEFT_PAREN)
            case ")":
                self.add_token(TokenType.RIGHT_PAREN)
            case "{":
                self.add_token(TokenType.LEFT_BRACE)
            case "}":
                self.add_token(TokenType.RIGHT_BRACE)
            case ",":
                self.add_token(TokenType.COMMA)
            case ".":
                self.add_token(TokenType.DOT)
            case "-":
                self.add_token(TokenType.MINUS)
            case "+":
                self.add_token(TokenType.PLUS)
            case ";":
                self.add_token(TokenType.SEMICOLON)
            case "*":
                self.add_token(TokenType.STAR)
            case "!":
                self.add_token(
                    TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG
                )
            case "=":
                self.add_token(
                    TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL
                )
            case "<":
                self.add_token(
                    TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS
                )
            case ">":
                self.add_token(
                    TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER
                )
            case " " | "\t" | "\r":
                pass
            case "\n":
                self.line += 1
            case "/":
                if self.match("/"):
                    while not self.end() and self.peek() != "\n":
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            case '"':
                self.string()
            case _ as c if is_digit(c):
                self.number()
            case _ as c if is_alpha(c):
                self.identifier()

            case _:
                self.lox.error(self.line, "Unexpected character.")

    def scan_tokens(self) -> List[Token]:
        while not self.end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens
