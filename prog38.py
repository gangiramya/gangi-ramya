a=input()
l=list(map(int,a.split(' ')))
t=l[0]
u=l[1]
t=t^u
u=t^u
t=t^u
print(t,u)
