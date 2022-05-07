def fibonacci(terms):
  n1 = 0
  n2 =  1
  count = 0
  if terms <= 0:
    return("number must be a positive integer")
  elif terms == 1:
    print("Fib seq up to ", terms,":", "\n", n1)
  else:
    print("Fib sequence:")
    while count < terms:
      print(n1)
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1
  

def fib(n):
  if n == 0 or n == 1:
    return n
  return fib(n-1) + fib(n-2)

for n in range(12):
  print(fib(n))
