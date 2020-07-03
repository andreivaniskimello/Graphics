import numpy as np
import os
import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import scipy.linalg
import plotly
import plotly.graph_objs as go
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# IMPORT COST OF TRANSPORT INDIVIDUAL DATA
File_Path = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Kinetic_Geral.txt")
Data = pd.read_csv(File_Path,delimiter="\t",header = 0)
Rows = Data.shape[0]
Data_Array = np.array(Data)

Depth = Data_Array[:,0]
Speed = Data_Array[:,1]
Custo = Data_Array[:,2]
Drag = Data_Array[:,3]
GRF_V = Data_Array[:,4]
SUM_Drag_and_GRF_V = Data_Array[:,5]
Drag_per_Meter = Data_Array[:,6]

#  0.2 SPEED
File_Path_Two = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Kinetic_Geral_0.2.txt")
Data_Two = pd.read_csv(File_Path_Two,delimiter="\t",header = 0)
Data_Array_Two = np.array(Data_Two)

Depth_Two = Data_Array_Two[:,0]
Speed_Two = Data_Array_Two[:,1]
Custo_Two = Data_Array_Two[:,2]
Drag_Two = Data_Array_Two[:,3]
GRF_V_Two = Data_Array_Two[:,4]
SUM_Drag_and_GRF_V_Two = Data_Array_Two[:,5]
Drag_per_Meter_Two = Data_Array_Two[:,6]

#  0.4 SPEED
File_Path_Four = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Kinetic_Geral_0.4.txt")
Data_Four = pd.read_csv(File_Path_Four,delimiter="\t",header = 0)
Data_Array_Four = np.array(Data_Four)

Depth_Four = Data_Array_Four[:,0]
Speed_Four = Data_Array_Four[:,1]
Custo_Four = Data_Array_Four[:,2]
Drag_Four = Data_Array_Four[:,3]
GRF_V_Four = Data_Array_Four[:,4]
SUM_Drag_and_GRF_V_Four = Data_Array_Four[:,5]
Drag_per_Meter_Four = Data_Array_Four[:,6]

#  0.6 SPEED
File_Path_Six = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Kinetic_Geral_0.6.txt")
Data_Six = pd.read_csv(File_Path_Six,delimiter="\t",header = 0)
Data_Array_Six = np.array(Data_Six)

Depth_Six = Data_Array_Six[:,0]
Speed_Six = Data_Array_Six[:,1]
Custo_Six = Data_Array_Six[:,2]
Drag_Six = Data_Array_Six[:,3]
GRF_V_Six = Data_Array_Six[:,4]
SUM_Drag_and_GRF_V_Six = Data_Array_Six[:,5]
Drag_per_Meter_Six = Data_Array_Six[:,6]

#  0.8 SPEED
File_Path_Eight = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Kinetic_Geral_0.8.txt")
Data_Eight = pd.read_csv(File_Path_Eight,delimiter="\t",header = 0)
Data_Array_Eight = np.array(Data_Eight)

Depth_Eight = Data_Array_Eight[:,0]
Speed_Eight = Data_Array_Eight[:,1]
Custo_Eight = Data_Array_Eight[:,2]
Drag_Eight = Data_Array_Eight[:,3]
GRF_V_Eight = Data_Array_Eight[:,4]
SUM_Drag_and_GRF_V_Eight = Data_Array_Eight[:,5]
Drag_per_Meter_Eight = Data_Array_Eight[:,6]

# JOELHO
File_Path_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Kinetic_Geral_Joelho.txt")
Data_Joelho = pd.read_csv(File_Path_Joelho,delimiter="\t",header = 0)
Data_Array_Joelho = np.array(Data_Joelho)

Depth_Joelho = Data_Array_Joelho[:,0]
Speed_Joelho = Data_Array_Joelho[:,1]
Custo_Joelho = Data_Array_Joelho[:,2]
Drag_Joelho = Data_Array_Joelho[:,3]
GRF_V_Joelho = Data_Array_Joelho[:,4]
SUM_Drag_and_GRF_V_Joelho = Data_Array_Joelho[:,5]
Drag_per_Meter_Joelho = Data_Array_Joelho[:,6]

# JOELHO
File_Path_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Kinetic_Geral_Quadril.txt")
Data_Quadril = pd.read_csv(File_Path_Quadril,delimiter="\t",header = 0)
Data_Array_Quadril = np.array(Data_Quadril)

Depth_Quadril = Data_Array_Quadril[:,0]
Speed_Quadril = Data_Array_Quadril[:,1]
Custo_Quadril = Data_Array_Quadril[:,2]
Drag_Quadril = Data_Array_Quadril[:,3]
GRF_V_Quadril = Data_Array_Quadril[:,4]
SUM_Drag_and_GRF_V_Quadril = Data_Array_Quadril[:,5]
Drag_per_Meter_Quadril = Data_Array_Quadril[:,6]

# UMBIGO
File_Path_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Kinetic_Geral_Umbigo.txt")
Data_Umbigo = pd.read_csv(File_Path_Umbigo,delimiter="\t",header = 0)
Data_Array_Umbigo = np.array(Data_Umbigo)

Depth_Umbigo = Data_Array_Umbigo[:,0]
Speed_Umbigo = Data_Array_Umbigo[:,1]
Custo_Umbigo = Data_Array_Umbigo[:,2]
Drag_Umbigo = Data_Array_Umbigo[:,3]
GRF_V_Umbigo = Data_Array_Umbigo[:,4]
SUM_Drag_and_GRF_V_Umbigo = Data_Array_Umbigo[:,5]
Drag_per_Meter_Umbigo = Data_Array_Umbigo[:,6]

# XIFOIDE
File_Path_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Kinetic_Geral_Xifoide.txt")
Data_Xifoide = pd.read_csv(File_Path_Xifoide,delimiter="\t",header = 0)
Data_Array_Xifoide = np.array(Data_Xifoide)

Depth_Xifoide = Data_Array_Xifoide[:,0]
Speed_Xifoide = Data_Array_Xifoide[:,1]
Custo_Xifoide = Data_Array_Xifoide[:,2]
Drag_Xifoide = Data_Array_Xifoide[:,3]
GRF_V_Xifoide = Data_Array_Xifoide[:,4]
SUM_Drag_and_GRF_V_Xifoide = Data_Array_Xifoide[:,5]
Drag_per_Meter_Xifoide = Data_Array_Xifoide[:,6]





#Figure
fig, ax = plt.subplots()
fig.canvas.set_window_title('Cost of Transport and Drag_per_Meter INDIVIDUAL')

ax.scatter(GRF_V, Custo, cmap = 'rainbow')

ax.set_ylim([0, 12])
ax.set_title('Cost of Transport and Drag_per_Meter', fontsize=20)
ax.set_xlabel('Drag_per_Meter (N/m)', fontsize=18)
ax.set_ylabel('Cost of Transport (J/kg/m)', fontsize=16)
ax.tick_params(labelsize=14)
#ax.legend(loc = 'best', title = 'Depth', fontsize=14)


#Create and Plot Figure
fig, ax = plt.subplots(2, sharex=True)
fig.canvas.set_window_title('Cost of Transport and Drag_per_Meter INDIVIDUAL')
fig.suptitle('Cost of Transport and Drag_per_Meter', fontsize = 14)

ax[0].set_title('per Speed')
ax[0].set_ylabel('Cost (J/kg/m)',fontsize = 14)
#ax[0].set_xlabel('Drag_per_Meter (N)',fontsize = 12)
ax[0].grid(False)
ax[0].scatter(Drag_per_Meter_Two, Custo_Two, color='goldenrod', linewidth=2, label ='0.2 m/s')
ax[0].scatter(Drag_per_Meter_Four, Custo_Four, color='limegreen', linewidth=2, label ='0.4 m/s')
ax[0].scatter(Drag_per_Meter_Six, Custo_Six, color='mediumorchid', linewidth=2, label ='0.6 m/s')
ax[0].scatter(Drag_per_Meter_Eight, Custo_Eight, color='dodgerblue', linewidth=2, label ='0.8 m/s')
ax[0].legend(loc = 'best', title = 'Speeds', fontsize=14)

ax[1].set_title('per Depth')
ax[1].set_ylabel('Cost (J/kg/m)',fontsize = 14)
ax[1].set_xlabel('Drag_per_Meter (N)',fontsize = 12)
ax[1].grid(False)
ax[1].scatter(Drag_per_Meter_Joelho, Custo_Joelho, color='goldenrod', linewidth=2, label ='Knee')
ax[1].scatter(Drag_per_Meter_Quadril, Custo_Quadril, color='limegreen', linewidth=2, label ='Hip')
ax[1].scatter(Drag_per_Meter_Umbigo, Custo_Umbigo, color='mediumorchid', linewidth=2, label ='Umbilical')
ax[1].scatter(Drag_per_Meter_Xifoide, Custo_Xifoide, color='dodgerblue', linewidth=2, label ='Xiphoid')
ax[1].legend(loc = 'best', title = 'Speeds', fontsize=14)


plt.show()