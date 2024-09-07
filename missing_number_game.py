def missing_number(numbers):
  for num in range(0, len(numbers)+1):
    if num not in numbers:
      return num

# Test 1: 
# all numbers are in the range [0,3]. 
# 2 is the missing number in the range since it does not appear in the list
print(f'missing number is: {missing_number([3,0,1])}')

# Test 2: 
print(f'missing number is: {missing_number([0,1])}')

# Test 3: 
print(f'missing number is: {missing_number([9,6,4,2,3,5,7,0,1])}')
