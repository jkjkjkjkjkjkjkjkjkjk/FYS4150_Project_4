from numpy import *
from matplotlib.pyplot import *
import plotFunctions
import Py_Functions

'''
Uncomment the task that you want done.
'''

# 1 The most likely state
'''
n_ML = 100000000 #ML = Most likely
A_20_order = Py_Functions.readmatrices("../Results/Results_4c_order_N_%s_L_20.txt" % n_ML)[0]
print("Read ordered")
A_20_random = Py_Functions.readmatrices("../Results/Results_4c_random_N_%s_L_20.txt" % n_ML)[0]
print("Read random")

T_ML = [i for i in A_20_order[0]]
lst_ML = [A_20_order,A_20_random]

plotFunctions.plotMostLikelyState(lst_ML,T_ML,n_ML)
plotFunctions.plotAcceptedConfigurations(lst_ML,T_ML,n_ML)
'''

# 2 Probability distribution
"""
n_PD = 1000000000 #PD = Probability distribution
values = []

with open("../Results/Results_4d_N_%s_L_20.txt" % n_PD) as file:
    for line in file:
        if (line != "\n"):
            values.append(line.split())

T_PD = array([[float(i) for i in values[0]],[float(i) for i in values[1]]])
energies = array([[float(i) for i in values[2]],[float(i) for i in values[3]]])
variances = array([[float(i) for i in values[4]],[float(i) for i in values[5]]])
mean_energies = array([[float(i) for i in values[6]],[float(i) for i in values[7]]])

plotFunctions.plotProbabilityDistribution(energies,T_PD,variances,mean_energies,n_PD)
"""

# 3 Phase transition and critical temperature

n = 100
A_40_R_0 = Py_Functions.readmatrices("Results_4e_2_N_%s_L_40_R_0.txt" % n)[0]
A_40_R_1 = Py_Functions.readmatrices("Results_4e_2_N_%s_L_40_R_1.txt" % n)[0]
A_40_R_2 = Py_Functions.readmatrices("Results_4e_2_N_%s_L_40_R_2.txt" % n)[0]
A_40_R_3 = Py_Functions.readmatrices("Results_4e_2_N_%s_L_40_R_3.txt" % n)[0]
#print(A_40_R_0[1][:] + A_40_R_1[1][:] + A_40_R_2[1][:] + A_40_R_3[1][:])

A_40 = zeros(5)
print(A_40)
A_40_1 = A_40_R_0[0][:]
A_40_2 = A_40_R_0[1][:] + A_40_R_1[1][:] + A_40_R_2[1][:] + A_40_R_3[1][:]
A_40_3 = A_40_R_0[2][:] + A_40_R_1[2][:] + A_40_R_2[2][:] + A_40_R_3[2][:]
A_40_4 = A_40_R_0[3][:] + A_40_R_1[3][:] + A_40_R_2[3][:] + A_40_R_3[3][:]
A_40_5 = A_40_R_0[4][:] + A_40_R_1[4][:] + A_40_R_2[4][:] + A_40_R_3[4][:]
# ja dette gaar jo ikke siden elementene i A_40 ikke er arrays 
print("Read 40")
print(A_40_2)
E = []
Cv=[]
for i in range(len(A_40_1)):
	print A_40_2[i]	
	E.append(A_40_2[i][-1])
	Cv.append(A_40_5[i][-1])

plot(A_40_1,E)
show()

'''
A_60 = Py_Functions.readmatrices("Results_4e_2_N_s_L_60_R_0.txt")[0]
print("Read 60")
A_80 = Py_Functions.readmatrices("Results_4e_2_N_%s_L_80_R_0.txt" % n)[0]
print("Read 80")
A_100 = Py_Functions.readmatrices("Results_4e_2_N_%s_L_100_R_0.txt" % n)[0]
print("Read 100")
#T = [i[0] for i in A_40[0]]
#lst = [A_40,A_60,A_80,A_100]

#plotFunctions.plotPhaseTransition(lst,T,n)
'''
"""
#Finding critical temperature with max value of the Cv-plot
L = array([40,60,80,100])
T_c_values = zeros(len(L))
ind = 0
for i in range(len(L)):
    values = lst[-i][4][:,-1]
    max_value = amax(values)
    max_index = int(where(values == max_value)[0][0])
    T_c_values[ind] = T[max_index]
    ind += 1

coeffs = polyfit(L,T_c_values,1)

T_inf = coeffs[-1]

print("Critical temperature using max values of Cv: "+str(T_inf))
"""
