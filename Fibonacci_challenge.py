def fibonacci(number):
  if number == 0 or number == 1:
    return number
  else:
    return fibonacci(number - 1) + fibonacci(number - 2)

# Test 1: Fibonacci of 2 is 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1
print(f'result = {fibonacci(2)}')

# Test 2: Fibonacci of 3 is 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2
print(f'result = {fibonacci(3)}')

# Test 3: Fibonacci of 4 is 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3
print(f'result = {fibonacci(4)}')
