import numpy as np
q=0.286
x=350
y=250
beta=100
alpha=45
seuil=1-y/x

Q = list()
for i in range(7):
    Q.append(seuil*np.random.rand(1)[0])
for i in range(14):
    Q.append(1 - seuil*np.random.rand(1)[0])
Q = sorted(Q)

# Defenders
U1=list()
U2=list()
U3=list()
# Attackers
D1=list()
D2=list()
D3=list()

for i in range(7):
    U1.append((1-Q[i])*(-x))
    U2.append(-(1-Q[i])*((x+beta)/2))
    X=((x*(1-Q[i]))-(y*(1-2*Q[i])))/(2*(x-y)*(1-Q[i]))
    a=X*(x-y)*(1-Q[i])*(-beta/x)
    b=((Q[i]*((x-beta)))/(2*x))*(-y)
    c=((x+beta)/(2*x))*(x-y)*(1-Q[i])
    D1.append(a+b+c)
    e=((x-beta)/x)*(x*(1-Q[i])-y)
    f=((1-Q[i])*(x-y)*(x*(1-Q[i])-y)*beta)/((x-y)*(1-Q[i])*x)
    D2.append(e+f)

for i in range(8,21):
    U3.append((1-Q[i])*(-beta))
    D3.append(0)
print(U1)
print(U2)
print(U3)
print(D1)
print(D2)
print(D3)
