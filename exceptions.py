class UnexpectedCharacter(Exception):
    def __init__(self, line):
        self.line = line

    def __str__(self) -> str:
        return f"Error: Unexpected character: {self.line}"
    
class MalformedInput(Exception):
    def __str__(self) -> str:
        return "Error: Malformed input"   