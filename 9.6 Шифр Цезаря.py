# put your python code here
n, text = int(input()), input()
for c in text:
   ch = ord(c)
   h1 = ch - 96
   if  h1 >= n:
       ch = ch - n
   else:
       ch = 122 - (n - h1)
   print(chr(ch), end='')