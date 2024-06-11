
def fun1(u,v):
    for r in range(len(u)+1):
        fun[r][len(v)+1] = 0  #row
    for c in range(len(v)+1):
        fun[len(u)+1][c] = 0  #col
    max = 0
    for c in range(len(v)+1,-1,-1):
        for r in range(len(u)+1,-1,-1):
            if u[r] == v[c]:
                fun[r][c] = 1 + fun[r+1][c+1]
            else:
                fun[r][c] = 0
            if fun[r][c] > max:
                max = fun[r][c]
            return max

fun={}
print(fun1("kavi","amrkaveen"))