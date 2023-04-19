import sys
from typing import List

from PyLox.scanner import Scanner
from PyLox.tokens import Token, TokenType


class Lox:
    had_error = False

    @staticmethod
    def main():
        args = sys.argv
        if len(args) > 2:
            print("Usage: lox.py [script]")
            sys.exit(64)
        elif len(args) == 2:
            Lox.run_file(args[1])
        else:
            Lox.run_prompt()

    @staticmethod
    def run_file(path):
        with open(path, "r") as f:
            raw_code = f.read()
        Lox.run(raw_code)

        if Lox.had_error:
            sys.exit(65)

    @staticmethod
    def run_prompt():
        while True:
            try:
                line = input()
            except EOFError:
                break
            Lox.run(line)
            Lox.had_error = False

    @staticmethod
    def run(source: str):
        scanner = Scanner(source, Lox)
        tokens: List[Token] = scanner.scan_tokens()
        for token in tokens:
            print(token)

    @staticmethod
    def error(line_num: int, messaage: str):
        Lox.report(line_num, "", messaage)

    @staticmethod
    def report(line_num: int, where: str, message: str):
        print(f"[line {line_num}] Error{where}: {message}")

        Lox.had_error = True


if __name__ == "__main__":
    Lox.main()
