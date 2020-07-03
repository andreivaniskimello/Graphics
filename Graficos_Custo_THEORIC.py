# by André Ivaniski-Mello
# andreivaniskimello@gmail.com
# https://github.com/andreivaniskimello

import numpy as np
import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA



#THIS ROUTINE HAS 02 SECTIONS
    #1º) IMPORT AND PREPARE MATRIX OF COST OF TRANSPORT EXPERIMENTAL AND THEORIC (INDIVIDUAL DATA)
    #2º) FIGURES
        #FIGURE 01: COST EXPERIMENTAL AND THEORIC



#1º)IMPORT AND PREPARE MATRIX OF COST OF TRANSPORT EXPERIMENTAL AND THEORIC (INDIVIDUAL DATA)

    #PROFUNDIDADE: JOELHO
File_Path_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_THEORY_Geral_Joelho.txt")
Data_Joelho = pd.read_csv(File_Path_Joelho,delimiter="\t",header = 0)
Data_Array_Joelho = np.array(Data_Joelho)

Speed_Joelho = Data_Array_Joelho[:,0]
Cost_Experimental_Joelho = Data_Array_Joelho[:,1]
Work_Total_Joelho = Data_Array_Joelho[:,2]
Net_Work_Total_Joelho = Data_Array_Joelho[:,3]
Cost_Theory_Joelho = Data_Array_Joelho[:,4]
Ratio_Cost_TheoryExperimental_Joelho = Data_Array_Joelho[:,5]


    #PROFUNDIDADE: QUADRIL
File_Path_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_THEORY_Geral_Quadril.txt")
Data_Quadril = pd.read_csv(File_Path_Quadril,delimiter="\t",header = 0)
Data_Array_Quadril = np.array(Data_Quadril)

Speed_Quadril = Data_Array_Quadril[:,0]
Cost_Experimental_Quadril = Data_Array_Quadril[:,1]
Work_Total_Quadril = Data_Array_Quadril[:,2]
Net_Work_Total_Quadril = Data_Array_Quadril[:,3]
Cost_Theory_Quadril = Data_Array_Quadril[:,4]
Ratio_Cost_TheoryExperimental_Quadril = Data_Array_Quadril[:,5]

    #PROFUNDIDADE: UMBIGO
File_Path_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_THEORY_Geral_Umbigo.txt")
Data_Umbigo = pd.read_csv(File_Path_Umbigo,delimiter="\t",header = 0)
Data_Array_Umbigo = np.array(Data_Umbigo)

Speed_Umbigo = Data_Array_Umbigo[:,0]
Cost_Experimental_Umbigo = Data_Array_Umbigo[:,1]
Work_Total_Umbigo = Data_Array_Umbigo[:,2]
Net_Work_Total_Umbigo = Data_Array_Umbigo[:,3]
Cost_Theory_Umbigo = Data_Array_Umbigo[:,4]
Ratio_Cost_TheoryExperimental_Umbigo = Data_Array_Umbigo[:,5]


    #PROFUNDIDADE: XIFOIDE
File_Path_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_THEORY_Geral_Xifoide.txt")
Data_Xifoide = pd.read_csv(File_Path_Xifoide,delimiter="\t",header = 0)
Data_Array_Xifoide = np.array(Data_Xifoide)

Speed_Xifoide = Data_Array_Xifoide[:,0]
Cost_Experimental_Xifoide = Data_Array_Xifoide[:,1]
Work_Total_Xifoide = Data_Array_Xifoide[:,2]
Net_Work_Total_Xifoide = Data_Array_Xifoide[:,3]
Cost_Theory_Xifoide = Data_Array_Xifoide[:,4]
Ratio_Cost_TheoryExperimental_Xifoide = Data_Array_Xifoide[:,5]


#Total Arrays
Cost_Theory = np.append(Cost_Theory_Joelho, Cost_Theory_Quadril)
Cost_Theory = np.append(Cost_Theory, Cost_Theory_Umbigo)
Cost_Theory = np.append(Cost_Theory, Cost_Theory_Xifoide)

Cost_Experimental = np.append(Cost_Experimental_Joelho, Cost_Experimental_Quadril)
Cost_Experimental = np.append(Cost_Experimental, Cost_Experimental_Umbigo)
Cost_Experimental = np.append(Cost_Experimental, Cost_Experimental_Xifoide)

Cost_Theory_withoutKnee = np.append(Cost_Theory_Quadril, Cost_Theory_Umbigo)
Cost_Theory_withoutKnee = np.append(Cost_Theory_withoutKnee, Cost_Theory_Xifoide)

Cost_Experimental_withoutKnee = np.append(Cost_Experimental_Quadril, Cost_Experimental_Umbigo)
Cost_Experimental_withoutKnee = np.append(Cost_Experimental_withoutKnee, Cost_Experimental_Xifoide)

#Regression Lines
coef_withoutKnee,error_withoutKnee,_,_,_ = np.polyfit(Cost_Experimental_withoutKnee,Cost_Theory_withoutKnee,1, full=True)
poly1d_fn_withoutKnee = np.poly1d(coef_withoutKnee)

coef,error,_,_,_ = np.polyfit(Cost_Experimental, Cost_Theory,1, full=True)
poly1d_fn = np.poly1d(coef)

print(coef_withoutKnee)
print(error_withoutKnee)
print(coef)
print(error)
#2º)FIGURES

#Figure 1:
#fig, ax = plt.subplots()
#fig.canvas.set_window_title('Cost of Transport Experimental and Theoric')
#ax.scatter(Cost_Experimental, Cost_Theory, color='goldenrod', label = 'Cost Individual Data')
#plt.plot(Cost_Experimental_withoutKnee, poly1d_fn_withoutKnee(Cost_Experimental_withoutKnee),linestyle = '-' ,color='black', linewidth=3.0, label = 'Regression without Knee')
#plt.plot(Cost_Experimental, poly1d_fn(Cost_Experimental), linestyle = '--', color = 'silver',  linewidth=3.0, label = 'Regression with Knee')

#ax.set_ylim([0, 12])
#fig.suptitle('Cost of Transport', fontsize=20)
#plt.xlabel('Experimental (J/kg/m)', fontsize=18)
#plt.ylabel('Theory (J/kg/m)', fontsize=16)
#ax.tick_params(labelsize=14)
#plt.legend(loc = 'best', fontsize=14)

#Figure 2:
fig, ax = plt.subplots()
fig.canvas.set_window_title('Cost of Transport Experimental and Theoric per Depth')
ax.scatter(Cost_Experimental_Joelho, Cost_Theory_Joelho, color='goldenrod', linewidth=2, label ='Knee')
ax.scatter(Cost_Experimental_Quadril, Cost_Theory_Quadril, color='limegreen', linewidth=2, label ='Hip')
ax.scatter(Cost_Experimental_Umbigo, Cost_Theory_Umbigo, color='mediumorchid', linewidth=2, label ='Umbilical')
ax.scatter(Cost_Experimental_Xifoide, Cost_Theory_Xifoide, color='dodgerblue', linewidth=2, label ='Xiphoid')
plt.plot(Cost_Experimental_withoutKnee, poly1d_fn_withoutKnee(Cost_Experimental_withoutKnee),linestyle = '-' ,color='black', linewidth=3.0, label = 'Regression without Knee')
plt.plot(Cost_Experimental, poly1d_fn(Cost_Experimental), linestyle = '--', color = 'silver',  linewidth=3.0, label = 'Regression with Knee')

fig.suptitle('Cost of Transport per Depth', fontsize=20)
plt.xlabel('Experimental (J/kg/m)', fontsize=18)
plt.ylabel('Theory (J/kg/m)', fontsize=16)
ax.tick_params(labelsize=14)
plt.legend(loc = 'best', title = 'Depths', fontsize=14)


#Figure 3:
fig, ax = plt.subplots()
fig.canvas.set_window_title('Cost of Transport Experimental and Net Total Work per Depth')
ax.scatter(Cost_Experimental_Joelho, Net_Work_Total_Joelho, color='goldenrod', linewidth=2, label ='Knee')
ax.scatter(Cost_Experimental_Quadril, Net_Work_Total_Quadril, color='limegreen', linewidth=2, label ='Hip')
ax.scatter(Cost_Experimental_Umbigo, Net_Work_Total_Umbigo, color='mediumorchid', linewidth=2, label ='Umbilical')
ax.scatter(Cost_Experimental_Xifoide, Net_Work_Total_Xifoide, color='dodgerblue', linewidth=2, label ='Xiphoid')

fig.suptitle('Cost of Transport per Depth', fontsize=20)
plt.xlabel('Experimental (J/kg/m)', fontsize=18)
plt.ylabel('Net_Work_Total (J/kg/m)', fontsize=16)
ax.tick_params(labelsize=14)
plt.legend(loc = 'best', title = 'Depths', fontsize=14)

plt.show()
