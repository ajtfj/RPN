from enum import Enum

class TokenType(Enum):
    NUM = 1
    MINUS = 2
    PLUS = 3
    SLASH = 4
    STAR = 5
    EOF = 6

    def __str__(self) -> str:
        return self.name

class Token:
    def __init__(self, type, lexeme):
        self.type = type
        self.lexeme = lexeme

    def __str__(self):
        return f"Token [type={self.type}, lexeme={self.lexeme}]"