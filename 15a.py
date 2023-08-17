file=open(input("Enter file name: "),'r')
Lines=file.readlines()
for line in range(len(Lines)):
   if(line==len(Lines)-1):
      print('{}'.format(Lines[line].strip()))
   else:
       print('{}'.format(Lines[line].strip()),end=";")