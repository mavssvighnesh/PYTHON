file1 = open('ftemps.txt', 'w')
temp = [int(line.strip()) for line in open('temps.txt', 'r')]
for t in temp:
    print(t*9/5+32, file=file1)
file1.close()