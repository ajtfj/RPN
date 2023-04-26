import re
from Token import *
from exceptions import *

lex_to_token_type = {
    "+": TokenType.PLUS,
    "-": TokenType.MINUS,
    "*": TokenType.STAR,
    "/": TokenType.SLASH
}    
    
class Regex:

    def isNum(line):
        num_pattern = re.compile('^[0-9]+$')
        return num_pattern.match(line) != None

    def isOP(line):
        op_pattern = re.compile('^[\+\-\/\*]$')
        return op_pattern.match(line) != None

def scanner(file):
    tokens = []

    for line in file:
        line = line.strip()
        if not line:
            continue
        
        if Regex.isNum(line):
            token = Token(TokenType.NUM, line)
            tokens.append(token)
            continue
        
        if Regex.isOP(line):
            tokenType = lex_to_token_type[line]
            token = Token(tokenType, line)
            tokens.append(token)
            continue
        
        raise UnexpectedCharacter(line)
        
    return tokens
