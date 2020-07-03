import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

####### IMPORT FILES ######

#Open Knee Depth File
File_Path_Foot_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Curves_DragForce_Segments/Planilha_Curva_DragForce_Foot_Joelho.txt")
Data_Foot_Joelho = pd.read_csv(File_Path_Foot_Joelho, delimiter="\t", header = 0)
Data_Foot_Joelho_Array = np.array(Data_Foot_Joelho)

Joelho_Speed_2 = Data_Foot_Joelho_Array[:,0]
Joelho_Speed_4 = Data_Foot_Joelho_Array[:,1]
Joelho_Speed_6 = Data_Foot_Joelho_Array[:,2]
Joelho_Speed_8 = Data_Foot_Joelho_Array[:,3]
Joelho_Speed_VAS = Data_Foot_Joelho_Array[:,4]


#Open Hip Depth File
File_Path_Foot_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Curves_DragForce_Segments/Planilha_Curva_DragForce_Foot_Quadril.txt")
Data_Foot_Quadril = pd.read_csv(File_Path_Foot_Quadril,delimiter="\t",header = 0)
Data_Foot_Quadril_Array = np.array(Data_Foot_Quadril)

Quadril_Speed_2 = Data_Foot_Quadril_Array[:,0]
Quadril_Speed_4 = Data_Foot_Quadril_Array[:,1]
Quadril_Speed_6 = Data_Foot_Quadril_Array[:,2]
Quadril_Speed_8 = Data_Foot_Quadril_Array[:,3]
Quadril_Speed_VAS = Data_Foot_Quadril_Array[:,4]


#Open Umbilical Depth File
File_Path_Foot_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Curves_DragForce_Segments/Planilha_Curva_DragForce_Foot_Umbigo.txt")
Data_Foot_Umbigo = pd.read_csv(File_Path_Foot_Umbigo,delimiter="\t",header = 0)
Data_Foot_Umbigo_Array = np.array(Data_Foot_Umbigo)

Umbigo_Speed_2 = Data_Foot_Umbigo_Array[:,0]
Umbigo_Speed_4 = Data_Foot_Umbigo_Array[:,1]
Umbigo_Speed_6 = Data_Foot_Umbigo_Array[:,2]
Umbigo_Speed_8 = Data_Foot_Umbigo_Array[:,3]
Umbigo_Speed_VAS = Data_Foot_Umbigo_Array[:,4]


#Open Xiphoid Depth File
File_Path_Foot_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Curves_DragForce_Segments/Planilha_Curva_DragForce_Foot_Xifoide.txt")
Data_Foot_Xifoide = pd.read_csv(File_Path_Foot_Xifoide,delimiter="\t",header = 0)
Data_Foot_Xifoide_Array = np.array(Data_Foot_Xifoide)

Xifoide_Speed_2 = Data_Foot_Xifoide_Array[:,0]
Xifoide_Speed_4 = Data_Foot_Xifoide_Array[:,1]
Xifoide_Speed_6 = Data_Foot_Xifoide_Array[:,2]
Xifoide_Speed_8 = Data_Foot_Xifoide_Array[:,3]
Xifoide_Speed_VAS = Data_Foot_Xifoide_Array[:,4]

# Create Time Stride % Vector (0 - 100%)
Time_Stride = np.linspace(0,100,100)
Time_Stride = np.floor(Time_Stride)


####### PLOT GRAPHS #######

# Create and Plot Figure
fig, ax = plt.subplots(2,2, sharex=True, sharey= 'row')        #Create figure with 4 subplots (2 row, 2 columns)
fig.canvas.set_window_title('Drag Force FOOT')                 #Set Figure Window Title
fig.suptitle('Drag Force on FOOT', fontsize = 14)              #Set Figure Main Title

#Create common X axis for all subplots
fig.text(0.5, 0.04, '% of Stride', ha='center',fontsize = 14)
plt.xlim([0, 100])

# Knee Depth Subplot
ax[0,0].set_title('Knee Depth')
ax[0,0].set_ylabel('Drag Force (N)',fontsize = 14)
ax[0,0].set_ylim([-20, 1])
ax[0,0].grid(False)
ax[0,0].plot(Time_Stride, Joelho_Speed_2, linestyle= '-', color= 'indigo', linewidth=2)
ax[0,0].plot(Time_Stride, Joelho_Speed_4, linestyle= '-', color= 'red', linewidth=2)
ax[0,0].plot(Time_Stride, Joelho_Speed_6, linestyle= '-', color= 'goldenrod', linewidth=2)
ax[0,0].plot(Time_Stride, Joelho_Speed_8, linestyle= '-', color= 'steelblue', linewidth=2)
ax[0,0].plot(Time_Stride, Joelho_Speed_VAS, linestyle= '--', color= 'limegreen', linewidth=2)
    #Take-Off (Duty Factor)
ax[0,0].axvline(75.5, linestyle=':', color='indigo', linewidth=1.5)
ax[0,0].axvline(67, linestyle=':', color='red', linewidth=1.5)
ax[0,0].axvline(63.6, linestyle=':', color='goldenrod', linewidth=1.5)
ax[0,0].axvline(62.3, linestyle=':', color='steelblue', linewidth=1.5)
ax[0,0].axvline(62.7, linestyle=':', color='limegreen', linewidth=1.5)


# Hip Depth Subplot
ax[0,1].set_title('Hip Depth')
ax[0,1].set_ylim([-20, 1])
ax[0,1].plot(Time_Stride, Quadril_Speed_2, linestyle= '-', color= 'indigo', linewidth=2)
ax[0,1].plot(Time_Stride, Quadril_Speed_4, linestyle= '-', color= 'red', linewidth=2)
ax[0,1].plot(Time_Stride, Quadril_Speed_6, linestyle= '-', color= 'goldenrod', linewidth=2)
ax[0,1].plot(Time_Stride, Quadril_Speed_8, linestyle= '-', color= 'steelblue', linewidth=2)
ax[0,1].plot(Time_Stride, Quadril_Speed_VAS, linestyle= '--', color= 'limegreen', linewidth=2)
    #Take-Off (Duty Factor)
ax[0,1].axvline(73.5, linestyle=':', color='indigo', linewidth=1.5)
ax[0,1].axvline(65.7, linestyle=':', color='red', linewidth=1.5)
ax[0,1].axvline(61.9, linestyle=':', color='goldenrod', linewidth=1.5)
ax[0,1].axvline(60.9, linestyle=':', color='steelblue', linewidth=1.5)
ax[0,1].axvline(62.7, linestyle=':', color='limegreen', linewidth=1.5)


# Umbilical Depth Subplot
ax[1,0].set_title('Umbilical Depth')
ax[1,0].set_ylabel('Drag Force (N)',fontsize = 14)
ax[1,0].set_ylim([-25, 1])
ax[1,0].plot(Time_Stride, Umbigo_Speed_2, linestyle= '-', color= 'indigo', linewidth=2)
ax[1,0].plot(Time_Stride, Umbigo_Speed_4, linestyle= '-', color= 'red', linewidth=2)
ax[1,0].plot(Time_Stride, Umbigo_Speed_6, linestyle= '-', color= 'goldenrod', linewidth=2)
ax[1,0].plot(Time_Stride, Umbigo_Speed_8, linestyle= '-', color= 'steelblue', linewidth=2)
ax[1,0].plot(Time_Stride, Umbigo_Speed_VAS, linestyle= '--', color= 'limegreen', linewidth=2)
    #Take-Off (Duty Factor)
ax[1,0].axvline(73.9, linestyle=':', color='indigo', linewidth=1.5)
ax[1,0].axvline(64.3, linestyle=':', color='red', linewidth=1.5)
ax[1,0].axvline(59.8, linestyle=':', color='goldenrod', linewidth=1.5)
ax[1,0].axvline(58.6, linestyle=':', color='steelblue', linewidth=1.5)
ax[1,0].axvline(62.9, linestyle=':', color='limegreen', linewidth=1.5)


# Xiphoid Depth Subplot
ax[1,1].set_title('Xiphoid Depth')
ax[1,1].set_ylim([-25, 1])
ax[1,1].plot(Time_Stride, Xifoide_Speed_2, linestyle= '-', color= 'indigo', linewidth=2)
ax[1,1].plot(Time_Stride, Xifoide_Speed_4, linestyle= '-', color= 'red', linewidth=2)
ax[1,1].plot(Time_Stride, Xifoide_Speed_6, linestyle= '-', color= 'goldenrod', linewidth=2)
ax[1,1].plot(Time_Stride, Xifoide_Speed_8, linestyle= '-', color= 'steelblue', linewidth=2)
ax[1,1].plot(Time_Stride, Xifoide_Speed_VAS, linestyle= '--', color= 'limegreen', linewidth=2)
    #Take-Off (Duty Factor)
ax[1,1].axvline(70.4, linestyle=':', color='indigo', linewidth=1.5)
ax[1,1].axvline(61.5, linestyle=':', color='red', linewidth=1.5)
ax[1,1].axvline(57, linestyle=':', color='goldenrod', linewidth=1.5)
ax[1,1].axvline(56.7, linestyle=':', color='steelblue', linewidth=1.5)
ax[1,1].axvline(61.7, linestyle=':', color='limegreen', linewidth=1.5)


#Figure Legend (it has to be after the subplots information)
line_labels = ['0.2 m/s','0.4 m/s','0.6 m/s', '0.8 m/s','VAS','TAKE-OFF']
fig.legend(labels = line_labels,
           loc = 'center left',
           title = 'Legend')

#fig.savefig("test.png")
plt.show()
