def missing_number(numbers):
  for num in range(0, len(numbers)+1):
    if num not in numbers:
      return num

nums_input = list(map(int, input().split(',')))
print(f'missing number is: {missing_number(nums_input)}')
