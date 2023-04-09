from typing import List

from PyLox.tokens import Token, TokenType


class Scanner:
    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens: List[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1

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

    def scan_tokens(self) -> List[Token]:
        while not self.end():
            c: str = self.advance()
            match c:
                case "(":
                    self.add_token(TokenType.LEFT_PAREN)
                    break
                case ")":
                    self.add_token(TokenType.RIGHT_PAREN)
                    break
                case "{":
                    self.add_token(TokenType.LEFT_BRACE)
                    break
                case "}":
                    self.add_token(TokenType.RIGHT_BRACE)
                    break
                case ",":
                    self.add_token(TokenType.COMMA)
                    break
                case ".":
                    self.add_token(TokenType.DOT)
                    break
                case "-":
                    self.add_token(TokenType.MINUS)
                    break
                case "+":
                    self.add_token(TokenType.PLUS)
                    break
                case ";":
                    self.add_token(TokenType.SEMICOLON)
                    break
                case "*":
                    self.add_token(TokenType.STAR)
                    break
                case "!":
                    self.add_token(
                        TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG
                    )
                    break
                case "=":
                    self.add_token(
                        TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL
                    )
                    break
                case "<":
                    self.add_token(
                        TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS
                    )
                    break
                case ">":
                    self.add_token(
                        TokenType.GREATER_EQUAL
                        if self.match("=")
                        else TokenType.GREATER
                    )
                    break

                case _:
                    print("error TODO handle later")
                    break

    def end(self) -> bool:
        return self.current >= len(self.source)
