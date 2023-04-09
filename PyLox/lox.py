import sys
from typing import List

from PyLox.scanner import Scanner
from PyLox.tokens import Token


had_error = False
def main():
    args = sys.argv
    if len(args) > 2:
        print("Usage: lox.py [script]")
        sys.exit(64)
    elif len(args) == 2:
        run_file(args[1])
    else:
        run_prompt()


def run_file(path):
    with open(path, "r") as f:
        raw_code = f.read()
    run(raw_code)

    if had_error:
        sys.exit(65)


def run_prompt():
    while True:
        try:
            line = input()
        except EOFError:
            break
        run(line)
        had_error = False


def run(source: str):
    scanner = Scanner(source)
    tokens: List[Token] = scanner.scan_tokens()
    for token in tokens:
        print(token)


def error(line_num: int, messaage: str):
    report(line_num, "", messaage)


def report(line_num: int, where: str, message: str):
    print("[line " + line_num + "] Error" + where + ": " + message)
    had_error = True


if __name__ == "__main__":
    main()
