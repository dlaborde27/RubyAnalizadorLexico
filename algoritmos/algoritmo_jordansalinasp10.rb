module Example
  def self.calculate
    a = 10
    b = 20
    unless a == b
      a += 1
      b **= 2
      result = a % b
    end
    if a != b
      puts "a is not equal to b"
    end
    range_inclusive = 1..10
    range_exclusive = 1...10
    if range_inclusive.include?(5)
      puts "5 is in the inclusive range"
    end
    if range_exclusive.include?(10)
      puts "10 is in the exclusive range"
    end
    case result
    when 0
      puts "Result is zero"
    else
      puts "Result is non-zero"
    end
    until result > 1000
      result *= 2
    end
    result %= 3
    puts "Final result: #{result}"
  end
  def self.check_defined
    if defined? (@@CLASS_VARIABLEiable)
      puts "Class variable is defined"
    end
  end
end
Example.calculate
Example.check_defined