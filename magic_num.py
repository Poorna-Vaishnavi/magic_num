def magic(a):
 while(a >= 10):
   res = 0
   while a > 0:
      rem = a % 10
      res += rem
      a//=10
   a = res
 if a==1:
      return 1
 else:
      return 0   


a=int(input())
print(magic(a))