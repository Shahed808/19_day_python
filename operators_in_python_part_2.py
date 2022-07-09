''' Note : But in c and java languages they used symbols to represent the logical operators
      Bitwise operators are used symbols to represent it'''

'''Relational/ comparision operators'''

# a = int(input("Enter the value of a: "))                                    # 10
# b = int(input("Enter the value of b: "))                                    # 15
# print(f"The value of {a} > {b} is {a>b}")                                   # False                                      
# print(f"The value of {a} < {b} is {a<b}")                                   # True
# print(f"The value of {a} <= {b} is {a<=b}")                                  # True
# print(f"The value of {a} >= {b} is {a>=b}")                                  # False
# print(f"The value of {a} != {b} is {a!=b}")                                  # True
# print(f"The value of {a} == {b} is {a==b}")                                  # False



# a = int(input("Enter the value of a :"))
# b = int(input("Enter the value of b :"))
# print("The value of %d<%d=%d"%(a,b,a<b))
# print("The value of a=%d < b=%d and a<b = %d"%(a,b,a<b))                            # 1
# print("The value of a=%d > b=%d and a>b = %d"%(a,b,a>b))                            # 0
# print("The value of a=%d <= b=%d and a<=b = %d"%(a,b,a<=b))                         # 1
# print("The value of a=%d >= b=%d and a>=b = %d"%(a,b,a>=b))                         # 0                       
# print("The value of a=%d != b=%d and a!=b = %d"%(a,b,a!=b))                         # 1
# print("The value of a=%d == b=%d and a==b = %d"%(a,b,a==b))                         # 0


''' logical operator used words to represent'''

# a =int(input("Enter the value of a :"))                                         # 5
# b =int(input("Enter the value of b :"))                                         # 7
# print("The value of a<b and b<a is {}".format(a<b,b<a))                         # True
# print("The value of a>b and b>a is {}".format(a>b,b>a))                         # False
# print("The value of a!=b and b==a is {}".format(a!=b,b==a))                         # True
# print("The value of a!=b and a<=b is {}".format(a!=b,a<=b))                         # True
# print("The value of a==b and a>=b is {}".format(a==b,a>=b))                         # False
# print("The value of a==b and a<=b is {}".format(a==b,a<=b))                             # False
# print("The value of a!=b and a>=b is {}".format(a!=b,a>=b))                             # True
# print("The value of a<b or b<a is {}".format(a<b,b<a))                                    #True
# print("The value of a>b or b>a is {}".format(a>b,b>a))                                    # False
# print("The opposite of {}=={} is {}".format(a,b,not a==b))                                  # True
# print("The opposite of {}!={} is {}".format(a,b,not a!=b))                                  # False

# a = True
# b = False
# print(a or b)
# print(b or a)


''' bitwise operator uses symbols to represent (&-and, |-or)'''

# x = int(input("Enter the value of a :"))                                            # 9
# y = int(input("Enter the value of b :"))                                            # 11
# print("The value of {} & {} is {}".format(x,y,x&y))                                 # 9
# print("The value of {} | {} is {}".format(x,y,x|y))                                 # 11

# print(0b1001)


'''identity operators
if the id are same we will get the value as same or it will get different'''

# a= 35.5
# b=35.0

# if a is b:
#     print("a and b have the same identity")
# else :
#     print("a and b do not have same identity")                              # a and b do not have same identity

# print(id(a))
# print(id(b))

# a =16
# b=4*4

# if id(a)==id(b):
#     print("a and b have the same identity ")
# else:
#     print("a and b do not have the same identity")                          # a and b have the same identity 


# w = (input("Enter the value of w :"))                                        # doubt session(10)
# print(type(w) is int)                                                           # False (True)
# print(type(w) is not float)                                                     # True
# print(type(w) is float)                                                         # False


# x = input("Enter the value of x :")
# print(type(x) is float)                                                     # False (True)
# print(type(x) is not float)                                                 # True  (False)
# print(type(x) is int)                                                       # False

'''membership operator'''

# l1=['bob','sam','atharv','shri','bablu','angi',
# 'lalu','buddy','carrie','alex','ravi','babu']

# print('alex' in l1)                                                               # True
# print('sham' in l1)                                                               # False
# print('bobby' in l1)                                                              # False
# print('sam' in l1)                                                                # True


# t1='bob','sam','atharv','shri','bablu','angi',
# 'lalu','buddy','carrie','alex','ravi','babu'

# print('carrie' in t1)                                                               # False


# s1 = {'bob','sam','atharv','shri','bablu','angi',
# 'lalu','buddy','carrie','alex','ravi','babu'}

# print("danny" in s1)                                                                # False
# print("anny"  not in s1 )                                                           # True
# print("carrie"  not in s1 )                                                         # False

# l1=['bob','sam','atharv','shri','bablu','angi',
# 'Lalu','buddy','Carrie','alex','ravi','Babu']
# l1.sort()
# print(l1)                                                                            # ['Babu', 'Carrie', 'Lalu', 'alex', 'angi', 'atharv', 'bablu', 'bob', 'buddy', 'ravi', 'sam', 'shri']


# l2 = ['p','e','o','W','t','Y']
# l2.sort()
# print(l2)                                                                   # ['W', 'Y', 'e', 'o', 'p', 't']

# l2.sort(reverse=True)
# print(*l2)                                                                     # t p o e Y W (* will exclude brackets and comas)


# for i in l2:
#     print(i,end=" ")                                                          # t p o e Y W 


''' shift operator is (>>-/2) and (<<*2) '''

# a = int(input("Enter the value of a : "))
# print(a>>1)                                                             # 15
# print(a>>2)                                                             # 7
# print(a>>3)                                                             # 3
# print(a>>4)                                                             # 1


# o = int(input("Enter the value of o : "))
# print(o<<1)                                                               # 72
# print(o<<2)                                                                 # 144
# print(o<<3)                                                               # 288


