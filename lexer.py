from sly import Lexer

class customLexer(Lexer):
    tokens = {
        BEG, END, DATATYPE, ASSIGN, TO, PRINT, SCAN, READ, COMMA, OPEN, CLOSE,
        IF, THEN, ELSE, ENDIF, WHILE, ENDWHILE, ENDDOWHILE, DO, FOR, FROM, REPEAT,
        RETURN, ENDFOR, QUOTE, BOOL, RELOP, LOGOP, AS, MD, Q, START_PROCEDURE,
        END_FUNCTION, VAR, NAME_PROCEDURE, NUM, STRING
    }

    ignore = ' '
    ignore_comment = r'[\/\/].*'
    ignore_newline = r'\n+'

    BEG = r'\b(begin|start)\b'
    END = r'\bend\b'
    DATATYPE = r'int|float|char|double'
    ASSIGN = r'assign'
    TO = r'to'
    PRINT = r'print'
    SCAN = r"scan"
    READ = r'read'
    COMMA = r","
    OPEN = r"\("
    CLOSE = r"\)"
    IF = r'if'
    THEN = r'then'
    ELSE = r'else'
    ENDIF = r'endif'
    WHILE = r'while'
    ENDWHILE = r'endwhile'
    ENDDOWHILE = r'enddowhile'
    DO = r'do'
    FOR = r'for'
    FROM = r'from'
    REPEAT = r'repeat'
    RETURN = r'return'
    ENDFOR = r'endfor'
    STRING = r'\".*?\"'
    QUOTE = r"\""
    BOOL = r'true|false'
    RELOP = r"<=|>=|==|<|>"
    LOGOP = r"&&|\|\|"
    AS = r"\+|\-"
    MD = r"\*|\\|%"
    Q = r"="
    START_PROCEDURE = r'start_procedure'
    END_FUNCTION = r'end_procedure'
    NAME_PROCEDURE = r'[a-zA-Z_][a-zA-Z0-9_]*[(]'
    VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUM = r'[0-9]+'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
