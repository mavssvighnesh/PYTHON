# This is a Python module to find Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)
