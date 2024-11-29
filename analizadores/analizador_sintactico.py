import datetime
import sys
import ply.yacc as yacc
from ply import lex

from analizadores.analizador_lexico import palabras_reservadas, tokens
import analizadores.analizador_lexico as analizador

#INICIO DARIO LABORDE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO DARIO LABORDE
def p_codigo(p):
    ''' codigo : puts
               | gets
               | estructura_datos
               | estructura_control
               | llamada_metodo
               | declaracion_variable
               | almacenar_resultado_condicional
               | declaracion_estructura_datos
               | condiciones_con_conectores '''

def p_estructura_datos(p):
    ''' estructura_datos : array
                         | variable_arreglo
                         | acceder_arreglo '''

def p_estructura_control(p):
    ' estructura_control : if_statement '


# Reglas sintácticas mínimas
def p_declaracion_variable(p):
    ' declaracion_variable : variable ASSIGN value '

def p_almacenar_resultado_condicional(p):
    ' almacenar_resultado_condicional : variable ASSIGN condiciones '

def p_declaracion_estructura_datos(p):
    ' declaracion_estructura_datos :  variable_arreglo '

def p_condiciones_con_conectores(p):
    ' condiciones_con_conectores : condiciones conectores condiciones '


# Funciones
def p_llamada_metodo(p):
    ''' llamada_metodo : variable LEFT_PAR values RIGHT_PAR
                       | variable LEFT_PAR RIGHT_PAR '''

def p_value(p):
    ''' value : variable
              | numero
              | STRING
              | NIL
              | SYMBOL '''

def p_values_space(p):
    ''' values_space : value
                     | value SPACE values_space '''

def p_values(p):
    ''' values : value
               | value COMMA values '''

def p_variable(p):
    ''' variable : LOCAL_VARIABLE
                 | INSTANCE_VARIABLE
                 | CLASS_VARIABLE
                 | GLOBAL_VARIABLE
                 | CONSTANT '''

def p_numero(p):
    ''' numero : FLOAT
               | INTEGER '''

def p_gets(p):
    ''' gets : GETS DOT CHOMP DOT TO_F
             | GETS DOT CHOMP '''

def p_puts(p):
    ' puts : PUTS values '


# Estructura de datos (array)
def p_array(p):
    ''' array : array_explicito
              | array_implicito
              | array_creacion
              | array_new '''

def p_array_explicito(p):
    ''' array_explicito : LEFT_COR values RIGHT_COR
                        | LEFT_COR RIGHT_COR '''

def p_array_implicito(p):
    ''' array_implicito : PERCENT_W LEFT_COR values_space RIGHT_COR
                        | PERCENT_W LEFT_COR RIGHT_COR '''

def p_array_creacion(p):
    ' array_creacion : ARRAY LEFT_PAR array_explicito RIGHT_PAR '

def p_array_new(p):
    ''' array_new : ARRAY DOT NEW
                  | ARRAY DOT NEW LEFT_PAR INTEGER RIGHT_PAR
                  | ARRAY DOT NEW LEFT_PAR INTEGER COMMA values RIGHT_PAR '''

def p_variable_arreglo(p):
    ''' variable_arreglo : variable
                         | variable ASSIGN array '''

def p_acceder_arreglo(p):
    ' acceder_arreglo : variable_arreglo LEFT_COR INTEGER RIGHT_COR '


# Estructura de control (if)
def p_if_statement(p):
    ''' if_statement : IF condiciones NEWLINE codigo END
                     | IF condiciones NEWLINE codigo else_statement END '''

def p_else_statement(p):
    ' else_statement : ELSE NEWLINE codigo '

def p_condiciones(p):
    ''' condiciones : condicion
                    | condiciones conectores condiciones '''

def p_condicion(p):
    ''' condicion : numero operador_comparacion numero
                  | variable operador_comparacion numero
                  | numero operador_comparacion variable '''

def p_conectores(p):
    ''' conectores : AND
                   | OR
                   | AND_RESERVED
                   | OR_RESERVED '''

def p_operador_comparacion(p):
    ''' operador_comparacion : CASE_EQUAL
                             | EQUAL
                             | GREATER_THAN
                             | GREATER_THAN_EQUAL
                             | LESS_THAN
                             | LESS_THAN_EQUAL
                             | NOT_EQUAL
                             | SPACESHIP '''

def p_error(p):
    if p:
        error_msg = f"Error de sintaxis en linea {p.lineno}, posicion {p.lexpos}: Token inesperado '{p.value}' \n'{p}'"
    else:
        error_msg = "Syntax error: Unexpected end of input"
    print(error_msg)
#FIN DARIO LABORDE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DARIO LABORDE

#INICIO JORDAN SALINAS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO JORDAN SALINAS

# Estructuras de datos (hash)
def p_hash_declaration(p):
    ''' hash_declaration : HASH LEFT_COR values RIGHT_COR
                         | HASH LEFT_COR RIGHT_COR
    '''

def p_hash_access(p):
    ''' hash_access : variable LEFT_COR value RIGHT_COR
    '''

def p_hash_operations(p):
    ''' hash_operations : hash_access ASSIGN value
    '''



# Estructuras de control (while)
def p_while_statement(p):
    ''' while_statement : WHILE condiciones COLON codigo
    '''



def p_print_statement(p):
    ''' print_statement : PUTS LEFT_PAR values RIGHT_PAR
    '''

# Expresiones
def p_boolean_expression(p):
    ''' boolean_expression : expression GREATER_THAN expression
                           | expression LESS_THAN expression
                           | expression GREATER_THAN_EQUAL expression
                           | expression LESS_THAN_EQUAL expression
                           | expression EQUAL expression
                           | expression NOT_EQUAL expression
                           | BOOLEAN '''

def p_expression(p):
    ''' expression : INTEGER
                   | FLOAT
                   | variable
                   | STRING '''

# Declaraciones
def p_declaraciones(p):
    ''' declaraciones : declaracion_variable
                      | almacenar_resultado_condicional
                      | declaracion_estructura_datos
    '''

# Expresiones
def p_expresion(p):
    ''' expresion : puts
                 | gets
                 | print_statement
    '''


def p_set_expression(p):
    """set_expression : SET DOT NEW LEFT_PAR LEFT_COR values RIGHT_COR RIGHT_PAR
                      | SET LEFT_COR values RIGHT_COR"""

def p_set_operations(p):
    """set_operations : set_expression
                      | set_operations set_binary_operators set_expression"""

def p_set_declaration(p):
    """declaracion_estructura_datos : LOCAL_VARIABLE ASSIGN set_expression"""

def p_set_binary_operators(p):
    """set_binary_operators : PLUS
                            | MINUS
                            | AMPERSAND
                            | PIPE
                            | CARET"""

def p_unless_expression(p):
    """unless_expression : UNLESS boolean_expression THEN expresion END
                         | UNLESS boolean_expression THEN expresion ELSE expresion END"""

def p_arithmetic_expression(p):
    """expresion : arithmetic_production"""

def p_arithmetic_production(p):
    """arithmetic_production : numero
                             | variable
                             | numero arithmetic_operators arithmetic_production
                             | variable arithmetic_operators arithmetic_production"""

def p_arithmetic_operators(p):
    """arithmetic_operators : PLUS
                            | MINUS
                            | MULTIPLY
                            | DIVIDE
                            | MODULO
                            | EXPONENT"""

def p_block_expression(p):
    """block_expression : LBRACE expresion RBRACE
                         | DO expresion END
                         | LBRACE PIPE LOCAL_VARIABLE PIPE expresion RBRACE
                         | DO PIPE LOCAL_VARIABLE PIPE expresion END"""

def p_block_assignment(p):
    """block_assignment : llamada_metodo block_expression"""

def p_proc_expression(p):
    """proc_expression : PROC DOT NEW block_expression"""

def p_proc_assignment(p):
    """proc_assignment : LOCAL_VARIABLE ASSIGN proc_expression"""

def p_proc_call(p):
    """proc_call : LOCAL_VARIABLE DOT CALL LEFT_PAR values RIGHT_PAR
                 | LOCAL_VARIABLE DOT LEFT_PAR values RIGHT_PAR
                 | LOCAL_VARIABLE LEFT_COR values RIGHT_COR"""

def p_condition_expr(p):
    """expresion : condiciones_con_conectores"""

algoritmo_jordansalinasp10 = """
nombre = "María"
edad = 30
es_mayor_de_edad = edad >= 18

puts "Hola, #{nombre}. Tienes #{edad} años."
puts "¿Eres mayor de edad? #{es_mayor_de_edad}"

persona = { nombre: "Carlos", edad: 25, ciudad: "Bogotá" }
puts "Información de la persona: #{persona}"
persona[:edad] = 26
puts "Edad actualizada: #{persona[:edad]

if edad < 18
  puts "Eres menor de edad."
elsif edad == 18
  puts "¡Acabas de cumplir la mayoría de edad!"
else
  puts "Eres mayor de edad."
end

def saludo_personalizado(nombre, hora)
  if hora < 12
    "Buenos días, #{nombre}."
  elsif hora < 18
    "Buenas tardes, #{nombre}."
  else
    "Buenas noches, #{nombre}."
  end
end

x = 10
y = 5
z = x * y - (x + y)
puts "Resultado de la operación: #{z}"

dia = "lunes"
case dia
when "lunes"
  puts "Inicio de semana"
when "viernes"
  puts "Fin de semana cercano"
else
  puts "Es un día común"
end


numeros = [1, 2, 3, 4]
numeros.each { |n| puts "Número: #{n}, Cuadrado: #{cuadrado(n)}" }
if x > y
  puts "#{x} es mayor que #{y}"
else
  puts "#{y} es mayor o igual a #{x}"
end

"""
#FIN JORDAN SALINAS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN JORDAN SALINAS


algoritmo_dlaborde = """
variable1 = 10
variable2 = 20
resultado = nil

if variable1 > 5 && variable2 < 30
  resultado = "Ambas condiciones son verdaderas"
else
  resultado = "Una o ambas condiciones son falsas"
end

puts resultado

array_explicito = [1, 2, 3, 4]
array_implicito = %w[manzana naranja plátano]

primer_elemento = array_explicito[0]
puts "El primer elemento del arreglo explícito es: #{primer_elemento}"

array_explicito[1] = 10
puts "El arreglo modificado es: #{array_explicito}"

array_new = Array.new(3, "valor")
puts "Arreglo creado con 'Array.new': #{array_new}"

def saludo(nombre, edad)
  "Hola, #{nombre}. Tienes #{edad} años."
end

puts saludo("Carlos", 25)

def despedida
  "Adiós, hasta pronto."
end

puts despedida

if variable1 < variable2
  puts "variable1 es menor que variable2"
elsif variable1 == variable2
  puts "variable1 es igual a variable2"
else
  puts "variable1 es mayor que variable2"
end

puts "Introduce un número:"
numero = gets.chomp.to_i
puts "El número que introdujiste es: #{numero}"

CONSTANTE = :mi_constante
puts "Este es un símbolo constante: #{CONSTANTE}"

if variable1 <=> variable2
  puts "Comparación con spaceship: #{variable1 <=> variable2}"
end
"""

parser = yacc.yacc()
# while True:
#    try:
#        s = input('calc > ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)

#log_filename = f"../logs/sintactico/sintactico-dlaborde27-{datetime.datetime.now().strftime('%Y%m%d-%Hh%M')}.txt"
# log_filename = f"../logs/sintactico/sintactico-jordansalinasp10-{datetime.datetime.now().strftime('%Y%m%d-%Hh%M')}.txt"
# print("Ruta completa:", log_filename )
# with open(log_filename , "w") as f:
#     sys.stdout = f
#     result = parser.parse(algoritmo_jordansalinasp10)
#     sys.stdout = sys.__stdout__
#     print("Análisis completado. Los errores sintácticos se han guardado en el archivo de registro:", log_filename)
#

def llamada_lexer():
    global lexer
    lexer = lex.lex()