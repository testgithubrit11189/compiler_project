from sly import Parser

class customParser(Parser):
    tokens = {
        BEG, END, DATATYPE, ASSIGN, TO, PRINT, SCAN, READ, COMMA, OPEN, CLOSE,
        IF, THEN, ELSE, ENDIF, WHILE, ENDWHILE, ENDDOWHILE, DO, FOR, FROM, REPEAT,
        RETURN, ENDFOR, QUOTE, BOOL, RELOP, LOGOP, AS, MD, Q, START_PROCEDURE,
        END_FUNCTION, VAR, NAME_PROCEDURE, NUM, STRING
    }

    def _init_(self):
        self.names = {}
        self.variables = set()
        self.undeclared_vars = set()
        self.funcdec = ""

    # Add all your grammar rules from the original code here (as in your customParser)
    # Example:
    @_('BEG CODE END')
    def START(self, p):
        return "#include<stdio.h>\n" + self.funcdec + "void main()\n{\n" + p.CODE + "}"

    # (rest of the rules go here)

    def find_type(self, datatype):
        if datatype == 'int':
            return "%d"
        elif datatype == 'char':
            return "%c"
        elif datatype == 'float':
            return "%f"
        else:
            return "%ld"

    def update_VAR(self, var):
        if var in self.variables:
            print(f"Same variable used twice: {var}")
        else:
            self.variables.add(var)

    def check_VAR(self, var):
        if var in self.variables:
            return True
        else:
            self.undeclared_vars.add(var)
            return False
