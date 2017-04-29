#Reshma Bhatia (USC ID: 8959806814)
import numpy as np
from cvxopt import matrix,solvers
coord=[]
vals=[]
with open("linsep.txt", "r") as file:
	for line in file:
		templine=line.split(",")
		tempcord=[]
		tempcord.append(float(templine[0]))
		tempcord.append(float(templine[1]))
		coord.append(tempcord)
		vals.append(float(templine[2]))

#print (coord)
#print (vals)
coord=np.array(coord)
vals=np.array(vals)
vals=np.resize(vals,(100,1))
#print (coord)
#print (vals)

P = matrix(np.dot(coord, coord.T)* np.dot(vals, vals.T))
q = matrix(np.ones(100) * -1)
G = matrix(np.diag(np.ones(100) * -1))
h= matrix(np.zeros(100))
b = matrix([0.0])
A = matrix(vals.T, (1,100))
sol = solvers.qp(P, q, G, h, A, b)
alpha = sol['x']
#print (alpha)
weight=0.0
for i in range(100):
    weight+=alpha[i]*vals[i]*coord[i]
print ('weight=',weight)
fcoord=[]
falpha=[]
fval=[]
for i in range(100):
    if (alpha[i]>0.0001):
        falpha.append(alpha[i])
        fcoord.append(coord[i])
        fval.append(vals[i])
#print (fcoord)
print ("alpha=",falpha)
b= (1/fval[0])-np.dot(weight , fcoord[0])
print ('b=', b)