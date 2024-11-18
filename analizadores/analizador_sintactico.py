import datetime
import sys
import ply.yacc as yacc
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

analizador.llamada_lexer()
parser = yacc.yacc()
# while True:
#    try:
#        s = input('calc > ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)

log_filename = f"../logs/sintactico/sintactico-dlaborde27-{datetime.datetime.now().strftime('%Y%m%d-%Hh%M')}.txt"

print("Ruta completa:", log_filename )
with open(log_filename , "w") as f:
    sys.stdout = f
    result = parser.parse(algoritmo_dlaborde)
    sys.stdout = sys.__stdout__
    print("Análisis completado. Los errores sintácticos se han guardado en el archivo de registro:", log_filename)