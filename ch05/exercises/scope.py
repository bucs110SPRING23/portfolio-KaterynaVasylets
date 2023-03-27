def multiply(num1, num2):
  
  result = 0

  for i in range(num2):
        result += num1
  return result
print (multiply (5, 4))
print (multiply (9, 100))

def power(base, exponent):
   
    
    result = 1
    for i in range(exponent):
        result *= base
    return result
print (power (5,7))

def square(num):
    return power(num, 2)
print (square(16))
