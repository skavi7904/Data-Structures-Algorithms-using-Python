# qn1
# x = [1,"abcd",2,"efgh",[3,4]]  # Statement 1
# y = x[0:6]                     # Statement 2
# z = x                          # Statement 3
# w = y                          # Statement 4
# x[1] = x[1][0:3] + 'd'         # Statement 5
# y[2] = 4                       # Statement 6
# z[1][1:3] = 'yzw'              # Statement 7
# z[0] = 0                       # Statement 8
# w[4][0] = 1000                 # Statement 9
# a = (x[4][1] == 4)             # Statement 10

#qn 2
# x = [423,'b',37,'f']
# u = x[1:]
# y = u
# w = x
# u = u[0:]
# u[1] = 53
# x[2] = 47
# print(x[2],y[1],w[2],u[1])

#qn 4
# def mystery(l):
#   l = l[0:5]
#   return()
# list1 = [44,71,12,8,23,17,16]
# mystery(list1)
# print(list1)

# x = [423,'b',37,'f']
# u = x[1:]
# y = u
# w = x
# u = u[0:]
# u[1] = 53
# x[2] = 47
# print(x[2] == 47, y[1] == 37, w[2] == 47, u[1] == 53)