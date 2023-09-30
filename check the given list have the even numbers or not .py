def even_numbers(nums):
  """Return True if all numbers in list are even."""
  for num in nums:
    if num % 2 != 0:
      return False
  return True


def test_even_numbers():
  """Test the even_numbers function."""
  t=True
  f=False
  assert even_numbers([2, 4, 6, 8]) == t
  assert even_numbers([1, 3, 5, 7]) == t
test_even_numbers()
