import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

######## IMPORT FILES #######

#Open Umbilical Depth File
File_Path_Trunk_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Curves_DragForce_Segments/Planilha_Curva_DragForce_Trunk_Umbigo.txt")
Data_Trunk_Umbigo = pd.read_csv(File_Path_Trunk_Umbigo, delimiter="\t", header=0)
Data_Trunk_Umbigo_Array = np.array(Data_Trunk_Umbigo)

Umbigo_Speed_2 = Data_Trunk_Umbigo_Array[:,0]
Umbigo_Speed_4 = Data_Trunk_Umbigo_Array[:,1]
Umbigo_Speed_6 = Data_Trunk_Umbigo_Array[:,2]
Umbigo_Speed_8 = Data_Trunk_Umbigo_Array[:,3]
Umbigo_Speed_VAS = Data_Trunk_Umbigo_Array[:,4]


#Open Xiphoid Depth File
File_Path_Trunk_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Curves_DragForce_Segments/Planilha_Curva_DragForce_Trunk_Xifoide.txt")
Data_Trunk_Xifoide = pd.read_csv(File_Path_Trunk_Xifoide, delimiter="\t", header=0)
Data_Trunk_Xifoide_Array = np.array(Data_Trunk_Xifoide)

Xifoide_Speed_2 = Data_Trunk_Xifoide_Array[:,0]
Xifoide_Speed_4 = Data_Trunk_Xifoide_Array[:,1]
Xifoide_Speed_6 = Data_Trunk_Xifoide_Array[:,2]
Xifoide_Speed_8 = Data_Trunk_Xifoide_Array[:,3]
Xifoide_Speed_VAS = Data_Trunk_Xifoide_Array[:,4]

# Create Time Stride % Vector (0 - 100%)
Time_Stride = np.linspace(0,100,100)
Time_Stride = np.floor(Time_Stride)


####### PLOT GRAPHS #######

# Create and Plot Figure
fig, ax = plt.subplots(2, sharex=True)        #Create figure with 4 subplots (2 row, 2 columns)
fig.canvas.set_window_title('Drag Force TRUNK')                 #Set Figure Window Title
fig.suptitle('Drag Force on TRUNK', fontsize = 14)              #Set Figure Main Title

#Create common X axis for all subplots
fig.text(0.5, 0.04, '% of Stride', ha='center',fontsize = 14)
plt.xlim([0, 100])

# Umbilical Depth Subplot
ax[0].set_title('Umbilical Depth')
ax[0].set_ylabel('Drag Force (N)',fontsize = 14)
ax[0].set_ylim([-60, 1])
ax[0].plot(Time_Stride, Umbigo_Speed_2, linestyle= '-', color= 'indigo', linewidth=2)
ax[0].plot(Time_Stride, Umbigo_Speed_4, linestyle= '-', color= 'red', linewidth=2)
ax[0].plot(Time_Stride, Umbigo_Speed_6, linestyle= '-', color= 'goldenrod', linewidth=2)
ax[0].plot(Time_Stride, Umbigo_Speed_8, linestyle= '-', color= 'steelblue', linewidth=2)
ax[0].plot(Time_Stride, Umbigo_Speed_VAS, linestyle= '--', color= 'limegreen', linewidth=2)
    #Take-Off (Duty Factor)
ax[0].axvline(73.9, linestyle=':', color='indigo', linewidth=1.5)
ax[0].axvline(64.3, linestyle=':', color='red', linewidth=1.5)
ax[0].axvline(59.8, linestyle=':', color='goldenrod', linewidth=1.5)
ax[0].axvline(58.6, linestyle=':', color='steelblue', linewidth=1.5)
ax[0].axvline(62.9, linestyle=':', color='limegreen', linewidth=1.5)


# Xiphoid Depth Subplot
ax[1].set_title('Xiphoid Depth')
ax[1].set_ylim([-60, 1])
ax[1].plot(Time_Stride, Xifoide_Speed_2, linestyle= '-', color= 'indigo', linewidth=2)
ax[1].plot(Time_Stride, Xifoide_Speed_4, linestyle= '-', color= 'red', linewidth=2)
ax[1].plot(Time_Stride, Xifoide_Speed_6, linestyle= '-', color= 'goldenrod', linewidth=2)
ax[1].plot(Time_Stride, Xifoide_Speed_8, linestyle= '-', color= 'steelblue', linewidth=2)
ax[1].plot(Time_Stride, Xifoide_Speed_VAS, linestyle= '--', color= 'limegreen', linewidth=2)
    #Take-Off (Duty Factor)
ax[1].axvline(70.4, linestyle=':', color='indigo', linewidth=1.5)
ax[1].axvline(61.5, linestyle=':', color='red', linewidth=1.5)
ax[1].axvline(57, linestyle=':', color='goldenrod', linewidth=1.5)
ax[1].axvline(56.7, linestyle=':', color='steelblue', linewidth=1.5)
ax[1].axvline(61.7, linestyle=':', color='limegreen', linewidth=1.5)

#Figure Legend (it has to be after the subplots information)
line_labels = ['0.2 m/s','0.4 m/s','0.6 m/s', '0.8 m/s','VAS','TAKE-OFF']
fig.legend(labels = line_labels,
           loc = 'center left',
           title = 'Legend')

#fig.savefig("test.png")
plt.show()