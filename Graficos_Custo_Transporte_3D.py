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

#THIS ROUTINE HAS XX SECTIONS
    #1º) IMPORT COST OF TRANSPORT INDIVIDUAL DATA
    #2º) IMPORT PREPARE MATRIX OF VAS DATA
    #3º) IMPORT PREPARE MATRIX OF DEPTH IN METERS DATA
    #4º) IMPORT PREPARE MATRIX OF DEPTH IN STATURE PERCENTUAL DATA
    # 5º) IMPORT AND PREPARE MATRIX OF TOTAL MEAN DATA COST OF TRANSPORT
    #6º)  TOTAL SUM FORCES (DRAG FORCE AND GRF_V_MEAN)
    #7º) FIGURES
    #FIGURE 1: FIGURE 3D OF INDIVIDUAL DATA OF COST OF TRANSPORT
    #FIGURE 2: FIGURE 3D OF TOTAL COST OF TRANSPORT MEAN DATA


#1º) IMPORT COST OF TRANSPORT INDIVIDUAL DATA
File_Path = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Geral.txt")
Data = pd.read_csv(File_Path,delimiter="\t",header = 0)
Rows = Data.shape[0]
Data_Array = np.array(Data)

#2º) IMPORT VAS DATA
File_Path_VAS = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/VAS_Mean.txt")
Data_VAS  = pd.read_csv(File_Path_VAS,delimiter="\t",header = 0)
Data_Array_VAS = np.array(Data_VAS)

VAS_Joelho = Data_Array_VAS [0,1]
VAS_Joelho_CIUpper = Data_Array_VAS[0,4]
VAS_Joelho_CI = VAS_Joelho_CIUpper - VAS_Joelho

VAS_Quadril = Data_Array_VAS [1,1]
VAS_Quadril_CIUpper = Data_Array_VAS[1,4]
VAS_Quadril_CI = VAS_Quadril_CIUpper - VAS_Quadril

VAS_Umbigo = Data_Array_VAS [2,1]
VAS_Umbigo_CIUpper = Data_Array_VAS[1,4]
VAS_Umbigo_CI = VAS_Umbigo_CIUpper - VAS_Umbigo

VAS_Xifoide = Data_Array_VAS [3,1]
VAS_Xifoide_CIUpper = Data_Array_VAS[1,4]
VAS_Xifoide_CI = VAS_Xifoide_CIUpper - VAS_Xifoide

VAS_All_Depths_Mean = [VAS_Joelho, VAS_Quadril, VAS_Umbigo, VAS_Xifoide]
VAS_All_Depths_CI = [VAS_Joelho_CI, VAS_Quadril_CI, VAS_Umbigo_CI, VAS_Xifoide_CI]

#3º) IMPORT DEPTH IN METERS DATA
File_Path_DepthMeters = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Profundidade_in_Meters.txt")
Data_DepthMeters = pd.read_csv(File_Path_DepthMeters,delimiter="\t",header = 0)
Data_Array_DepthMeters = np.array(Data_DepthMeters)


DepthMeters_Joelho = Data_Array_DepthMeters [0,0]
DepthMeters_Quadril = Data_Array_DepthMeters [1,0]
DepthMeters_Umbigo = Data_Array_DepthMeters [2,0]
DepthMeters_Xifoide = Data_Array_DepthMeters [3,0]

Gravity_Joelho = Data_Array_DepthMeters [0,1]
Gravity_Quadril = Data_Array_DepthMeters [1,1]
Gravity_Umbigo = Data_Array_DepthMeters [2,1]
Gravity_Xifoide = Data_Array_DepthMeters [3,1]

DepthMeters_Joelho = (DepthMeters_Joelho, DepthMeters_Joelho, DepthMeters_Joelho, DepthMeters_Joelho)
DepthMeters_Quadril = (DepthMeters_Quadril, DepthMeters_Quadril, DepthMeters_Quadril, DepthMeters_Quadril)
DepthMeters_Umbigo = (DepthMeters_Umbigo, DepthMeters_Umbigo, DepthMeters_Umbigo, DepthMeters_Umbigo)
DepthMeters_Xifoide = (DepthMeters_Xifoide, DepthMeters_Xifoide, DepthMeters_Xifoide, DepthMeters_Xifoide)

DepthMeters_Total = np.append(DepthMeters_Joelho,DepthMeters_Quadril)
DepthMeters_Total = np.append(DepthMeters_Total,DepthMeters_Umbigo)
DepthMeters_Total = np.append(DepthMeters_Total,DepthMeters_Xifoide)

Gravity_Joelho = (Gravity_Joelho, Gravity_Joelho, Gravity_Joelho, Gravity_Joelho)
Gravity_Quadril = (Gravity_Quadril, Gravity_Quadril, Gravity_Quadril, Gravity_Quadril)
Gravity_Umbigo = (Gravity_Umbigo, Gravity_Umbigo, Gravity_Umbigo, Gravity_Umbigo)
Gravity_Xifoide = (Gravity_Xifoide, Gravity_Xifoide, Gravity_Xifoide, Gravity_Xifoide)

Gravity_Total = np.append(Gravity_Joelho,Gravity_Quadril)
Gravity_Total = np.append(Gravity_Total,Gravity_Umbigo)
Gravity_Total = np.append(Gravity_Total,Gravity_Xifoide)

#4º) IMPORT DEPTH IN STATURE PERCENTUAL DATA
File_Path_DepthPercentual = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Profundidade_in_Percentual_of_Stature.txt")
Data_DepthPercentual = pd.read_csv(File_Path_DepthPercentual,delimiter="\t",header = 0)
Data_Array_DepthPercentual = np.array(Data_DepthPercentual)

DepthPercentual_Joelho = Data_Array_DepthPercentual [0,1]
DepthPercentual_Quadril = Data_Array_DepthPercentual [1,1]
DepthPercentual_Umbigo = Data_Array_DepthPercentual [2,1]
DepthPercentual_Xifoide = Data_Array_DepthPercentual [3,1]

DepthPercentual_Joelho = (DepthPercentual_Joelho, DepthPercentual_Joelho, DepthPercentual_Joelho, DepthPercentual_Joelho)
DepthPercentual_Quadril = (DepthPercentual_Quadril, DepthPercentual_Quadril, DepthPercentual_Quadril, DepthPercentual_Quadril)
DepthPercentual_Umbigo = (DepthPercentual_Umbigo, DepthPercentual_Umbigo, DepthPercentual_Umbigo, DepthPercentual_Umbigo)
DepthPercentual_Xifoide = (DepthPercentual_Xifoide, DepthPercentual_Xifoide, DepthPercentual_Xifoide, DepthPercentual_Xifoide)

DepthPercentual_Total = np.append(DepthPercentual_Joelho,DepthPercentual_Quadril)
DepthPercentual_Total = np.append(DepthPercentual_Total,DepthPercentual_Umbigo)
DepthPercentual_Total = np.append(DepthPercentual_Total,DepthPercentual_Xifoide)

# 5º) IMPORT AND PREPARE MATRIX OF TOTAL MEAN DATA COST OF TRANSPORT
 #JOELHO CUSTO MEAN
File_Path_Custo_Mean_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Custo_Mean_Joelho.txt")
Data_Custo_Mean_Joelho = pd.read_csv(File_Path_Custo_Mean_Joelho,delimiter="\t",header = 0)
Data_Array_Custo_Mean_Joelho = np.array(Data_Custo_Mean_Joelho)

Speed_Joelho = Data_Array_Custo_Mean_Joelho[:,0]
Custo_Joelho = Data_Array_Custo_Mean_Joelho[:,1]
Custo_Joelho_CIUpper = Data_Array_Custo_Mean_Joelho[:,4]
Custo_Joelho_CI = Custo_Joelho_CIUpper - Custo_Joelho
Depth_Joelho = Data_Array_Custo_Mean_Joelho[:,5]

  #QUADRIL CUSTO MEAN
File_Path_Custo_Mean_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Custo_Mean_Quadril.txt")
Data_Custo_Mean_Quadril = pd.read_csv(File_Path_Custo_Mean_Quadril,delimiter="\t",header = 0)
Data_Array_Custo_Mean_Quadril = np.array(Data_Custo_Mean_Quadril)

Speed_Quadril = Data_Array_Custo_Mean_Quadril[:,0]
Custo_Quadril = Data_Array_Custo_Mean_Quadril[:,1]
Custo_Quadril_CIUpper = Data_Array_Custo_Mean_Quadril[:,4]
Custo_Quadril_CI = Custo_Quadril_CIUpper - Custo_Quadril
Depth_Quadril = Data_Array_Custo_Mean_Quadril[:,5]

 #UMBIGO CUSTO MEAN
File_Path_Custo_Mean_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Custo_Mean_Umbigo.txt")
Data_Custo_Mean_Umbigo = pd.read_csv(File_Path_Custo_Mean_Umbigo,delimiter="\t",header = 0)
Data_Array_Custo_Mean_Umbigo = np.array(Data_Custo_Mean_Umbigo)

Speed_Umbigo = Data_Array_Custo_Mean_Umbigo[:,0]
Custo_Umbigo = Data_Array_Custo_Mean_Umbigo[:,1]
Custo_Umbigo_CIUpper = Data_Array_Custo_Mean_Umbigo[:,4]
Custo_Umbigo_CI = Custo_Umbigo_CIUpper - Custo_Umbigo
Depth_Umbigo = Data_Array_Custo_Mean_Umbigo[:,5]

#XIFOIDE CUSTO MEAN
File_Path_Custo_Mean_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Custo_Mean_Xifoide.txt")
Data_Custo_Mean_Xifoide = pd.read_csv(File_Path_Custo_Mean_Xifoide,delimiter="\t",header = 0)
Data_Array_Custo_Mean_Xifoide = np.array(Data_Custo_Mean_Xifoide)

Speed_Xifoide = Data_Array_Custo_Mean_Xifoide[:,0]
Custo_Xifoide = Data_Array_Custo_Mean_Xifoide[:,1]
Custo_Xifoide_CIUpper = Data_Array_Custo_Mean_Xifoide[:,4]
Custo_Xifoide_CI = Custo_Xifoide_CIUpper - Custo_Xifoide
Depth_Xifoide = Data_Array_Custo_Mean_Xifoide[:,5]

#TOTAL MATRIX
Depth_Total = np.append(Depth_Joelho,Depth_Quadril)
Depth_Total = np.append(Depth_Total,Depth_Umbigo)
Depth_Total = np.append(Depth_Total,Depth_Xifoide)

Speed_Total = np.append(Speed_Joelho,Speed_Quadril)
Speed_Total = np.append(Speed_Total,Speed_Umbigo)
Speed_Total = np.append(Speed_Total,Speed_Xifoide)

Custo_Total = np.append(Custo_Joelho,Custo_Quadril)
Custo_Total = np.append(Custo_Total,Custo_Umbigo)
Custo_Total = np.append(Custo_Total,Custo_Xifoide)


Custo_Total_CI = np.append(Custo_Joelho_CI,Custo_Quadril_CI)
Custo_Total_CI = np.append(Custo_Total_CI,Custo_Umbigo_CI)
Custo_Total_CI = np.append(Custo_Total_CI,Custo_Xifoide_CI)


#6º)  TOTAL SUM FORCES (DRAG FORCE AND GRF_V_MEAN)

#JOELHO
File_Path_TOTAL_SUM_FORCES_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/TOTAL_SUM_FORCES_Drag_GRFVMean_Joelho.txt")
Data_TOTAL_SUM_FORCES_Joelho = pd.read_csv(File_Path_TOTAL_SUM_FORCES_Joelho,delimiter="\t",header = 0)
Data_Array_TOTAL_SUM_FORCES_Joelho = np.array(Data_TOTAL_SUM_FORCES_Joelho)

TOTAL_SUM_FORCES_Joelho_AllSpeeds= Data_Array_TOTAL_SUM_FORCES_Joelho [0:4,1]
TOTAL_SUM_FORCES_Joelho_AllSpeeds_CI_Upper = Data_Array_TOTAL_SUM_FORCES_Joelho[0:4,4]
TOTAL_SUM_FORCES_Joelho_AllSpeeds_CI = TOTAL_SUM_FORCES_Joelho_AllSpeeds_CI_Upper - TOTAL_SUM_FORCES_Joelho_AllSpeeds

    #0.2 m/s
TOTAL_SUM_FORCES_Joelho_SpeedTwo_Mean = Data_Array_TOTAL_SUM_FORCES_Joelho[0,1]
TOTAL_SUM_FORCES_Joelho_SpeedTwo_CIUpper = Data_Array_TOTAL_SUM_FORCES_Joelho[0,4]
TOTAL_SUM_FORCES_Joelho_SpeedTwo_CI = TOTAL_SUM_FORCES_Joelho_SpeedTwo_CIUpper - TOTAL_SUM_FORCES_Joelho_SpeedTwo_Mean
    #0.4 m/s
TOTAL_SUM_FORCES_Joelho_SpeedFour_Mean = Data_Array_TOTAL_SUM_FORCES_Joelho[1,1]
TOTAL_SUM_FORCES_Joelho_SpeedFour_CIUpper = Data_Array_TOTAL_SUM_FORCES_Joelho[1,4]
TOTAL_SUM_FORCES_Joelho_SpeedFour_CI = TOTAL_SUM_FORCES_Joelho_SpeedFour_CIUpper - TOTAL_SUM_FORCES_Joelho_SpeedFour_Mean
    #0.6 m/s
TOTAL_SUM_FORCES_Joelho_SpeedSix_Mean = Data_Array_TOTAL_SUM_FORCES_Joelho[2,1]
TOTAL_SUM_FORCES_Joelho_SpeedSix_CIUpper = Data_Array_TOTAL_SUM_FORCES_Joelho[2,4]
TOTAL_SUM_FORCES_Joelho_SpeedSix_CI = TOTAL_SUM_FORCES_Joelho_SpeedSix_CIUpper - TOTAL_SUM_FORCES_Joelho_SpeedSix_Mean
    #0.8 m/s
TOTAL_SUM_FORCES_Joelho_SpeedEight_Mean = Data_Array_TOTAL_SUM_FORCES_Joelho[3,1]
TOTAL_SUM_FORCES_Joelho_SpeedEight_CIUpper = Data_Array_TOTAL_SUM_FORCES_Joelho[3,4]
TOTAL_SUM_FORCES_Joelho_SpeedEight_CI = TOTAL_SUM_FORCES_Joelho_SpeedEight_CIUpper - TOTAL_SUM_FORCES_Joelho_SpeedEight_Mean

#QUADRIL
File_Path_TOTAL_SUM_FORCES_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/TOTAL_SUM_FORCES_Drag_GRFVMean_Quadril.txt")
Data_TOTAL_SUM_FORCES_Quadril = pd.read_csv(File_Path_TOTAL_SUM_FORCES_Quadril,delimiter="\t",header = 0)
Data_Array_TOTAL_SUM_FORCES_Quadril = np.array(Data_TOTAL_SUM_FORCES_Quadril)

TOTAL_SUM_FORCES_Quadril_AllSpeeds= Data_Array_TOTAL_SUM_FORCES_Quadril [0:4,1]
TOTAL_SUM_FORCES_Quadril_AllSpeeds_CI_Upper = Data_Array_TOTAL_SUM_FORCES_Quadril[0:4,4]
TOTAL_SUM_FORCES_Quadril_AllSpeeds_CI = TOTAL_SUM_FORCES_Quadril_AllSpeeds_CI_Upper - TOTAL_SUM_FORCES_Quadril_AllSpeeds

    #0.2 m/s
TOTAL_SUM_FORCES_Quadril_SpeedTwo_Mean = Data_Array_TOTAL_SUM_FORCES_Quadril[0,1]
TOTAL_SUM_FORCES_Quadril_SpeedTwo_CIUpper = Data_Array_TOTAL_SUM_FORCES_Quadril[0,4]
TOTAL_SUM_FORCES_Quadril_SpeedTwo_CI = TOTAL_SUM_FORCES_Quadril_SpeedTwo_CIUpper - TOTAL_SUM_FORCES_Quadril_SpeedTwo_Mean
    #0.4 m/s
TOTAL_SUM_FORCES_Quadril_SpeedFour_Mean = Data_Array_TOTAL_SUM_FORCES_Quadril[1,1]
TOTAL_SUM_FORCES_Quadril_SpeedFour_CIUpper = Data_Array_TOTAL_SUM_FORCES_Quadril[1,4]
TOTAL_SUM_FORCES_Quadril_SpeedFour_CI = TOTAL_SUM_FORCES_Quadril_SpeedFour_CIUpper - TOTAL_SUM_FORCES_Quadril_SpeedFour_Mean
    #0.6 m/s
TOTAL_SUM_FORCES_Quadril_SpeedSix_Mean = Data_Array_TOTAL_SUM_FORCES_Quadril[2,1]
TOTAL_SUM_FORCES_Quadril_SpeedSix_CIUpper = Data_Array_TOTAL_SUM_FORCES_Quadril[2,4]
TOTAL_SUM_FORCES_Quadril_SpeedSix_CI = TOTAL_SUM_FORCES_Quadril_SpeedSix_CIUpper - TOTAL_SUM_FORCES_Quadril_SpeedSix_Mean
    #0.8 m/s
TOTAL_SUM_FORCES_Quadril_SpeedEight_Mean = Data_Array_TOTAL_SUM_FORCES_Quadril[3,1]
TOTAL_SUM_FORCES_Quadril_SpeedEight_CIUpper = Data_Array_TOTAL_SUM_FORCES_Quadril[3,4]
TOTAL_SUM_FORCES_Quadril_SpeedEight_CI = TOTAL_SUM_FORCES_Quadril_SpeedEight_CIUpper - TOTAL_SUM_FORCES_Quadril_SpeedEight_Mean

#UMBIGO
File_Path_TOTAL_SUM_FORCES_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/TOTAL_SUM_FORCES_Drag_GRFVMean_Umbigo.txt")
Data_TOTAL_SUM_FORCES_Umbigo = pd.read_csv(File_Path_TOTAL_SUM_FORCES_Umbigo,delimiter="\t",header = 0)
Data_Array_TOTAL_SUM_FORCES_Umbigo = np.array(Data_TOTAL_SUM_FORCES_Umbigo)

TOTAL_SUM_FORCES_Umbigo_AllSpeeds= Data_Array_TOTAL_SUM_FORCES_Umbigo[0:4,1]
TOTAL_SUM_FORCES_Umbigo_AllSpeeds_CI_Upper = Data_Array_TOTAL_SUM_FORCES_Umbigo[0:4,4]
TOTAL_SUM_FORCES_Umbigo_AllSpeeds_CI = TOTAL_SUM_FORCES_Umbigo_AllSpeeds_CI_Upper - TOTAL_SUM_FORCES_Umbigo_AllSpeeds

    #0.2 m/s
TOTAL_SUM_FORCES_Umbigo_SpeedTwo_Mean = Data_Array_TOTAL_SUM_FORCES_Umbigo[0,1]
TOTAL_SUM_FORCES_Umbigo_SpeedTwo_CIUpper = Data_Array_TOTAL_SUM_FORCES_Umbigo[0,4]
TOTAL_SUM_FORCES_Umbigo_SpeedTwo_CI = TOTAL_SUM_FORCES_Umbigo_SpeedTwo_CIUpper - TOTAL_SUM_FORCES_Umbigo_SpeedTwo_Mean
    #0.4 m/s
TOTAL_SUM_FORCES_Umbigo_SpeedFour_Mean = Data_Array_TOTAL_SUM_FORCES_Umbigo[1,1]
TOTAL_SUM_FORCES_Umbigo_SpeedFour_CIUpper = Data_Array_TOTAL_SUM_FORCES_Umbigo[1,4]
TOTAL_SUM_FORCES_Umbigo_SpeedFour_CI = TOTAL_SUM_FORCES_Umbigo_SpeedFour_CIUpper - TOTAL_SUM_FORCES_Umbigo_SpeedFour_Mean
    #0.6 m/s
TOTAL_SUM_FORCES_Umbigo_SpeedSix_Mean = Data_Array_TOTAL_SUM_FORCES_Umbigo[2,1]
TOTAL_SUM_FORCES_Umbigo_SpeedSix_CIUpper = Data_Array_TOTAL_SUM_FORCES_Umbigo[2,4]
TOTAL_SUM_FORCES_Umbigo_SpeedSix_CI = TOTAL_SUM_FORCES_Umbigo_SpeedSix_CIUpper - TOTAL_SUM_FORCES_Umbigo_SpeedSix_Mean
    #0.8 m/s
TOTAL_SUM_FORCES_Umbigo_SpeedEight_Mean = Data_Array_TOTAL_SUM_FORCES_Umbigo[3,1]
TOTAL_SUM_FORCES_Umbigo_SpeedEight_CIUpper = Data_Array_TOTAL_SUM_FORCES_Umbigo[3,4]
TOTAL_SUM_FORCES_Umbigo_SpeedEight_CI = TOTAL_SUM_FORCES_Umbigo_SpeedEight_CIUpper - TOTAL_SUM_FORCES_Umbigo_SpeedEight_Mean

#XIFOIDE
File_Path_TOTAL_SUM_FORCES_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/TOTAL_SUM_FORCES_Drag_GRFVMean_Xifoide.txt")
Data_TOTAL_SUM_FORCES_Xifoide = pd.read_csv(File_Path_TOTAL_SUM_FORCES_Xifoide,delimiter="\t",header = 0)
Data_Array_TOTAL_SUM_FORCES_Xifoide = np.array(Data_TOTAL_SUM_FORCES_Xifoide)

TOTAL_SUM_FORCES_Xifoide_AllSpeeds= Data_Array_TOTAL_SUM_FORCES_Xifoide[0:4,1]
TOTAL_SUM_FORCES_Xifoide_AllSpeeds_CI_Upper = Data_Array_TOTAL_SUM_FORCES_Xifoide[0:4,4]
TOTAL_SUM_FORCES_Xifoide_AllSpeeds_CI = TOTAL_SUM_FORCES_Xifoide_AllSpeeds_CI_Upper - TOTAL_SUM_FORCES_Xifoide_AllSpeeds

    #0.2 m/s
TOTAL_SUM_FORCES_Xifoide_SpeedTwo_Mean = Data_Array_TOTAL_SUM_FORCES_Xifoide[0,1]
TOTAL_SUM_FORCES_Xifoide_SpeedTwo_CIUpper = Data_Array_TOTAL_SUM_FORCES_Xifoide[0,4]
TOTAL_SUM_FORCES_Xifoide_SpeedTwo_CI = TOTAL_SUM_FORCES_Xifoide_SpeedTwo_CIUpper - TOTAL_SUM_FORCES_Xifoide_SpeedTwo_Mean
    #0.4 m/s
TOTAL_SUM_FORCES_Xifoide_SpeedFour_Mean = Data_Array_TOTAL_SUM_FORCES_Xifoide[1,1]
TOTAL_SUM_FORCES_Xifoide_SpeedFour_CIUpper = Data_Array_TOTAL_SUM_FORCES_Xifoide[1,4]
TOTAL_SUM_FORCES_Xifoide_SpeedFour_CI = TOTAL_SUM_FORCES_Xifoide_SpeedFour_CIUpper - TOTAL_SUM_FORCES_Xifoide_SpeedFour_Mean
    #0.6 m/s
TOTAL_SUM_FORCES_Xifoide_SpeedSix_Mean = Data_Array_TOTAL_SUM_FORCES_Xifoide[2,1]
TOTAL_SUM_FORCES_Xifoide_SpeedSix_CIUpper = Data_Array_TOTAL_SUM_FORCES_Xifoide[2,4]
TOTAL_SUM_FORCES_Xifoide_SpeedSix_CI = TOTAL_SUM_FORCES_Xifoide_SpeedSix_CIUpper - TOTAL_SUM_FORCES_Xifoide_SpeedSix_Mean
    #0.8 m/s
TOTAL_SUM_FORCES_Xifoide_SpeedEight_Mean = Data_Array_TOTAL_SUM_FORCES_Xifoide[3,1]
TOTAL_SUM_FORCES_Xifoide_SpeedEight_CIUpper = Data_Array_TOTAL_SUM_FORCES_Xifoide[3,4]
TOTAL_SUM_FORCES_Xifoide_SpeedEight_CI = TOTAL_SUM_FORCES_Xifoide_SpeedEight_CIUpper - TOTAL_SUM_FORCES_Xifoide_SpeedEight_Mean



#TOTAL MATRIX SUM FORCES
TOTAL_SUM_FORCES_Total= np.append(TOTAL_SUM_FORCES_Joelho_AllSpeeds,TOTAL_SUM_FORCES_Quadril_AllSpeeds)
TOTAL_SUM_FORCES_Total= np.append(TOTAL_SUM_FORCES_Total,TOTAL_SUM_FORCES_Umbigo_AllSpeeds)
TOTAL_SUM_FORCES_Total= np.append(TOTAL_SUM_FORCES_Total,TOTAL_SUM_FORCES_Xifoide_AllSpeeds)
TOTAL_SUM_FORCES_Total = TOTAL_SUM_FORCES_Total.tolist()
TOTAL_SUM_FORCES_Total_CI = np.append(TOTAL_SUM_FORCES_Joelho_AllSpeeds_CI,TOTAL_SUM_FORCES_Quadril_AllSpeeds_CI)
TOTAL_SUM_FORCES_Total_CI = np.append(TOTAL_SUM_FORCES_Total_CI,TOTAL_SUM_FORCES_Umbigo_AllSpeeds_CI)
TOTAL_SUM_FORCES_Total_CI = np.append(TOTAL_SUM_FORCES_Total_CI,TOTAL_SUM_FORCES_Xifoide_AllSpeeds_CI)
TOTAL_SUM_FORCES_Total_CI = TOTAL_SUM_FORCES_Total_CI.tolist()


#7) PAVEI & MINETTI (2016) CURVE OF COST OF TRANSPORT

def Custo_Pavei(v,g):
    return 3.531 - 3.3374*v + 1.535*v**2 + 0.0557*g


#8)FIGURES

#FIGURE 1
#FIGURE 3D OF INDIVIDUAL DATA OF COST OF TRANSPORT
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#fig.canvas.set_window_title('Cost of Transport x Speed x Depth in Meters (INDIVIDUAL VALUES')
x = Data_Array[:,2]
y = Data_Array[:,1]
z = Data_Array[:,5]
z = np.reshape(z,(-1,1))

#X axis
#xticks = [1, 2, 3, 4]
#xlabels = ["Knee", "Hip", "Umbilical","Xiphoid"]
#plt.xticks(xticks, xlabels)
#Y axis
#yticks = [2, 3, 4, 5]
#ylabels = ["0.2 m/s", "0.4 m/s", "0.6 m/s","0.8 m/s"]
#plt.yticks(yticks, ylabels)
#plt.yticks(np.arange(min(y), max(y)+1, 1.0))
#Z axis
#ax.set_zlim(0, 15)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.i'))

#ax.set_xlabel('Depth in Meters (m)',fontsize=14)
#ax.set_ylabel('Speed (m/s)',fontsize=14)
#ax.set_zlabel('Cost of Transport (J/kg/m)',fontsize=14)
#fig.suptitle('Cost of Transport', fontsize=20)

#Scatter Plot Specifications
c = (z)
s = 450
#ax.scatter(x,y,z,s=s, c = c, cmap = 'rainbow')


#FIGURE 2
#FIGURE 3D OF TOTAL COST OF TRANSPORT MEAN DATA

#Reference for Surface Fit: http://inversionlabs.com/2016/03/21/best-fit-surfaces-for-3-dimensional-data.html

#Set Matrix of Surface to be Plotted [x, y, z]
Data_Total = np.c_[DepthMeters_Total,Speed_Total,Custo_Total]   #Create One big array (Slice Concatanate) of (N x 3). N is lenght of each Individual array.

#Prepare Surface Plot
# regular grid covering the domain of the data
mn = np.min(Data_Total, axis=0)     # Minima along the first axis (mn is a (1 x 3) array)
mx = np.max(Data_Total, axis=0)     # Maxima along the first axis (mx is a (1 x 3) array)
X,Y = np.meshgrid(np.linspace(mn[0], mx[0], 20), np.linspace(mn[1], mx[1], 20)) #meshgrid: create a retangular array from two input vectors with all pair combinations between them. Output is two 2D arrays.
XX = X.flatten()    #flatten: convert n-D array into 1D array
YY = Y.flatten()

# 1º Order ((best-fit linear curve)
# best-fit linear plane (1st-order)
A_1 = np.c_[Data_Total[:, 0], Data_Total[:, 1], np.ones(Data_Total.shape[0])]

#Parameters order: Parameter[0]: x; Parameter[1]: y; Parameter[2]: linear intercept
Parameters_1, Error_1, _, _ = scipy.linalg.lstsq(A_1, Data_Total[:, 2])  # coefficients

# evaluate it on grid
Z_1 = Parameters_1[0] * X + Parameters_1[1] * Y + Parameters_1[2]

#Minimum Point Of Surface
xmin_Z_1, ymin_Z_1 = np.unravel_index(np.argmin(Z_1), Z_1.shape)
minimum_Z_1 = (X[xmin_Z_1,ymin_Z_1], Y[xmin_Z_1,ymin_Z_1], Z_1.min())
minimum_Z_1 = np.asarray(minimum_Z_1)

# or expressed using matrix/vector product
# Z = np.dot(np.c_[XX, YY, np.ones(XX.shape)], C).reshape(X.shape)

# 2º Order (best-fit quadratic curve)
# A is an Array n x 6: [1 ; x ; y ; x*y ; x^2 ; y^2]
A_2 = np.c_[np.ones(Data_Total.shape[0]), Data_Total[:, :2], np.prod(Data_Total[:, :2], axis=1), Data_Total[:, :2] ** 2]

#Parameters order: #Parameter[5]: y**2; Parameter[4]: x**2; Parameter[3]: y*x; Parameter[2]: y; Parameter[1]: x; Parameter[0]: linear intercept
Parameters_2, Error_2, _, _ = scipy.linalg.lstsq(A_2, Data_Total[:, 2])    #scipy: scipy library; linalg: linear algebra module; lstsq: least squares function (Ax=b; find x).

# evaluate it on a grid
Z_2 = np.dot(np.c_[np.ones(XX.shape), XX, YY, XX * YY, XX ** 2, YY ** 2], Parameters_2).reshape(X.shape)


#Minimum Point Of Surface
xmin_Z_2, ymin_Z_2 = np.unravel_index(np.argmin(Z_2), Z_2.shape)
minimum_Z_2 = (X[xmin_Z_2,ymin_Z_2], Y[xmin_Z_2,ymin_Z_2], Z_2.min())
minimum_Z_2 = np.asarray(minimum_Z_2)
# Arrays for plotting,
# first row for points in xplane, last row for points in 3D space
#Ami = np.array([mi]*4)
#for i, v in enumerate([4,4,20]):
#    Ami[i,i] = v


#print('Parameters 1º Order Polynomial')
#print(Parameters_1)
#print ('Error Fit 1º Order Polynomial')
#print(Error_1)

#print('Parameters 2º Order Polynomial')
#print(Parameters_2)
#print ('Error Fit 2º Order Polynomial')
#print(Error_2)

#PAVEI & MINETTI (2016) COST SURFACE

Data_Total_PaveiSurface = np.c_[Gravity_Total, Speed_Total]

#Prepare Surface Plot
# regular grid covering the domain of the data
mn_Pavei = np.min(Data_Total_PaveiSurface , axis=0)     # Minima along the first axis (mn is a (1 x 3) array)
mx_Pavei = np.max(Data_Total_PaveiSurface , axis=0)     # Maxima along the first axis (mx is a (1 x 3) array)
X_Pavei,Y_Pavei = np.meshgrid(np.linspace(mn_Pavei[0], mx_Pavei[0], 20), np.linspace(mn_Pavei[1], mx_Pavei[1], 20)) #meshgrid: create a retangular array from two input vectors with all pair combinations between them. Output is two 2D arrays.
XX_Pavei = X_Pavei.flatten()    #flatten: convert n-D array into 1D array
YY_Pavei = Y_Pavei.flatten()

Z_Pavei = Custo_Pavei(YY_Pavei, XX_Pavei).reshape(X.shape)

#Minimum Point Of Surface
xmin_Z_Pavei, ymin_Z_Pavei = np.unravel_index(np.argmin(Z_Pavei), Z_Pavei.shape)
minimum_Z_Pavei = (X[xmin_Z_Pavei,ymin_Z_Pavei], Y[xmin_Z_Pavei,ymin_Z_Pavei], Z_Pavei.min())
minimum_Z_Pavei = np.asarray(minimum_Z_Pavei)

#fig, ax = plt.subplots(2,2, sharex=True, sharey= 'row')
#Create figure
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#fig.canvas.set_window_title('Cost of Transport x Speed x Depth in Meters (MEAN)')

#X axis
#plt.xticks(np.arange(min(DepthMeters_Total), max(DepthMeters_Total)+1, 0.2))
#Y axis
#yticks = [2, 3, 4, 5]
#ylabels = ["0.2 m/s", "0.4 m/s", "0.6 m/s","0.8 m/s"]
#plt.yticks(yticks, ylabels)
#plt.yticks(np.arange(min(Speed_Total), max(Speed_Total)+1, 0.2))
#Z axis
#ax.set_zlim(0, 15)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.i'))

#ax.set_xlabel('Depth in Meters (m)',fontsize=12, fontweight='bold')
#ax.set_ylabel('Speed (m/s)',fontsize=12, fontweight='bold')
#ax.set_zlabel('Cost of Transport (J/kg/m)',fontsize=12, fontweight='bold')
#fig.suptitle('Cost of Transport: Water 2º Order Surface Fit vs. Pavei & Minetti Hypogravity (2016)', fontsize=14, fontweight='bold')

#Scatter Plot and Surface Specification
c = (Custo_Total)
s = 200
#ax.scatter(DepthMeters_Total,Speed_Total,Custo_Total,s=s, c=c, alpha=1.0, cmap='autumn', marker='p', label='Cost of Transport per Condition')

#1º Order Polynomial Surface
#ax.plot_surface(X, Y, Z_1, rstride=1, cstride=1, alpha=0.8, cmap='autumn', label = '1º Order Fit')
#ax.scatter(minimum_Z_1[0], minimum_Z_1[1], minimum_Z_1[2], color='black', s=500, marker='*')

#2º Order Polynomial Surface
#ax.plot_surface(X, Y, Z_2, rstride=1, cstride=1, alpha=0.8, cmap='autumn', label = '2º Order Fit')
#ax.scatter(minimum_Z_2[0], minimum_Z_2[1], minimum_Z_2[2], color='black', s=500, marker='*')

#print(X[1,1])
#print(Y[1,1])
print(Z_2[:,1])
#print(X_Pavei[1,1])
#print(np.flip(X)[1,1])
print(Z_Pavei[:,1])

#Pavei Cost function
#ax.plot_surface(np.flip(X), Y_Pavei, Z_Pavei, rstride=1, cstride=1, alpha=0.6, cmap='winter', label = 'Pavei Cost')
#ax.scatter(minimum_Z_Pavei[0], minimum_Z_Pavei[1], minimum_Z_Pavei[2], color='black', s=500, marker='d')

#Error bar of COST TRANSPORT
#for i in np.arange(0, len(Custo_Total)):
#    ax.plot((DepthMeters_Total[i],DepthMeters_Total[i]), (Speed_Total[i],Speed_Total[i]), (Custo_Total[i] + Custo_Total_CI[i], Custo_Total[i] - Custo_Total_CI[i]), "k-")

#VAS Points of Each Depth and Error Bar respective
svas = 300

# Find Z-Position of each VAS Point at Surface Fit
VAS_Joelho_Z_1 = (Parameters_1[1]*VAS_Joelho) + (Parameters_1[0]*DepthMeters_Total[1]) + (Parameters_1[2])
VAS_Quadril_Z_1 =(Parameters_1[1]*VAS_Quadril) + (Parameters_1[0]*DepthMeters_Total[5]) + (Parameters_1[2])
VAS_Umbigo_Z_1 = (Parameters_1[1]*VAS_Umbigo) + (Parameters_1[0]*DepthMeters_Total[9]) + (Parameters_1[2])
VAS_Xifoide_Z_1 = (Parameters_1[1]*VAS_Xifoide) + (Parameters_1[0]*DepthMeters_Total[13]) + (Parameters_1[2])

VAS_Joelho_Z_2 = (Parameters_2[5]*VAS_Joelho**2) + (Parameters_2[4]* DepthMeters_Total[1]**2) + (Parameters_2[3]*VAS_Joelho* DepthMeters_Total[1]) + (Parameters_2[2]*VAS_Joelho) + (Parameters_2[1]*DepthMeters_Total[1]) + (Parameters_2[0])
VAS_Quadril_Z_2 = (Parameters_2[5]*VAS_Quadril**2) + (Parameters_2[4]* DepthMeters_Total[5]**2) + (Parameters_2[3]*VAS_Quadril* DepthMeters_Total[5]) + (Parameters_2[2]*VAS_Quadril) + (Parameters_2[1]*DepthMeters_Total[5]) + (Parameters_2[0])
VAS_Umbigo_Z_2 = (Parameters_2[5]*VAS_Umbigo**2) + (Parameters_2[4]* DepthMeters_Total[9]**2) + (Parameters_2[3]*VAS_Umbigo* DepthMeters_Total[9]) + (Parameters_2[2]*VAS_Umbigo) + (Parameters_2[1]*DepthMeters_Total[9]) + (Parameters_2[0])
VAS_Xifoide_Z_2 = (Parameters_2[5]*VAS_Xifoide**2) + (Parameters_2[4]* DepthMeters_Total[13]**2) + (Parameters_2[3]*VAS_Xifoide* DepthMeters_Total[13]) + (Parameters_2[2]*VAS_Xifoide) + (Parameters_2[1]*DepthMeters_Total[13]) + (Parameters_2[0])

#VAS MATRIX FOR LINE PLOT CONECTING EACH VAS POINT
VAS_Line_Plot_Depth = np.array([DepthMeters_Total[1], DepthMeters_Total[5], DepthMeters_Total[9], DepthMeters_Total[13]])
VAS_Line_Plot_VAS = np.array([VAS_Joelho, VAS_Quadril, VAS_Umbigo, VAS_Xifoide])
VAS_Line_Plot_Z_1 = np.array([VAS_Joelho_Z_1, VAS_Quadril_Z_1, VAS_Umbigo_Z_1, VAS_Xifoide_Z_1])
VAS_Line_Plot_Z_2 = np.array([VAS_Joelho_Z_2, VAS_Quadril_Z_2, VAS_Umbigo_Z_2, VAS_Xifoide_Z_2])

#ax.scatter(DepthMeters_Total[1],VAS_Joelho, VAS_Joelho_Z_2,  color='black', s=svas, marker='o', label = 'Self-Selected Speed per Depth')
#ax.plot((DepthMeters_Total[1], DepthMeters_Total[1]), [VAS_Joelho + VAS_Joelho_CI, VAS_Joelho - VAS_Joelho_CI], [VAS_Joelho_Z_2, VAS_Joelho_Z_2], "k-")

#ax.scatter(DepthMeters_Total[5],VAS_Quadril, VAS_Quadril_Z_2,  color='black', s=svas, marker='o')
#ax.plot((DepthMeters_Total[5], DepthMeters_Total[5]), [VAS_Quadril + VAS_Quadril_CI, VAS_Quadril - VAS_Quadril_CI], [VAS_Quadril_Z_2, VAS_Quadril_Z_2], "k-")

#ax.scatter(DepthMeters_Total[9],VAS_Umbigo, VAS_Umbigo_Z_2,  color='black', s=svas, marker='o')
#ax.plot((DepthMeters_Total[9], DepthMeters_Total[9]), [VAS_Umbigo + VAS_Umbigo_CI, VAS_Umbigo - VAS_Umbigo_CI], [VAS_Umbigo_Z_2, VAS_Umbigo_Z_2], "k-")

#ax.scatter(DepthMeters_Total[13],VAS_Xifoide, VAS_Xifoide_Z_2,  color='black', s=svas, marker='o')
#ax.plot((DepthMeters_Total[13], DepthMeters_Total[13]), [VAS_Xifoide + VAS_Xifoide_CI, VAS_Xifoide - VAS_Xifoide_CI], [VAS_Xifoide_Z_2, VAS_Xifoide_Z_2], "k-")

#ax.plot(VAS_Line_Plot_Depth, VAS_Line_Plot_VAS,VAS_Line_Plot_Z_2, '--', color = 'black',linewidth = 2.5)

#ax.legend(frameon=False)

#Animation Section: create the rotation animation and Save .mp4 file
#for angle in range(0, 360):
#    ax.view_init(20, angle)
#    plt.draw()
#    plt.pause(.001)

#def rotate(angle):
 #      ax.view_init(10, azim=angle)

#rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=250)

Writer = animation.writers['ffmpeg']
writer = Writer(metadata=dict(artist='Me'), bitrate=-1)
#rot_animation.save("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Grafico_Cost_Depth_Velocidade_SURFACE2ºOrder_PaveiMinetti_Video.mp4", writer=writer)







#FIGURE 3
#FIGURE 3D OF TOTAL EXTERNAL FORCE MEAN DATA

#Reference for Surface Fit: http://inversionlabs.com/2016/03/21/best-fit-surfaces-for-3-dimensional-data.html

#Set Matrix of Surface to be Plotted [x, y, z]
Data_Total_Force = np.c_[DepthMeters_Total,Speed_Total,TOTAL_SUM_FORCES_Total]   #Create One big array (Slice Concatanate) of (N x 3). N is lenght of each Individual array.

#Prepare Surface Plot
# regular grid covering the domain of the data
mn_Force = np.min(Data_Total_Force, axis=0)     # Minima along the first axis (mn is a (1 x 3) array)
mx_Force = np.max(Data_Total_Force, axis=0)     # Maxima along the first axis (mx is a (1 x 3) array)
X_Force,Y_Force = np.meshgrid(np.linspace(mn_Force[0], mx_Force[0], 20), np.linspace(mn_Force[1], mx_Force[1], 20)) #meshgrid: create a retangular array from two input vectors with all pair combinations between them. Output is two 2D arrays.
XX_Force = X_Force.flatten()    #flatten: convert n-D array into 1D array
YY_Force = Y_Force.flatten()

# 1º Order ((best-fit linear curve)
# best-fit linear plane (1st-order)
A_Force_1 = np.c_[Data_Total_Force[:,0], Data_Total_Force[:,1], np.ones(Data_Total_Force.shape[0])]

#Parameters order: Parameter[0]: x; Parameter[1]: y; Parameter[2]: linear intercept
Parameters_Force_1, Error_Force_1, _, _ = scipy.linalg.lstsq(A_Force_1, Data_Total_Force[:,2])  # coefficients

# evaluate it on grid
Z_Force_1 = Parameters_Force_1[0] * X_Force + Parameters_Force_1[1] * Y_Force + Parameters_Force_1[2]

#Minimum Point Of Surface
xmin_Z_Force_1, ymin_Z_Force_1 = np.unravel_index(np.argmin(Z_Force_1), Z_Force_1.shape)
minimum_Z_Force_1 = (X_Force[xmin_Z_Force_1,ymin_Z_Force_1], Y_Force[xmin_Z_Force_1,ymin_Z_Force_1], Z_Force_1.min())
minimum_Z_Force_1 = np.asarray(minimum_Z_Force_1)

# or expressed using matrix/vector product
# Z = np.dot(np.c_[XX, YY, np.ones(XX.shape)], C).reshape(X.shape)

# 2º Order (best-fit quadratic curve)
# A is an Array n x 6: [1 ; x ; y ; x*y ; x^2 ; y^2]
A_Force_2 = np.c_[np.ones(Data_Total_Force.shape[0]), Data_Total_Force[:, :2], np.prod(Data_Total_Force[:, :2], axis=1), Data_Total_Force[:, :2] ** 2]

#Parameters order: #Parameter[5]: y**2; Parameter[4]: x**2; Parameter[3]: y*x; Parameter[2]: y; Parameter[1]: x; Parameter[0]: linear intercept
Parameters_Force_2, Error_Force_2, _, _ = scipy.linalg.lstsq(A_Force_2, Data_Total_Force[:, 2])    #scipy: scipy library; linalg: linear algebra module; lstsq: least squares function (Ax=b; find x).

# evaluate it on a grid
Z_Force_2 = np.dot(np.c_[np.ones(XX_Force.shape), XX_Force, YY_Force, XX_Force * YY_Force, XX_Force ** 2, YY_Force ** 2], Parameters_Force_2).reshape(X_Force.shape)


#Minimum Point Of Surface
xmin_Z_Force_2, ymin_Z_Force_2 = np.unravel_index(np.argmin(Z_Force_2), Z_Force_2.shape)
minimum_Z_Force_2 = (X_Force[xmin_Z_Force_2,ymin_Z_Force_2], Y[xmin_Z_Force_2,ymin_Z_Force_2], Z_Force_2.min())
minimum_Z_Force_2 = np.asarray(minimum_Z_Force_2)
# Arrays for plotting,
# first row for points in xplane, last row for points in 3D space
#Ami = np.array([mi]*4)
#for i, v in enumerate([4,4,20]):
#    Ami[i,i] = v


print('Parameters 1º Order Polynomial Force')
print(Parameters_Force_1)
print ('Error Fit 1º Order Polynomial Force')
print(Error_Force_1)

print('Parameters 2º Order Polynomial Force')
print(Parameters_Force_2)
print ('Error Fit 2º Order Polynomial Force')
print(Error_Force_2)


#Create figure
fig = plt.figure()
ax = fig.gca(projection='3d')
fig.canvas.set_window_title('External Force x Speed x Depth in Meters (MEAN)')

#X axis
#plt.xticks(np.arange(min(DepthMeters_Total), max(DepthMeters_Total)+1, 0.2))
#Y axis
#yticks = [2, 3, 4, 5]
#ylabels = ["0.2 m/s", "0.4 m/s", "0.6 m/s","0.8 m/s"]
#plt.yticks(yticks, ylabels)
#plt.yticks(np.arange(min(Speed_Total), max(Speed_Total)+1, 0.2))
#Z axis
ax.set_zlim(150, 1000)
ax.zaxis.set_ticks(np.arange(100,1000,200))
#ax.zaxis.set_major_locator(LinearLocator(20))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.i'))

ax.set_xlabel('Depth in Meters (m)',fontsize=12, fontweight='bold')
ax.set_ylabel('Speed (m/s)',fontsize=12, fontweight='bold')
ax.set_zlabel('External Force (N))',fontsize=12, fontweight='bold')
fig.suptitle('External Force and 2º Order Surface Fit', fontsize=16, fontweight='bold')

#Scatter Plot and Surface Specification
c = (Custo_Total)
s = 200
ax.scatter(DepthMeters_Total,Speed_Total,TOTAL_SUM_FORCES_Total,s=s, c=c, alpha=1.0, cmap='autumn', marker='p', label='External Force per Condition')

#1º Order Polynomial Surface
#ax.plot_surface(X_Force, Y_Force, Z_Force_1, rstride=1, cstride=1, alpha=0.8, cmap='autumn', label = '1º Order Fit')
#ax.scatter(minimum_Z_Force_1[0], minimum_Z_Force_1[1], minimum_Z_Force_1[2], color='black', s=500, marker='*')

#2º Order Polynomial Surface
ax.plot_surface(X_Force, Y_Force, Z_Force_2, rstride=1, cstride=1, alpha=0.8, cmap='autumn', label = '2º Order Fit')
ax.scatter(minimum_Z_Force_2[0], minimum_Z_Force_2[1], minimum_Z_Force_2[2], color='black', s=500, marker='*')



#Error bar of EXTERNAL FORCE
for i in np.arange(0, len(TOTAL_SUM_FORCES_Total)):
    ax.plot((DepthMeters_Total[i],DepthMeters_Total[i]), (Speed_Total[i],Speed_Total[i]), (TOTAL_SUM_FORCES_Total[i] + TOTAL_SUM_FORCES_Total_CI[i], TOTAL_SUM_FORCES_Total[i] - TOTAL_SUM_FORCES_Total_CI[i]), "k-")

#VAS Points of Each Depth and Error Bar respective
svas = 300

# Find Z-Position of each VAS Point at Surface Fit
VAS_Joelho_Z_Force_1 = (Parameters_Force_1[1]*VAS_Joelho) + (Parameters_Force_1[0]*DepthMeters_Total[1]) + (Parameters_Force_1[2])
VAS_Quadril_Z_Force_1 =(Parameters_Force_1[1]*VAS_Quadril) + (Parameters_Force_1[0]*DepthMeters_Total[5]) + (Parameters_Force_1[2])
VAS_Umbigo_Z_Force_1 = (Parameters_Force_1[1]*VAS_Umbigo) + (Parameters_Force_1[0]*DepthMeters_Total[9]) + (Parameters_Force_1[2])
VAS_Xifoide_Z_Force_1 = (Parameters_Force_1[1]*VAS_Xifoide) + (Parameters_Force_1[0]*DepthMeters_Total[13]) + (Parameters_Force_1[2])

VAS_Joelho_Z_Force_2 = (Parameters_Force_2[5]*VAS_Joelho**2) + (Parameters_Force_2[4]* DepthMeters_Total[1]**2) + (Parameters_Force_2[3]*VAS_Joelho* DepthMeters_Total[1]) + (Parameters_Force_2[2]*VAS_Joelho) + (Parameters_Force_2[1]*DepthMeters_Total[1]) + (Parameters_Force_2[0])
VAS_Quadril_Z_Force_2 = (Parameters_Force_2[5]*VAS_Quadril**2) + (Parameters_Force_2[4]* DepthMeters_Total[5]**2) + (Parameters_Force_2[3]*VAS_Quadril* DepthMeters_Total[5]) + (Parameters_Force_2[2]*VAS_Quadril) + (Parameters_Force_2[1]*DepthMeters_Total[5]) + (Parameters_Force_2[0])
VAS_Umbigo_Z_Force_2 = (Parameters_Force_2[5]*VAS_Umbigo**2) + (Parameters_Force_2[4]* DepthMeters_Total[9]**2) + (Parameters_Force_2[3]*VAS_Umbigo* DepthMeters_Total[9]) + (Parameters_Force_2[2]*VAS_Umbigo) + (Parameters_Force_2[1]*DepthMeters_Total[9]) + (Parameters_Force_2[0])
VAS_Xifoide_Z_Force_2 = (Parameters_Force_2[5]*VAS_Xifoide**2) + (Parameters_Force_2[4]* DepthMeters_Total[13]**2) + (Parameters_Force_2[3]*VAS_Xifoide* DepthMeters_Total[13]) + (Parameters_Force_2[2]*VAS_Xifoide) + (Parameters_Force_2[1]*DepthMeters_Total[13]) + (Parameters_Force_2[0])

#VAS MATRIX FOR LINE PLOT CONECTING EACH VAS POINT
VAS_Line_Plot_Depth = np.array([DepthMeters_Total[1], DepthMeters_Total[5], DepthMeters_Total[9], DepthMeters_Total[13]])
VAS_Line_Plot_VAS = np.array([VAS_Joelho, VAS_Quadril, VAS_Umbigo, VAS_Xifoide])
VAS_Line_Plot_Z_Force_1 = np.array([VAS_Joelho_Z_Force_1, VAS_Quadril_Z_Force_1, VAS_Umbigo_Z_Force_1, VAS_Xifoide_Z_Force_1])
VAS_Line_Plot_Z_Force_2 = np.array([VAS_Joelho_Z_Force_2, VAS_Quadril_Z_Force_2, VAS_Umbigo_Z_Force_2, VAS_Xifoide_Z_Force_2])


#VAS POINTS PER DEPTH PLOT
ax.scatter(DepthMeters_Total[1],VAS_Joelho, VAS_Joelho_Z_Force_2,  color='black', s=svas, marker='o', label = 'Self-Selected Speed per Depth')
ax.plot((DepthMeters_Total[1], DepthMeters_Total[1]), [VAS_Joelho + VAS_Joelho_CI, VAS_Joelho - VAS_Joelho_CI], [VAS_Joelho_Z_Force_2, VAS_Joelho_Z_Force_2], "k-")

ax.scatter(DepthMeters_Total[5],VAS_Quadril, VAS_Quadril_Z_Force_2,  color='black', s=svas, marker='o')
ax.plot((DepthMeters_Total[5], DepthMeters_Total[5]), [VAS_Quadril + VAS_Quadril_CI, VAS_Quadril - VAS_Quadril_CI], [VAS_Quadril_Z_Force_2, VAS_Quadril_Z_Force_2], "k-")

ax.scatter(DepthMeters_Total[9],VAS_Umbigo, VAS_Umbigo_Z_Force_2,  color='black', s=svas, marker='o')
ax.plot((DepthMeters_Total[9], DepthMeters_Total[9]), [VAS_Umbigo + VAS_Umbigo_CI, VAS_Umbigo - VAS_Umbigo_CI], [VAS_Umbigo_Z_Force_2, VAS_Umbigo_Z_Force_2], "k-")

ax.scatter(DepthMeters_Total[13],VAS_Xifoide, VAS_Xifoide_Z_Force_2,  color='black', s=svas, marker='o')
ax.plot((DepthMeters_Total[13], DepthMeters_Total[13]), [VAS_Xifoide + VAS_Xifoide_CI, VAS_Xifoide - VAS_Xifoide_CI], [VAS_Xifoide_Z_Force_2, VAS_Xifoide_Z_Force_2], "k-")

ax.plot(VAS_Line_Plot_Depth, VAS_Line_Plot_VAS,VAS_Line_Plot_Z_Force_2, '--', color = 'black',linewidth = 2.5)

#ax.legend(frameon=False)

#Animation Section: create the rotation animation and Save .mp4 file
for angle in range(0, 360):
    ax.view_init(20, angle)
    plt.draw()
    plt.pause(.001)

def rotate(angle):
        ax.view_init(10, azim=angle)

rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=250)

Writer = animation.writers['ffmpeg']
writer = Writer(metadata=dict(artist='Me'), bitrate=-1)
rot_animation.save("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Grafico_External_Force_Depth_Velocidade_SURFACE2ºOrder_Video.mp4", writer=writer)




plt.show()