# Educational Pseudocode Compiler

This project is a lightweight compiler designed for beginners who write simple pseudocode. The tool converts pseudocode into valid Python code using:

- **Lexical Analysis** with SLY's Lexer
- **Syntax Analysis** using a custom grammar and Parse Trees
- **Semantic Analysis** with variable declarations, type checks, and logic validation
- **Educational Error Feedback** to guide users through mistakes

## Key Features
- Replaces casual keywords (e.g., "repeat", "do this") with proper syntax
- Detects undeclared variables and type mismatches
- Displays helpful error messages for easier debugging
- Modular compiler phases: Lexer → Parser → Semantic Analyzer → Code Generator

## Tech Stack
- Python 3
- SLY (Lex-Yacc for Python)
- NLP preprocessing for keyword normalization

## Ideal For:
- Programming beginners
- Students learning compiler design
