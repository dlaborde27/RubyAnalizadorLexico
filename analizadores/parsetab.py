
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND AND AND_RESERVED ARRAY ASSIGN BACKSLASH BEGIN BOOLEAN BREAK CALL CARET CASE CASE_EQUAL CHOMP CLASS CLASS_VARIABLE COLON COMMA CONSTANT DEF DEFINED DIVIDE DIVIDE_ASSIGN DO DOT DOUBLE_QUOTE ELSE ELSIF END EQUAL EXPONENT EXPONENT_ASSIGN FLOAT FOR GETS GLOBAL_VARIABLE GREATER_THAN GREATER_THAN_EQUAL HASH IF IN INSTANCE_VARIABLE INTEGER LBRACE LEFT_COR LEFT_PAR LESS_THAN LESS_THAN_EQUAL LOCAL_VARIABLE MINUS MINUS_ASSIGN MODULE MODULO MODULO_ASSIGN MULTIPLY MULTIPLY_ASSIGN NEW NEWLINE NIL NOT NOT_EQUAL OR OR_RESERVED PERCENT_W PIPE PLUS PLUS_ASSIGN PROC PUTS RANGE_EX RANGE_IN RBRACE REDO RETURN RIGHT_COR RIGHT_PAR SELF SET SPACE SPACESHIP STRING SYMBOL TAB THEN TO_F TO_I UNLESS UNTIL WHEN WHILE codigo : puts\n               | gets\n               | estructura_datos\n               | estructura_control\n               | llamada_metodo\n               | declaracion_variable\n               | almacenar_resultado_condicional\n               | declaracion_estructura_datos\n               | condiciones_con_conectores  estructura_datos : array\n                         | variable_arreglo\n                         | acceder_arreglo  estructura_control : if_statement  declaracion_variable : variable ASSIGN value  almacenar_resultado_condicional : variable ASSIGN condiciones  declaracion_estructura_datos :  variable_arreglo  condiciones_con_conectores : condiciones conectores condiciones  llamada_metodo : variable LEFT_PAR values RIGHT_PAR\n                       | variable LEFT_PAR RIGHT_PAR  value : variable\n              | numero\n              | STRING\n              | NIL\n              | SYMBOL  values_space : value\n                     | value SPACE values_space  values : value\n               | value COMMA values  variable : LOCAL_VARIABLE\n                 | INSTANCE_VARIABLE\n                 | CLASS_VARIABLE\n                 | GLOBAL_VARIABLE\n                 | CONSTANT  numero : FLOAT\n               | INTEGER  gets : GETS DOT CHOMP DOT TO_F\n             | GETS DOT CHOMP  puts : PUTS values  array : array_explicito\n              | array_implicito\n              | array_creacion\n              | array_new  array_explicito : LEFT_COR values RIGHT_COR\n                        | LEFT_COR RIGHT_COR  array_implicito : PERCENT_W LEFT_COR values_space RIGHT_COR\n                        | PERCENT_W LEFT_COR RIGHT_COR  array_creacion : ARRAY LEFT_PAR array_explicito RIGHT_PAR  array_new : ARRAY DOT NEW\n                  | ARRAY DOT NEW LEFT_PAR INTEGER RIGHT_PAR\n                  | ARRAY DOT NEW LEFT_PAR INTEGER COMMA values RIGHT_PAR  variable_arreglo : variable\n                         | variable ASSIGN array  acceder_arreglo : variable_arreglo LEFT_COR INTEGER RIGHT_COR  if_statement : IF condiciones NEWLINE codigo END\n                     | IF condiciones NEWLINE codigo else_statement END  else_statement : ELSE NEWLINE codigo  condiciones : condicion\n                    | condiciones conectores condiciones  condicion : numero operador_comparacion numero\n                  | variable operador_comparacion numero\n                  | numero operador_comparacion variable  conectores : AND\n                   | OR\n                   | AND_RESERVED\n                   | OR_RESERVED  operador_comparacion : CASE_EQUAL\n                             | EQUAL\n                             | GREATER_THAN\n                             | GREATER_THAN_EQUAL\n                             | LESS_THAN\n                             | LESS_THAN_EQUAL\n                             | NOT_EQUAL\n                             | SPACESHIP  hash_declaration : HASH LEFT_COR values RIGHT_COR\n                         | HASH LEFT_COR RIGHT_COR\n     hash_access : variable LEFT_COR value RIGHT_COR\n     hash_operations : hash_access ASSIGN value\n     while_statement : WHILE condiciones COLON codigo\n     print_statement : PUTS LEFT_PAR values RIGHT_PAR\n     boolean_expression : expression GREATER_THAN expression\n                           | expression LESS_THAN expression\n                           | expression GREATER_THAN_EQUAL expression\n                           | expression LESS_THAN_EQUAL expression\n                           | expression EQUAL expression\n                           | expression NOT_EQUAL expression\n                           | BOOLEAN  expression : INTEGER\n                   | FLOAT\n                   | variable\n                   | STRING  declaraciones : declaracion_variable\n                      | almacenar_resultado_condicional\n                      | declaracion_estructura_datos\n     expresion : puts\n                 | gets\n                 | print_statement\n    set_expression : SET DOT NEW LEFT_PAR LEFT_COR values RIGHT_COR RIGHT_PAR\n                      | SET LEFT_COR values RIGHT_CORset_operations : set_expression\n                      | set_operations set_binary_operators set_expressiondeclaracion_estructura_datos : LOCAL_VARIABLE ASSIGN set_expressionset_binary_operators : PLUS\n                            | MINUS\n                            | AMPERSAND\n                            | PIPE\n                            | CARETunless_expression : UNLESS boolean_expression THEN expresion END\n                         | UNLESS boolean_expression THEN expresion ELSE expresion ENDexpresion : arithmetic_productionarithmetic_production : numero\n                             | variable\n                             | numero arithmetic_operators arithmetic_production\n                             | variable arithmetic_operators arithmetic_productionarithmetic_operators : PLUS\n                            | MINUS\n                            | MULTIPLY\n                            | DIVIDE\n                            | MODULO\n                            | EXPONENTblock_expression : LBRACE expresion RBRACE\n                         | DO expresion END\n                         | LBRACE PIPE LOCAL_VARIABLE PIPE expresion RBRACE\n                         | DO PIPE LOCAL_VARIABLE PIPE expresion ENDblock_assignment : llamada_metodo block_expressionproc_expression : PROC DOT NEW block_expressionproc_assignment : LOCAL_VARIABLE ASSIGN proc_expressionproc_call : LOCAL_VARIABLE DOT CALL LEFT_PAR values RIGHT_PAR\n                 | LOCAL_VARIABLE DOT LEFT_PAR values RIGHT_PAR\n                 | LOCAL_VARIABLE LEFT_COR values RIGHT_CORexpresion : condiciones_con_conectores'
    
_lr_action_items = {'PUTS':([0,86,118,],[11,11,11,]),'GETS':([0,86,118,],[12,12,12,]),'LOCAL_VARIABLE':([0,11,24,26,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,67,70,71,86,87,100,104,118,120,121,],[19,43,43,43,43,43,-66,-67,-68,-69,-70,-71,-72,-73,43,-62,-63,-64,-65,43,43,43,19,43,43,43,19,43,43,]),'IF':([0,86,118,],[26,26,26,]),'INSTANCE_VARIABLE':([0,11,24,26,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,67,70,71,86,87,100,104,118,120,121,],[27,27,27,27,27,27,-66,-67,-68,-69,-70,-71,-72,-73,27,-62,-63,-64,-65,27,27,27,27,27,27,27,27,27,27,]),'CLASS_VARIABLE':([0,11,24,26,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,67,70,71,86,87,100,104,118,120,121,],[28,28,28,28,28,28,-66,-67,-68,-69,-70,-71,-72,-73,28,-62,-63,-64,-65,28,28,28,28,28,28,28,28,28,28,]),'GLOBAL_VARIABLE':([0,11,24,26,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,67,70,71,86,87,100,104,118,120,121,],[29,29,29,29,29,29,-66,-67,-68,-69,-70,-71,-72,-73,29,-62,-63,-64,-65,29,29,29,29,29,29,29,29,29,29,]),'CONSTANT':([0,11,24,26,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,67,70,71,86,87,100,104,118,120,121,],[30,30,30,30,30,30,-66,-67,-68,-69,-70,-71,-72,-73,30,-62,-63,-64,-65,30,30,30,30,30,30,30,30,30,30,]),'LEFT_COR':([0,14,17,19,20,21,22,23,27,28,29,30,32,47,64,68,79,84,85,86,89,92,103,105,115,118,119,125,],[24,45,-51,-29,-39,-40,-41,-42,-30,-31,-32,-33,67,24,-44,24,-52,100,-43,24,-46,-48,-45,-47,121,24,-49,-50,]),'PERCENT_W':([0,47,86,118,],[32,32,32,32,]),'ARRAY':([0,47,86,118,],[33,33,33,33,]),'FLOAT':([0,11,24,26,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,67,70,71,86,87,100,104,118,120,121,],[35,35,35,35,35,35,35,-66,-67,-68,-69,-70,-71,-72,-73,35,-62,-63,-64,-65,35,35,35,35,35,35,35,35,35,35,]),'INTEGER':([0,11,24,26,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,67,70,71,86,87,100,104,106,118,120,121,],[25,25,25,25,73,25,25,25,-66,-67,-68,-69,-70,-71,-72,-73,25,-62,-63,-64,-65,25,25,25,25,25,25,25,114,25,25,25,]),'$end':([1,2,3,4,5,6,7,8,9,10,13,14,15,16,17,19,20,21,22,23,25,27,28,29,30,31,35,36,37,38,39,40,41,42,43,64,72,75,76,77,78,79,80,81,82,83,85,89,92,93,94,95,97,98,102,103,105,107,110,116,117,119,125,127,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-51,-29,-39,-40,-41,-42,-35,-30,-31,-32,-33,-57,-34,-38,-27,-20,-21,-22,-23,-24,-29,-44,-37,-19,-20,-14,-15,-52,-21,-60,-17,-101,-43,-46,-48,-59,-61,-28,-53,-18,-58,-45,-47,-36,-54,-98,-55,-49,-50,-97,]),'END':([2,3,4,5,6,7,8,9,10,13,14,15,16,17,19,20,21,22,23,25,27,28,29,30,31,35,36,37,38,39,40,41,42,43,64,72,75,76,77,78,79,80,81,82,83,85,89,92,93,94,95,97,98,101,102,103,105,107,110,111,116,117,119,122,125,127,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-51,-29,-39,-40,-41,-42,-35,-30,-31,-32,-33,-57,-34,-38,-27,-20,-21,-22,-23,-24,-29,-44,-37,-19,-20,-14,-15,-52,-21,-60,-17,-101,-43,-46,-48,-59,-61,-28,-53,-18,110,-58,-45,-47,-36,-54,117,-98,-55,-49,-56,-50,-97,]),'ELSE':([2,3,4,5,6,7,8,9,10,13,14,15,16,17,19,20,21,22,23,25,27,28,29,30,31,35,36,37,38,39,40,41,42,43,64,72,75,76,77,78,79,80,81,82,83,85,89,92,93,94,95,97,98,101,102,103,105,107,110,116,117,119,125,127,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-51,-29,-39,-40,-41,-42,-35,-30,-31,-32,-33,-57,-34,-38,-27,-20,-21,-22,-23,-24,-29,-44,-37,-19,-20,-14,-15,-52,-21,-60,-17,-101,-43,-46,-48,-59,-61,-28,-53,-18,112,-58,-45,-47,-36,-54,-98,-55,-49,-50,-97,]),'STRING':([11,24,46,47,67,71,100,104,120,121,],[40,40,40,40,40,40,40,40,40,40,]),'NIL':([11,24,46,47,67,71,100,104,120,121,],[41,41,41,41,41,41,41,41,41,41,]),'SYMBOL':([11,24,46,47,67,71,100,104,120,121,],[42,42,42,42,42,42,42,42,42,42,]),'DOT':([12,33,72,84,],[44,69,96,99,]),'LEFT_PAR':([17,19,27,28,29,30,33,92,108,],[46,-29,-30,-31,-32,-33,68,106,115,]),'ASSIGN':([17,19,27,28,29,30,],[47,62,-30,-31,-32,-33,]),'CASE_EQUAL':([17,19,25,27,28,29,30,34,35,43,66,76,80,],[49,-29,-35,-30,-31,-32,-33,49,-34,-29,49,49,49,]),'EQUAL':([17,19,25,27,28,29,30,34,35,43,66,76,80,],[50,-29,-35,-30,-31,-32,-33,50,-34,-29,50,50,50,]),'GREATER_THAN':([17,19,25,27,28,29,30,34,35,43,66,76,80,],[51,-29,-35,-30,-31,-32,-33,51,-34,-29,51,51,51,]),'GREATER_THAN_EQUAL':([17,19,25,27,28,29,30,34,35,43,66,76,80,],[52,-29,-35,-30,-31,-32,-33,52,-34,-29,52,52,52,]),'LESS_THAN':([17,19,25,27,28,29,30,34,35,43,66,76,80,],[53,-29,-35,-30,-31,-32,-33,53,-34,-29,53,53,53,]),'LESS_THAN_EQUAL':([17,19,25,27,28,29,30,34,35,43,66,76,80,],[54,-29,-35,-30,-31,-32,-33,54,-34,-29,54,54,54,]),'NOT_EQUAL':([17,19,25,27,28,29,30,34,35,43,66,76,80,],[55,-29,-35,-30,-31,-32,-33,55,-34,-29,55,55,55,]),'SPACESHIP':([17,19,25,27,28,29,30,34,35,43,66,76,80,],[56,-29,-35,-30,-31,-32,-33,56,-34,-29,56,56,56,]),'AND':([18,25,27,28,29,30,31,35,43,65,78,81,82,93,94,102,],[58,-35,-30,-31,-32,-33,-57,-34,-29,58,58,-60,58,-59,-61,58,]),'OR':([18,25,27,28,29,30,31,35,43,65,78,81,82,93,94,102,],[59,-35,-30,-31,-32,-33,-57,-34,-29,59,59,-60,59,-59,-61,59,]),'AND_RESERVED':([18,25,27,28,29,30,31,35,43,65,78,81,82,93,94,102,],[60,-35,-30,-31,-32,-33,-57,-34,-29,60,60,-60,60,-59,-61,60,]),'OR_RESERVED':([18,25,27,28,29,30,31,35,43,65,78,81,82,93,94,102,],[61,-35,-30,-31,-32,-33,-57,-34,-29,61,61,-60,61,-59,-61,61,]),'RIGHT_COR':([24,25,27,28,29,30,35,37,38,39,40,41,42,43,63,67,73,88,90,95,109,113,124,],[64,-35,-30,-31,-32,-33,-34,-27,-20,-21,-22,-23,-24,-29,85,89,97,103,-25,-28,116,-26,126,]),'COMMA':([25,27,28,29,30,35,37,38,39,40,41,42,43,114,],[-35,-30,-31,-32,-33,-34,71,-20,-21,-22,-23,-24,-29,120,]),'RIGHT_PAR':([25,27,28,29,30,35,37,38,39,40,41,42,43,46,64,74,85,91,95,114,123,126,],[-35,-30,-31,-32,-33,-34,-27,-20,-21,-22,-23,-24,-29,75,-44,98,-43,105,-28,119,125,127,]),'NEWLINE':([25,27,28,29,30,31,35,43,65,81,93,94,102,112,],[-35,-30,-31,-32,-33,-57,-34,-29,86,-60,-59,-61,-58,118,]),'SPACE':([25,27,28,29,30,35,38,39,40,41,42,43,90,],[-35,-30,-31,-32,-33,-34,-20,-21,-22,-23,-24,-29,104,]),'CHOMP':([44,],[72,]),'SET':([62,],[84,]),'NEW':([69,99,],[92,108,]),'TO_F':([96,],[107,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,86,118,],[1,101,122,]),'puts':([0,86,118,],[2,2,2,]),'gets':([0,86,118,],[3,3,3,]),'estructura_datos':([0,86,118,],[4,4,4,]),'estructura_control':([0,86,118,],[5,5,5,]),'llamada_metodo':([0,86,118,],[6,6,6,]),'declaracion_variable':([0,86,118,],[7,7,7,]),'almacenar_resultado_condicional':([0,86,118,],[8,8,8,]),'declaracion_estructura_datos':([0,86,118,],[9,9,9,]),'condiciones_con_conectores':([0,86,118,],[10,10,10,]),'array':([0,47,86,118,],[13,79,13,13,]),'variable_arreglo':([0,86,118,],[14,14,14,]),'acceder_arreglo':([0,86,118,],[15,15,15,]),'if_statement':([0,86,118,],[16,16,16,]),'variable':([0,11,24,26,46,47,57,67,70,71,86,87,100,104,118,120,121,],[17,38,38,66,38,76,66,38,94,38,17,66,38,38,17,38,38,]),'condiciones':([0,26,47,57,86,87,118,],[18,65,78,82,18,102,18,]),'array_explicito':([0,47,68,86,118,],[20,20,91,20,20,]),'array_implicito':([0,47,86,118,],[21,21,21,21,]),'array_creacion':([0,47,86,118,],[22,22,22,22,]),'array_new':([0,47,86,118,],[23,23,23,23,]),'condicion':([0,26,47,57,86,87,118,],[31,31,31,31,31,31,31,]),'numero':([0,11,24,26,46,47,48,57,67,70,71,86,87,100,104,118,120,121,],[34,39,39,34,39,80,81,34,39,93,39,34,34,39,39,34,39,39,]),'values':([11,24,46,71,100,120,121,],[36,63,74,95,109,123,124,]),'value':([11,24,46,47,67,71,100,104,120,121,],[37,37,37,77,90,37,37,90,37,37,]),'operador_comparacion':([17,34,66,76,80,],[48,70,48,48,70,]),'conectores':([18,65,78,82,102,],[57,87,87,87,87,]),'set_expression':([62,],[83,]),'values_space':([67,104,],[88,113,]),'else_statement':([101,],[111,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> puts','codigo',1,'p_codigo','analizador_sintactico.py',11),
  ('codigo -> gets','codigo',1,'p_codigo','analizador_sintactico.py',12),
  ('codigo -> estructura_datos','codigo',1,'p_codigo','analizador_sintactico.py',13),
  ('codigo -> estructura_control','codigo',1,'p_codigo','analizador_sintactico.py',14),
  ('codigo -> llamada_metodo','codigo',1,'p_codigo','analizador_sintactico.py',15),
  ('codigo -> declaracion_variable','codigo',1,'p_codigo','analizador_sintactico.py',16),
  ('codigo -> almacenar_resultado_condicional','codigo',1,'p_codigo','analizador_sintactico.py',17),
  ('codigo -> declaracion_estructura_datos','codigo',1,'p_codigo','analizador_sintactico.py',18),
  ('codigo -> condiciones_con_conectores','codigo',1,'p_codigo','analizador_sintactico.py',19),
  ('estructura_datos -> array','estructura_datos',1,'p_estructura_datos','analizador_sintactico.py',22),
  ('estructura_datos -> variable_arreglo','estructura_datos',1,'p_estructura_datos','analizador_sintactico.py',23),
  ('estructura_datos -> acceder_arreglo','estructura_datos',1,'p_estructura_datos','analizador_sintactico.py',24),
  ('estructura_control -> if_statement','estructura_control',1,'p_estructura_control','analizador_sintactico.py',27),
  ('declaracion_variable -> variable ASSIGN value','declaracion_variable',3,'p_declaracion_variable','analizador_sintactico.py',32),
  ('almacenar_resultado_condicional -> variable ASSIGN condiciones','almacenar_resultado_condicional',3,'p_almacenar_resultado_condicional','analizador_sintactico.py',35),
  ('declaracion_estructura_datos -> variable_arreglo','declaracion_estructura_datos',1,'p_declaracion_estructura_datos','analizador_sintactico.py',38),
  ('condiciones_con_conectores -> condiciones conectores condiciones','condiciones_con_conectores',3,'p_condiciones_con_conectores','analizador_sintactico.py',41),
  ('llamada_metodo -> variable LEFT_PAR values RIGHT_PAR','llamada_metodo',4,'p_llamada_metodo','analizador_sintactico.py',46),
  ('llamada_metodo -> variable LEFT_PAR RIGHT_PAR','llamada_metodo',3,'p_llamada_metodo','analizador_sintactico.py',47),
  ('value -> variable','value',1,'p_value','analizador_sintactico.py',50),
  ('value -> numero','value',1,'p_value','analizador_sintactico.py',51),
  ('value -> STRING','value',1,'p_value','analizador_sintactico.py',52),
  ('value -> NIL','value',1,'p_value','analizador_sintactico.py',53),
  ('value -> SYMBOL','value',1,'p_value','analizador_sintactico.py',54),
  ('values_space -> value','values_space',1,'p_values_space','analizador_sintactico.py',57),
  ('values_space -> value SPACE values_space','values_space',3,'p_values_space','analizador_sintactico.py',58),
  ('values -> value','values',1,'p_values','analizador_sintactico.py',61),
  ('values -> value COMMA values','values',3,'p_values','analizador_sintactico.py',62),
  ('variable -> LOCAL_VARIABLE','variable',1,'p_variable','analizador_sintactico.py',65),
  ('variable -> INSTANCE_VARIABLE','variable',1,'p_variable','analizador_sintactico.py',66),
  ('variable -> CLASS_VARIABLE','variable',1,'p_variable','analizador_sintactico.py',67),
  ('variable -> GLOBAL_VARIABLE','variable',1,'p_variable','analizador_sintactico.py',68),
  ('variable -> CONSTANT','variable',1,'p_variable','analizador_sintactico.py',69),
  ('numero -> FLOAT','numero',1,'p_numero','analizador_sintactico.py',72),
  ('numero -> INTEGER','numero',1,'p_numero','analizador_sintactico.py',73),
  ('gets -> GETS DOT CHOMP DOT TO_F','gets',5,'p_gets','analizador_sintactico.py',76),
  ('gets -> GETS DOT CHOMP','gets',3,'p_gets','analizador_sintactico.py',77),
  ('puts -> PUTS values','puts',2,'p_puts','analizador_sintactico.py',80),
  ('array -> array_explicito','array',1,'p_array','analizador_sintactico.py',85),
  ('array -> array_implicito','array',1,'p_array','analizador_sintactico.py',86),
  ('array -> array_creacion','array',1,'p_array','analizador_sintactico.py',87),
  ('array -> array_new','array',1,'p_array','analizador_sintactico.py',88),
  ('array_explicito -> LEFT_COR values RIGHT_COR','array_explicito',3,'p_array_explicito','analizador_sintactico.py',91),
  ('array_explicito -> LEFT_COR RIGHT_COR','array_explicito',2,'p_array_explicito','analizador_sintactico.py',92),
  ('array_implicito -> PERCENT_W LEFT_COR values_space RIGHT_COR','array_implicito',4,'p_array_implicito','analizador_sintactico.py',95),
  ('array_implicito -> PERCENT_W LEFT_COR RIGHT_COR','array_implicito',3,'p_array_implicito','analizador_sintactico.py',96),
  ('array_creacion -> ARRAY LEFT_PAR array_explicito RIGHT_PAR','array_creacion',4,'p_array_creacion','analizador_sintactico.py',99),
  ('array_new -> ARRAY DOT NEW','array_new',3,'p_array_new','analizador_sintactico.py',102),
  ('array_new -> ARRAY DOT NEW LEFT_PAR INTEGER RIGHT_PAR','array_new',6,'p_array_new','analizador_sintactico.py',103),
  ('array_new -> ARRAY DOT NEW LEFT_PAR INTEGER COMMA values RIGHT_PAR','array_new',8,'p_array_new','analizador_sintactico.py',104),
  ('variable_arreglo -> variable','variable_arreglo',1,'p_variable_arreglo','analizador_sintactico.py',107),
  ('variable_arreglo -> variable ASSIGN array','variable_arreglo',3,'p_variable_arreglo','analizador_sintactico.py',108),
  ('acceder_arreglo -> variable_arreglo LEFT_COR INTEGER RIGHT_COR','acceder_arreglo',4,'p_acceder_arreglo','analizador_sintactico.py',111),
  ('if_statement -> IF condiciones NEWLINE codigo END','if_statement',5,'p_if_statement','analizador_sintactico.py',116),
  ('if_statement -> IF condiciones NEWLINE codigo else_statement END','if_statement',6,'p_if_statement','analizador_sintactico.py',117),
  ('else_statement -> ELSE NEWLINE codigo','else_statement',3,'p_else_statement','analizador_sintactico.py',120),
  ('condiciones -> condicion','condiciones',1,'p_condiciones','analizador_sintactico.py',123),
  ('condiciones -> condiciones conectores condiciones','condiciones',3,'p_condiciones','analizador_sintactico.py',124),
  ('condicion -> numero operador_comparacion numero','condicion',3,'p_condicion','analizador_sintactico.py',127),
  ('condicion -> variable operador_comparacion numero','condicion',3,'p_condicion','analizador_sintactico.py',128),
  ('condicion -> numero operador_comparacion variable','condicion',3,'p_condicion','analizador_sintactico.py',129),
  ('conectores -> AND','conectores',1,'p_conectores','analizador_sintactico.py',132),
  ('conectores -> OR','conectores',1,'p_conectores','analizador_sintactico.py',133),
  ('conectores -> AND_RESERVED','conectores',1,'p_conectores','analizador_sintactico.py',134),
  ('conectores -> OR_RESERVED','conectores',1,'p_conectores','analizador_sintactico.py',135),
  ('operador_comparacion -> CASE_EQUAL','operador_comparacion',1,'p_operador_comparacion','analizador_sintactico.py',138),
  ('operador_comparacion -> EQUAL','operador_comparacion',1,'p_operador_comparacion','analizador_sintactico.py',139),
  ('operador_comparacion -> GREATER_THAN','operador_comparacion',1,'p_operador_comparacion','analizador_sintactico.py',140),
  ('operador_comparacion -> GREATER_THAN_EQUAL','operador_comparacion',1,'p_operador_comparacion','analizador_sintactico.py',141),
  ('operador_comparacion -> LESS_THAN','operador_comparacion',1,'p_operador_comparacion','analizador_sintactico.py',142),
  ('operador_comparacion -> LESS_THAN_EQUAL','operador_comparacion',1,'p_operador_comparacion','analizador_sintactico.py',143),
  ('operador_comparacion -> NOT_EQUAL','operador_comparacion',1,'p_operador_comparacion','analizador_sintactico.py',144),
  ('operador_comparacion -> SPACESHIP','operador_comparacion',1,'p_operador_comparacion','analizador_sintactico.py',145),
  ('hash_declaration -> HASH LEFT_COR values RIGHT_COR','hash_declaration',4,'p_hash_declaration','analizador_sintactico.py',159),
  ('hash_declaration -> HASH LEFT_COR RIGHT_COR','hash_declaration',3,'p_hash_declaration','analizador_sintactico.py',160),
  ('hash_access -> variable LEFT_COR value RIGHT_COR','hash_access',4,'p_hash_access','analizador_sintactico.py',164),
  ('hash_operations -> hash_access ASSIGN value','hash_operations',3,'p_hash_operations','analizador_sintactico.py',168),
  ('while_statement -> WHILE condiciones COLON codigo','while_statement',4,'p_while_statement','analizador_sintactico.py',175),
  ('print_statement -> PUTS LEFT_PAR values RIGHT_PAR','print_statement',4,'p_print_statement','analizador_sintactico.py',181),
  ('boolean_expression -> expression GREATER_THAN expression','boolean_expression',3,'p_boolean_expression','analizador_sintactico.py',186),
  ('boolean_expression -> expression LESS_THAN expression','boolean_expression',3,'p_boolean_expression','analizador_sintactico.py',187),
  ('boolean_expression -> expression GREATER_THAN_EQUAL expression','boolean_expression',3,'p_boolean_expression','analizador_sintactico.py',188),
  ('boolean_expression -> expression LESS_THAN_EQUAL expression','boolean_expression',3,'p_boolean_expression','analizador_sintactico.py',189),
  ('boolean_expression -> expression EQUAL expression','boolean_expression',3,'p_boolean_expression','analizador_sintactico.py',190),
  ('boolean_expression -> expression NOT_EQUAL expression','boolean_expression',3,'p_boolean_expression','analizador_sintactico.py',191),
  ('boolean_expression -> BOOLEAN','boolean_expression',1,'p_boolean_expression','analizador_sintactico.py',192),
  ('expression -> INTEGER','expression',1,'p_expression','analizador_sintactico.py',195),
  ('expression -> FLOAT','expression',1,'p_expression','analizador_sintactico.py',196),
  ('expression -> variable','expression',1,'p_expression','analizador_sintactico.py',197),
  ('expression -> STRING','expression',1,'p_expression','analizador_sintactico.py',198),
  ('declaraciones -> declaracion_variable','declaraciones',1,'p_declaraciones','analizador_sintactico.py',202),
  ('declaraciones -> almacenar_resultado_condicional','declaraciones',1,'p_declaraciones','analizador_sintactico.py',203),
  ('declaraciones -> declaracion_estructura_datos','declaraciones',1,'p_declaraciones','analizador_sintactico.py',204),
  ('expresion -> puts','expresion',1,'p_expresion','analizador_sintactico.py',209),
  ('expresion -> gets','expresion',1,'p_expresion','analizador_sintactico.py',210),
  ('expresion -> print_statement','expresion',1,'p_expresion','analizador_sintactico.py',211),
  ('set_expression -> SET DOT NEW LEFT_PAR LEFT_COR values RIGHT_COR RIGHT_PAR','set_expression',8,'p_set_expression','analizador_sintactico.py',216),
  ('set_expression -> SET LEFT_COR values RIGHT_COR','set_expression',4,'p_set_expression','analizador_sintactico.py',217),
  ('set_operations -> set_expression','set_operations',1,'p_set_operations','analizador_sintactico.py',220),
  ('set_operations -> set_operations set_binary_operators set_expression','set_operations',3,'p_set_operations','analizador_sintactico.py',221),
  ('declaracion_estructura_datos -> LOCAL_VARIABLE ASSIGN set_expression','declaracion_estructura_datos',3,'p_set_declaration','analizador_sintactico.py',224),
  ('set_binary_operators -> PLUS','set_binary_operators',1,'p_set_binary_operators','analizador_sintactico.py',227),
  ('set_binary_operators -> MINUS','set_binary_operators',1,'p_set_binary_operators','analizador_sintactico.py',228),
  ('set_binary_operators -> AMPERSAND','set_binary_operators',1,'p_set_binary_operators','analizador_sintactico.py',229),
  ('set_binary_operators -> PIPE','set_binary_operators',1,'p_set_binary_operators','analizador_sintactico.py',230),
  ('set_binary_operators -> CARET','set_binary_operators',1,'p_set_binary_operators','analizador_sintactico.py',231),
  ('unless_expression -> UNLESS boolean_expression THEN expresion END','unless_expression',5,'p_unless_expression','analizador_sintactico.py',234),
  ('unless_expression -> UNLESS boolean_expression THEN expresion ELSE expresion END','unless_expression',7,'p_unless_expression','analizador_sintactico.py',235),
  ('expresion -> arithmetic_production','expresion',1,'p_arithmetic_expression','analizador_sintactico.py',238),
  ('arithmetic_production -> numero','arithmetic_production',1,'p_arithmetic_production','analizador_sintactico.py',241),
  ('arithmetic_production -> variable','arithmetic_production',1,'p_arithmetic_production','analizador_sintactico.py',242),
  ('arithmetic_production -> numero arithmetic_operators arithmetic_production','arithmetic_production',3,'p_arithmetic_production','analizador_sintactico.py',243),
  ('arithmetic_production -> variable arithmetic_operators arithmetic_production','arithmetic_production',3,'p_arithmetic_production','analizador_sintactico.py',244),
  ('arithmetic_operators -> PLUS','arithmetic_operators',1,'p_arithmetic_operators','analizador_sintactico.py',247),
  ('arithmetic_operators -> MINUS','arithmetic_operators',1,'p_arithmetic_operators','analizador_sintactico.py',248),
  ('arithmetic_operators -> MULTIPLY','arithmetic_operators',1,'p_arithmetic_operators','analizador_sintactico.py',249),
  ('arithmetic_operators -> DIVIDE','arithmetic_operators',1,'p_arithmetic_operators','analizador_sintactico.py',250),
  ('arithmetic_operators -> MODULO','arithmetic_operators',1,'p_arithmetic_operators','analizador_sintactico.py',251),
  ('arithmetic_operators -> EXPONENT','arithmetic_operators',1,'p_arithmetic_operators','analizador_sintactico.py',252),
  ('block_expression -> LBRACE expresion RBRACE','block_expression',3,'p_block_expression','analizador_sintactico.py',255),
  ('block_expression -> DO expresion END','block_expression',3,'p_block_expression','analizador_sintactico.py',256),
  ('block_expression -> LBRACE PIPE LOCAL_VARIABLE PIPE expresion RBRACE','block_expression',6,'p_block_expression','analizador_sintactico.py',257),
  ('block_expression -> DO PIPE LOCAL_VARIABLE PIPE expresion END','block_expression',6,'p_block_expression','analizador_sintactico.py',258),
  ('block_assignment -> llamada_metodo block_expression','block_assignment',2,'p_block_assignment','analizador_sintactico.py',261),
  ('proc_expression -> PROC DOT NEW block_expression','proc_expression',4,'p_proc_expression','analizador_sintactico.py',264),
  ('proc_assignment -> LOCAL_VARIABLE ASSIGN proc_expression','proc_assignment',3,'p_proc_assignment','analizador_sintactico.py',267),
  ('proc_call -> LOCAL_VARIABLE DOT CALL LEFT_PAR values RIGHT_PAR','proc_call',6,'p_proc_call','analizador_sintactico.py',270),
  ('proc_call -> LOCAL_VARIABLE DOT LEFT_PAR values RIGHT_PAR','proc_call',5,'p_proc_call','analizador_sintactico.py',271),
  ('proc_call -> LOCAL_VARIABLE LEFT_COR values RIGHT_COR','proc_call',4,'p_proc_call','analizador_sintactico.py',272),
  ('expresion -> condiciones_con_conectores','expresion',1,'p_condition_expr','analizador_sintactico.py',275),
]
