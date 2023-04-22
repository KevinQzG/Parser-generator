import ply.lex as lex
import ply.yacc as yacc
from prettytable import PrettyTable

# Definir tokens
tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'POTENCIA',
    'MODULO',
    'PARENTESIS_IZQUIERDO',
    'PARENTESIS_DERECHO',
)

# Expresiones regulares para los tokens
t_NUMERO = r'\d+'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_POTENCIA = r'\^'
t_MODULO = r'%'
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print("Caracter inesperado '%s'" % t.value[0])
    t.lexer.skip(1)

# Reglas de producción para el parser
def p_expresion_suma(p):
    'expresion : expresion SUMA termino'
    p[0] = p[1] + p[3]

def p_expresion_resta(p):
    'expresion : expresion RESTA termino'
    p[0] = p[1] - p[3]

def p_expresion_termino(p): 
    'expresion : termino'
    p[0] = p[1]

def p_termino_multiplicacion(p):
    'termino : termino MULTIPLICACION factor'
    p[0] = p[1] * p[3]

def p_termino_division(p):
    'termino : termino DIVISION factor'
    if p[3] == 0:
        print("Error: división por cero")
        p[0] = 0
    else:
        p[0] = p[1] / p[3]

def p_termino_factor(p):
    'termino : factor'
    p[0] = p[1]

def p_factor_potencia(p):
    'factor : factor POTENCIA atom'
    p[0] = p[1] ** p[3]

def p_factor_modulo(p):
    'factor : factor MODULO atom'
    p[0] = p[1] % p[3]

def p_factor_atom(p):
    'factor : atom'
    p[0] = p[1]

def p_atom_parentesis(p):
    'atom : PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO'
    p[0] = p[2]

def p_atom_numero(p):
    'atom : NUMERO'
    p[0] = int(p[1])

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

# Crear el lexer y el parser
lexer = lex.lex()
parser = yacc.yacc()

# Función para evaluar una cadena de entrada
def evaluar(expresion):
    resultado = parser.parse(expresion)
    if resultado is not None:
        print(f"La expresión '{expresion}' es válida y su resultado es {resultado}")
    else:
        print(f"La expresión '{expresion}' es inválida para la gramatica")

menu = PrettyTable()
menu.field_names = ["Opción", "Descripción"]
menu.add_row(["1", "Evaluar expresión que ya está en el código"])
menu.add_row(["2", "Ingresar expresión a evaluar"])

print(menu)

opcion = input("Seleccione una opción (1 o 2): ")

if opcion == "1":
    print("Ha seleccionado la Opción 1" + "\n")
    evaluar("7 + 2 % 5")
    evaluar("3 + 1 * 9 - 0")
    evaluar("6 + 4 * 1 - 7 / 2")
    evaluar("5 + 2 * 3 - 4 / 0")
elif opcion == "2":
    print("Ha seleccionado la Opción 2" + "\n")
    expresion = input("Ingrese la expresión a evaluar: ")
    evaluar(expresion)
else:
    print("Opción inválida")

