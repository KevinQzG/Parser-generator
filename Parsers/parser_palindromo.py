import ply.lex as lex
import ply.yacc as yacc
from prettytable import PrettyTable
# tokens
tokens = ['PALABRA']

# reglas
def t_PALABRA(token):
    r'[a-zA-Z ]+'
    token.value = token.value.lower()
    return token

# definición de errores lexicográficos
def t_error(token):
    print(f"Carácter no válido '{token.value[0]}'")
    token.lexer.skip(1)

# reglas de precedencia
precedence = () 

# reglas de gramática
def p_palindromo(p):
    """
    palindromo : PALABRA
               | PALABRA palindromo
    """
    cadena = p[1].replace(' ', '')
    if cadena == cadena[::-1]:
        print(f"La cadena '{p[1]}' es un palíndromo y es aceptada por la gramática")
    else:
        print(f"La cadena '{p[1]}' no es un palíndromo y no es aceptada por la gramática")

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis en entrada")

# construcción del lexer y parser
lexer = lex.lex()
parser = yacc.yacc()

# función para evaluar una cadena
def evaluar(cadena):
    resultado = parser.parse(cadena, lexer=lexer)
    return resultado


menu = PrettyTable()
menu.field_names = ["Opción", "Descripción"]
menu.add_row(["1", "Evaluar expresión que ya está en el código"])
menu.add_row(["2", "Ingresar expresión a evaluar"])

print(menu)

opcion = input("Seleccione una opción (1 o 2): ")

if opcion == "1":
    print("Ha seleccionado la Opción 1" + "\n")
    evaluar('Salta ese atlas')
    evaluar('Ojo rojo') 
    evaluar('anita lava la tina')
    evaluar('Sergio esto no es un palindromo')

elif opcion == "2":
    print("Ha seleccionado la Opción 2")
    expresion = input("Ingrese la expresión a evaluar: " + "\n")
    evaluar(expresion)
else:
    print("Opción inválida")
