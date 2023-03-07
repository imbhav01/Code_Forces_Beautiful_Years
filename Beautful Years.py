x = str(input())
y = []
for i in range(0,len(x)):
    y.append(int(x[i]))

for i in range(0,len(x)-1):
    if y[i]!=y[i+1]:
        for j in range(int(x),9000):
            a=j/1000
            b=(j/100)%10
            c=(j/10)%10
            d=j%10
            if a!=b:
                if a!=c:
                    if a!=d:
                        if b!=c:
                            if c!=d:
                                print(j)