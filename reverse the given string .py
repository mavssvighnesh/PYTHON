class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

x=input("enter a string to get it's reversed")
print(py_solution().reverse_words(x))    