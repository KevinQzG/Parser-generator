# Parser-generator
Parser generator made with PLY library in Python.

In this parser generator, we have three .py files, which receive a specific grammar and receive several strings of the grammar, which can be valid or invalid and which I will explain in detail:

## Parser_aritmetica
This code implements a simple calculator capable of evaluating arithmetic expressions including addition, subtraction, multiplication, division, power and modulus operations, as well as parentheses to control the order of operations. The program uses the PLY (Python Lex-Yacc) library to define and parse tokens and grammar production rules, and the PrettyTable library to print a table of menu options.

The program starts by defining the tokens through regular expressions that are used to recognize the different elements of the expression. Each token represents a type of element, such as a number, an addition operator or a left parenthesis.

Next, production rules are defined for the parser. Each rule defines how the different tokens should be combined and produce a final result. For example, the p_expression_sum rule defines that an expression can be expressed as the sum of another expression and a term, while the p_factor_atom rule defines that a factor can simply be a number.

Then, a lexer and a parser are created through the lex.lex() and yacc.yacc() functions provided by PLY. The lexer is responsible for converting the text input into a sequence of tokens that the parser can process. The parser uses the production rules to parse the tokens and produce a final result.

Finally, the program displays a menu that allows the user to choose between two options: evaluate an expression that is already in the code or enter an expression to evaluate. Depending on the option chosen, the program calls the evaluate() function to process the expression and display the result. If the expression is invalid for the grammar, an error message is displayed instead.

## Parser_booleano
The code implements a syntactic and lexical analyzer to evaluate Boolean expressions. First, tokens are defined, which are the basic elements used to construct Boolean expressions, such as TRUE, FALSE, NOT, AND, OR, LEFT_ PARENThesis and RIGHT_ PARENThesis. 

Next, parser production rules are defined, which specify how tokens should be combined to build more complex Boolean expressions. For example, the p_expression_not rule indicates that a Boolean expression can be a NOT expression followed by another Boolean expression. The other production rules are defined similarly.

The evaluate() function uses the parser to evaluate a given Boolean expression. The function first calls the parser to parse the expression and returns the result of the evaluation. Then, it prints whether the expression is valid for the grammar and the result of the evaluation.

The program also displays a menu with two options: evaluate expressions that are already in the code (option 1) or enter an expression to evaluate (option 2). Depending on the selected option, the program calls the evaluate() function with the corresponding expression. If the selected option is not valid, an error message is displayed. 

Finally, the PrettyTable library is used to display the menu in a table with two columns: Option and Description.

## Parser_palindromo
This code implements a lexical and syntactic analyzer to recognize whether a string is a palindrome or not. 

First, the necessary libraries are imported, such as ply.lex and ply.yacc for lexical and syntactic analysis, respectively, and prettytable to display a menu to the user.

Next, a single token called "WORD" is defined and used to represent a string containing only letters and whitespace.

Next, a function t_WORD(token) is defined to parse the string and convert it to lowercase. If any invalid characters are found, an error message is printed using the defined function t_error(token).

Next, a grammar rule p_palindrome(p) is defined that uses the token WORD to construct the grammar. This grammar accepts a string that is a palindrome (a string that reads the same from left to right and right to left) and rejects a string that is not. The function evaluate(string) uses the parser to evaluate whether a string is a palindrome or not.

Finally, a menu is displayed to the user with two options: evaluate predefined expressions or enter an expression to evaluate. Depending on the option selected by the user, the corresponding expression is evaluated using the evaluate(string) function. If an invalid option is entered, an error message is displayed.

## How to use
In order to execute any of the three files we only need to have installed in our Python, the "ply and prettytable" library, which is installed with the command "pip install ply" and "pip install prettytable". After this, we must run our code, which will show us a console menu with two options:
 1. Analyze a string that has already been defined in the code.
 2. Parse a string that the user enters by console.

After this, it will generate a file called "parser.out" and "parsertab.py" which are files that show us the rules, productions, terminals, non terminals, states and other things that a parser must do and thanks to our library generates all this.

## Practice Members
**- <a href="https://github.com/KevinQzG">Kevin Quiroz Gonzalez</a>**

## Compilator
This practice was done **<a href="https://www.python.org">Python</a>** together with its built-in compiler **Python Compiler Version 3.10.8**


