def fibonacci(num):
    a=0
    b=1
    series=[]
    for i in range (1,num+1):
        series.append(a)
        c=a+b
        a=b
        b=c

    return series

print(fibonacci(5))
print(fibonacci(7))
