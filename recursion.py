#Direct Recursion
'''def fun(n):
    if n == 0:
        return
    print(n)
    fun(n - 1)

fun(5)'''


#Indirect Recursion

'''def fun1(n):
    if n > 0:
        print(n)
        fun2(n - 1)

def fun2(n):
    if n > 0:
        print(n)
        fun1(n - 1)

fun1(5)'''


