end = "end"
    until result > 1000
      result *= 2
    end
    result %= 3
    puts "Final result: #{result}"
  end
  def self.check_defined
    if defined? (@@CLASS_VARIABLEiable)


mi_conjunto = Set.new([1, 2, 3, 4, 4])  # Los duplicados se eliminan automáticamente
puts mi_conjunto.inspect  # Salida: #<Set: {1, 2, 3, 4}>
# Agregar un elemento
mi_conjunto.add(4)
puts mi_conjunto.inspect  # Salida: #<Set: {1, 2, 3, 4}>

# Agregar múltiples elementos
mi_conjunto.merge([5, 6])
puts mi_conjunto.inspect  # Salida: #<Set: {1, 2, 3, 4, 5, 6}>

# Eliminar un elemento
mi_conjunto.delete(3)
puts mi_conjunto.inspect  # Salida: #<Set: {1, 2, 4, 5, 6}>
