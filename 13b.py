def reverse_string(str1):
  str2 = ""
  for i in range(len(str1) - 1, -1, -1):
    str2 += str1[i]
  return str2



def test_reverse_string():
  assert (reverse_string("hello") == "olleh")==True
  assert (reverse_string("python") == "nohtyp")==True
  assert (reverse_string("12345") == "54321")==True
test_reverse_string()