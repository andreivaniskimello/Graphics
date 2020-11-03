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



#THIS ROUTINE HAS 12 SECTIONS
    #1º) IMPORT AND PREPARE MATRIX OF INDIVIDUAL DATA (COST OF TRANSPORT AND METABOLIC POWER)
    #2º) IMPORT AND PREPARE MATRIX OF TOTAL MEAN DATA COST OF TRANSPORT
    #3º) TOTAL MEAN DATA METABOLIC POWER NET (POT MET)
    #4º) IMPORT AND PREPARE MATRIX OF DEPTHS MEAN VALUES IN METRIC SCALE AND PERCENTUAL OF STATURE
    #5º) IMPORT AND PREPARE MATRIX OF VAS MEAN SPEED PER DEPTH
    #6º) ARDIGÒ'S (2003) AND ZAMPARO'S (1992) CURVES OF COST OF TRANSPORT
    #7º) IMPORT AND PREPARE MATRIX OF DRAG_F_STRIDE
    #8º) IMPORT AND PREPARE MATRIX OF DRAG_F_STRIDE_per_METER
    #9º) IMPORT AND PREPARE MATRIX OF GRF_V PEAK
    #10º) IMPORT AND PREPARE MATRIX OF GRF_V MEAN (APPARENT BODY WEIGHT)
    #11º) IMPORT AND PREPARE MATRIX OF TOTAL SUM FORCES (DRAG FORCE AND GRF_V_MEAN)
    #12º) FIGURES
        #FIGURE 01: COST AND DEPTH IN ANATOMICAL SCALE
        #FIGURE 02: COST AND DEPTH IN METRIC SCALE
        #FIGURE 03: COST AND DEPTH IN PERCENTUAL OF STATURE SCALE
        #FIGURE 04: COST PER SPEED, WITH LINES OF DEPTHS
        #FIGURE 05: COST AND DRAG FORCE AND GRFV_MEAN (Lines: Speeds)
        #FIGURE 06: COST AND DRAG FORCE PER METER (Lines: Depths)
        #FIGURE 07: COST AND GRF-V PEAK (Lines: Depths)
        #FIGURE 08: COST AND DRAG AND GRFV_MEAN WITH TWO VERTICAL AXIS 0.2 m/s
        #FIGURE 09: COST AND DRAG AND GRFV_MEAN WITH TWO VERTICAL AXIS 0.4 m/s
        #FIGURE 10: COST AND DRAG AND GRFV_MEAN WITH TWO VERTICAL AXIS 0.6 m/s
        #FIGURE 11: COST AND DRAG AND GRFV_MEAN WITH TWO VERTICAL AXIS 0.8 m/s
        #FIGURE 12: COST PER SPEED, WITH LINES OF DEPTHS (POLYNOMIAL FIT)
        #FIGURE 13: METABOLIC POWER NET PER SPEED, WITH LINES OF DEPTHS (POLYNOMIAL FIT)
        #FIGURE 14: COST OF TRANSPORT PER DEPTH (METRIC SCALE) WITH LINES OF SPEEDS (POLYNOMIAL FIT)
        #FIGURE 15: METABOLIC POWER NET PER DEPTH (METRIC SCALE) WITH LINES OF SPEEDS (POLYNOMIAL FIT)
        #FIGURE 16: COST OF TRANSPORT KNEE AND DRY LAND (Ardigò et al. 2003)



#1º)INDIVIDUAL DATA

    #PROFUNDIDADE: JOELHO
File_Path_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Profundidade_Joelho.txt")
Data_Joelho = pd.read_csv(File_Path_Joelho,delimiter="\t",header = 0)
Data_Array_Joelho = np.array(Data_Joelho)

Depth_Anatomical_Joelho = Data_Array_Joelho[:,0]
Speed_Joelho = Data_Array_Joelho[:,1]
Depth_Metric_Joelho = Data_Array_Joelho[:,2]
Depth_Percentual_Joelho = Data_Array_Joelho[:,3]
Pot_Met_Joelho = Data_Array_Joelho[:,4]
Cost_Joelho = Data_Array_Joelho[:,5]

    #PROFUNDIDADE: QUADRIL
File_Path_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Profundidade_Quadril.txt")
Data_Quadril = pd.read_csv(File_Path_Quadril,delimiter="\t",header = 0)
Data_Array_Quadril = np.array(Data_Quadril)

Depth_Anatomical_Quadril = Data_Array_Quadril[:,0]
Speed_Quadril = Data_Array_Quadril[:,1]
Depth_Metric_Quadril = Data_Array_Quadril[:,2]
Depth_Percentual_Quadril = Data_Array_Quadril[:,3]
Pot_Met_Quadril = Data_Array_Quadril[:,4]
Cost_Quadril = Data_Array_Quadril[:,5]

    #PROFUNDIDADE: UMBIGO
File_Path_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Profundidade_Umbigo.txt")
Data_Umbigo = pd.read_csv(File_Path_Umbigo,delimiter="\t",header = 0)
Data_Array_Umbigo = np.array(Data_Umbigo)

Depth_Anatomical_Umbigo = Data_Array_Umbigo[:,0]
Speed_Umbigo = Data_Array_Umbigo[:,1]
Depth_Metric_Umbigo = Data_Array_Umbigo[:,2]
Depth_Percentual_Umbigo = Data_Array_Umbigo[:,3]
Pot_Met_Umbigo = Data_Array_Umbigo[:,4]
Cost_Umbigo = Data_Array_Umbigo[:,5]

    #PROFUNDIDADE: XIFOIDE
File_Path_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Fisiologia/Planilha_Custo_Profundidade_Xifoide.txt")
Data_Xifoide = pd.read_csv(File_Path_Xifoide,delimiter="\t",header = 0)
Data_Array_Xifoide = np.array(Data_Xifoide)

Depth_Anatomical_Xifoide = Data_Array_Xifoide[:,0]
Speed_Xifoide = Data_Array_Xifoide[:,1]
Depth_Metric_Xifoide = Data_Array_Xifoide[:,2]
Depth_Percentual_Xifoide = Data_Array_Xifoide[:,3]
Pot_Met_Xifoide = Data_Array_Xifoide[:,4]
Cost_Xifoide = Data_Array_Xifoide[:,5]


#2º) TOTAL MEAN DATA CUSTO

    #JOELHO
File_Path_Custo_Mean_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Custo_Mean_Joelho.txt")
Data_Custo_Mean_Joelho = pd.read_csv(File_Path_Custo_Mean_Joelho,delimiter="\t",header = 0)
Data_Array_Custo_Mean_Joelho = np.array(Data_Custo_Mean_Joelho)

        #0.2 m/s
Custo_Joelho_SpeedTwo_Mean = Data_Array_Custo_Mean_Joelho[0,1]
Custo_Joelho_SpeedTwo_StdError = Data_Array_Custo_Mean_Joelho[0,2]
Custo_Joelho_SpeedTwo_CILower = Data_Array_Custo_Mean_Joelho[0,3]
Custo_Joelho_SpeedTwo_CIUpper = Data_Array_Custo_Mean_Joelho[0,4]
Custo_Joelho_SpeedTwo_CI = Custo_Joelho_SpeedTwo_CIUpper - Custo_Joelho_SpeedTwo_Mean
        #0.4 m/s
Custo_Joelho_SpeedFour_Mean = Data_Array_Custo_Mean_Joelho[1,1]
Custo_Joelho_SpeedFour_StdError = Data_Array_Custo_Mean_Joelho[1,2]
Custo_Joelho_SpeedFour_CILower = Data_Array_Custo_Mean_Joelho[1,3]
Custo_Joelho_SpeedFour_CIUpper = Data_Array_Custo_Mean_Joelho[1,4]
Custo_Joelho_SpeedFour_CI = Custo_Joelho_SpeedFour_CIUpper - Custo_Joelho_SpeedFour_Mean
        #0.6 m/s
Custo_Joelho_SpeedSix_Mean = Data_Array_Custo_Mean_Joelho[2,1]
Custo_Joelho_SpeedSix_StdError = Data_Array_Custo_Mean_Joelho[2,2]
Custo_Joelho_SpeedSix_CILower = Data_Array_Custo_Mean_Joelho[2,3]
Custo_Joelho_SpeedSix_CIUpper = Data_Array_Custo_Mean_Joelho[2,4]
Custo_Joelho_SpeedSix_CI = Custo_Joelho_SpeedSix_CIUpper - Custo_Joelho_SpeedSix_Mean
        #0.8 m/s
Custo_Joelho_SpeedEight_Mean = Data_Array_Custo_Mean_Joelho[3,1]
Custo_Joelho_SpeedEight_StdError = Data_Array_Custo_Mean_Joelho[3,2]
Custo_Joelho_SpeedEight_CILower = Data_Array_Custo_Mean_Joelho[3,3]
Custo_Joelho_SpeedEight_CIUpper = Data_Array_Custo_Mean_Joelho[3,4]
Custo_Joelho_SpeedEight_CI = Custo_Joelho_SpeedEight_CIUpper - Custo_Joelho_SpeedEight_Mean
    #All_Speeds
Custo_Joelho_All_Speed_Mean = Data_Array_Custo_Mean_Joelho[:,1]
Custo_Joelho_All_Speed_StdError = Data_Array_Custo_Mean_Joelho[:,2]
Custo_Joelho_All_Speed_CILower = Data_Array_Custo_Mean_Joelho[:,3]
Custo_Joelho_All_Speed_CIUpper = Data_Array_Custo_Mean_Joelho[:,4]
Custo_Joelho_All_Speed_CI = Custo_Joelho_All_Speed_CIUpper - Custo_Joelho_All_Speed_Mean
Custo_Joelho_All_Speed_Mean_list = Custo_Joelho_All_Speed_Mean.tolist()
Custo_Joelho_All_Speed_CI_list = Custo_Joelho_All_Speed_CI.tolist()
Custo_Joelho_All_Speed_Mean_withSpeedColumn = Data_Array_Custo_Mean_Joelho[:,0:2]

    #QUADRIL
File_Path_Custo_Mean_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Custo_Mean_Quadril.txt")
Data_Custo_Mean_Quadril = pd.read_csv(File_Path_Custo_Mean_Quadril,delimiter="\t",header = 0)
Data_Array_Custo_Mean_Quadril = np.array(Data_Custo_Mean_Quadril)

        #0.2 m/s
Custo_Quadril_SpeedTwo_Mean = Data_Array_Custo_Mean_Quadril[0,1]
Custo_Quadril_SpeedTwo_StdError = Data_Array_Custo_Mean_Quadril[0,2]
Custo_Quadril_SpeedTwo_CILower = Data_Array_Custo_Mean_Quadril[0,3]
Custo_Quadril_SpeedTwo_CIUpper = Data_Array_Custo_Mean_Quadril[0,4]
Custo_Quadril_SpeedTwo_CI = Custo_Quadril_SpeedTwo_CIUpper - Custo_Quadril_SpeedTwo_Mean
        #0.4 m/s
Custo_Quadril_SpeedFour_Mean = Data_Array_Custo_Mean_Quadril[1,1]
Custo_Quadril_SpeedFour_StdError = Data_Array_Custo_Mean_Quadril[1,2]
Custo_Quadril_SpeedFour_CILower = Data_Array_Custo_Mean_Quadril[1,3]
Custo_Quadril_SpeedFour_CIUpper = Data_Array_Custo_Mean_Quadril[1,4]
Custo_Quadril_SpeedFour_CI = Custo_Quadril_SpeedFour_CIUpper - Custo_Quadril_SpeedFour_Mean
        #0.6 m/s
Custo_Quadril_SpeedSix_Mean = Data_Array_Custo_Mean_Quadril[2,1]
Custo_Quadril_SpeedSix_StdError = Data_Array_Custo_Mean_Quadril[2,2]
Custo_Quadril_SpeedSix_CILower = Data_Array_Custo_Mean_Quadril[2,3]
Custo_Quadril_SpeedSix_CIUpper = Data_Array_Custo_Mean_Quadril[2,4]
Custo_Quadril_SpeedSix_CI = Custo_Quadril_SpeedSix_CIUpper - Custo_Quadril_SpeedSix_Mean
        #0.8 m/s
Custo_Quadril_SpeedEight_Mean = Data_Array_Custo_Mean_Quadril[3,1]
Custo_Quadril_SpeedEight_StdError = Data_Array_Custo_Mean_Quadril[3,2]
Custo_Quadril_SpeedEight_CILower = Data_Array_Custo_Mean_Quadril[3,3]
Custo_Quadril_SpeedEight_CIUpper = Data_Array_Custo_Mean_Quadril[3,4]
Custo_Quadril_SpeedEight_CI = Custo_Quadril_SpeedEight_CIUpper - Custo_Quadril_SpeedEight_Mean
    #All_Speeds
Custo_Quadril_All_Speed_Mean = Data_Array_Custo_Mean_Quadril[:,1]
Custo_Quadril_All_Speed_StdError = Data_Array_Custo_Mean_Quadril[:,2]
Custo_Quadril_All_Speed_CILower = Data_Array_Custo_Mean_Quadril[:,3]
Custo_Quadril_All_Speed_CIUpper = Data_Array_Custo_Mean_Quadril[:,4]
Custo_Quadril_All_Speed_CI = Custo_Quadril_All_Speed_CIUpper - Custo_Quadril_All_Speed_Mean
Custo_Quadril_All_Speed_Mean_list = Custo_Quadril_All_Speed_Mean.tolist()
Custo_Quadril_All_Speed_CI_list = Custo_Quadril_All_Speed_CI.tolist()
Custo_Quadril_All_Speed_Mean_withSpeedColumn = Data_Array_Custo_Mean_Quadril[:,0:2]

    #UMBIGO
File_Path_Custo_Mean_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Custo_Mean_Umbigo.txt")
Data_Custo_Mean_Umbigo = pd.read_csv(File_Path_Custo_Mean_Umbigo,delimiter="\t",header = 0)
Data_Array_Custo_Mean_Umbigo = np.array(Data_Custo_Mean_Umbigo)

        #0.2 m/s
Custo_Umbigo_SpeedTwo_Mean = Data_Array_Custo_Mean_Umbigo[0,1]
Custo_Umbigo_SpeedTwo_StdError = Data_Array_Custo_Mean_Umbigo[0,2]
Custo_Umbigo_SpeedTwo_CILower = Data_Array_Custo_Mean_Umbigo[0,3]
Custo_Umbigo_SpeedTwo_CIUpper = Data_Array_Custo_Mean_Umbigo[0,4]
Custo_Umbigo_SpeedTwo_CI = Custo_Umbigo_SpeedTwo_CIUpper - Custo_Umbigo_SpeedTwo_Mean
        #0.4 m/s
Custo_Umbigo_SpeedFour_Mean = Data_Array_Custo_Mean_Umbigo[1,1]
Custo_Umbigo_SpeedFour_StdError = Data_Array_Custo_Mean_Umbigo[1,2]
Custo_Umbigo_SpeedFour_CILower = Data_Array_Custo_Mean_Umbigo[1,3]
Custo_Umbigo_SpeedFour_CIUpper = Data_Array_Custo_Mean_Umbigo[1,4]
Custo_Umbigo_SpeedFour_CI = Custo_Umbigo_SpeedFour_CIUpper - Custo_Umbigo_SpeedFour_Mean
        #0.6 m/s
Custo_Umbigo_SpeedSix_Mean = Data_Array_Custo_Mean_Umbigo[2,1]
Custo_Umbigo_SpeedSix_StdError = Data_Array_Custo_Mean_Umbigo[2,2]
Custo_Umbigo_SpeedSix_CILower = Data_Array_Custo_Mean_Umbigo[2,3]
Custo_Umbigo_SpeedSix_CIUpper = Data_Array_Custo_Mean_Umbigo[2,4]
Custo_Umbigo_SpeedSix_CI = Custo_Umbigo_SpeedSix_CIUpper - Custo_Umbigo_SpeedSix_Mean
        #0.8 m/s
Custo_Umbigo_SpeedEight_Mean = Data_Array_Custo_Mean_Umbigo[3,1]
Custo_Umbigo_SpeedEight_StdError = Data_Array_Custo_Mean_Umbigo[3,2]
Custo_Umbigo_SpeedEight_CILower = Data_Array_Custo_Mean_Umbigo[3,3]
Custo_Umbigo_SpeedEight_CIUpper = Data_Array_Custo_Mean_Umbigo[3,4]
Custo_Umbigo_SpeedEight_CI = Custo_Umbigo_SpeedEight_CIUpper - Custo_Umbigo_SpeedEight_Mean
    #All_Speeds
Custo_Umbigo_All_Speed_Mean = Data_Array_Custo_Mean_Umbigo[:,1]
Custo_Umbigo_All_Speed_StdError = Data_Array_Custo_Mean_Umbigo[:,2]
Custo_Umbigo_All_Speed_CILower = Data_Array_Custo_Mean_Umbigo[:,3]
Custo_Umbigo_All_Speed_CIUpper = Data_Array_Custo_Mean_Umbigo[:,4]
Custo_Umbigo_All_Speed_CI = Custo_Umbigo_All_Speed_CIUpper - Custo_Umbigo_All_Speed_Mean
Custo_Umbigo_All_Speed_Mean_list = Custo_Umbigo_All_Speed_Mean.tolist()
Custo_Umbigo_All_Speed_CI_list = Custo_Umbigo_All_Speed_CI.tolist()
Custo_Umbigo_All_Speed_Mean_withSpeedColumn = Data_Array_Custo_Mean_Umbigo[:,0:2]

    #XIFOIDE
File_Path_Custo_Mean_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Custo_Mean_Xifoide_withoutDutyFactorUnder50.txt")
Data_Custo_Mean_Xifoide = pd.read_csv(File_Path_Custo_Mean_Xifoide,delimiter="\t",header = 0)
Data_Array_Custo_Mean_Xifoide = np.array(Data_Custo_Mean_Xifoide)

        #0.2 m/s
Custo_Xifoide_SpeedTwo_Mean = Data_Array_Custo_Mean_Xifoide[0,1]
Custo_Xifoide_SpeedTwo_StdError = Data_Array_Custo_Mean_Xifoide[0,2]
Custo_Xifoide_SpeedTwo_CILower = Data_Array_Custo_Mean_Xifoide[0,3]
Custo_Xifoide_SpeedTwo_CIUpper = Data_Array_Custo_Mean_Xifoide[0,4]
Custo_Xifoide_SpeedTwo_CI = Custo_Xifoide_SpeedTwo_CIUpper - Custo_Xifoide_SpeedTwo_Mean
        #0.4 m/s
Custo_Xifoide_SpeedFour_Mean = Data_Array_Custo_Mean_Xifoide[1,1]
Custo_Xifoide_SpeedFour_StdError = Data_Array_Custo_Mean_Xifoide[1,2]
Custo_Xifoide_SpeedFour_CILower = Data_Array_Custo_Mean_Xifoide[1,3]
Custo_Xifoide_SpeedFour_CIUpper = Data_Array_Custo_Mean_Xifoide[1,4]
Custo_Xifoide_SpeedFour_CI = Custo_Xifoide_SpeedFour_CIUpper - Custo_Xifoide_SpeedFour_Mean
        #0.6 m/s
Custo_Xifoide_SpeedSix_Mean = Data_Array_Custo_Mean_Xifoide[2,1]
Custo_Xifoide_SpeedSix_StdError = Data_Array_Custo_Mean_Xifoide[2,2]
Custo_Xifoide_SpeedSix_CILower = Data_Array_Custo_Mean_Xifoide[2,3]
Custo_Xifoide_SpeedSix_CIUpper = Data_Array_Custo_Mean_Xifoide[2,4]
Custo_Xifoide_SpeedSix_CI = Custo_Xifoide_SpeedSix_CIUpper - Custo_Xifoide_SpeedSix_Mean
        #0.8 m/s
Custo_Xifoide_SpeedEight_Mean = Data_Array_Custo_Mean_Xifoide[3,1]
Custo_Xifoide_SpeedEight_StdError = Data_Array_Custo_Mean_Xifoide[3,2]
Custo_Xifoide_SpeedEight_CILower = Data_Array_Custo_Mean_Xifoide[3,3]
Custo_Xifoide_SpeedEight_CIUpper = Data_Array_Custo_Mean_Xifoide[3,4]
Custo_Xifoide_SpeedEight_CI = Custo_Xifoide_SpeedEight_CIUpper - Custo_Xifoide_SpeedEight_Mean
    #All_Speeds
Custo_Xifoide_All_Speed_Mean = Data_Array_Custo_Mean_Xifoide[:,1]
Custo_Xifoide_All_Speed_StdError = Data_Array_Custo_Mean_Xifoide[:,2]
Custo_Xifoide_All_Speed_CILower = Data_Array_Custo_Mean_Xifoide[:,3]
Custo_Xifoide_All_Speed_CIUpper = Data_Array_Custo_Mean_Xifoide[:,4]
Custo_Xifoide_All_Speed_CI = Custo_Xifoide_All_Speed_CIUpper - Custo_Xifoide_All_Speed_Mean
Custo_Xifoide_All_Speed_Mean_list = Custo_Xifoide_All_Speed_Mean.tolist()
Custo_Xifoide_All_Speed_CI_list = Custo_Xifoide_All_Speed_CI.tolist()
Custo_Xifoide_All_Speed_Mean_withSpeedColumn = Data_Array_Custo_Mean_Xifoide[:,0:2]


#Custo Per Speed
    #Mean
Custo_Two_Mean = np.array([Custo_Joelho_SpeedTwo_Mean, Custo_Quadril_SpeedTwo_Mean, Custo_Umbigo_SpeedTwo_Mean, Custo_Xifoide_SpeedTwo_Mean])
Custo_Four_Mean = [Custo_Joelho_SpeedFour_Mean, Custo_Quadril_SpeedFour_Mean, Custo_Umbigo_SpeedFour_Mean, Custo_Xifoide_SpeedFour_Mean]
Custo_Six_Mean = [Custo_Joelho_SpeedSix_Mean, Custo_Quadril_SpeedSix_Mean, Custo_Umbigo_SpeedSix_Mean, Custo_Xifoide_SpeedSix_Mean]
Custo_Eight_Mean= [Custo_Joelho_SpeedEight_Mean, Custo_Quadril_SpeedEight_Mean, Custo_Umbigo_SpeedEight_Mean, Custo_Xifoide_SpeedEight_Mean]

#Custo_Two_Mean_List = Custo_Two_Mean.tolist()
#Custo_Four_Mean_List= Custo_Four_Mean.tolist()
#Custo_Six_Mean_List= Custo_Six_Mean.tolist()
#Custo_Eight_Mean_List=Custo_Eight_Mean.tolist()

    #CI
Custo_Two_CI = np.array([Custo_Joelho_SpeedTwo_CI, Custo_Quadril_SpeedTwo_CI, Custo_Umbigo_SpeedTwo_CI, Custo_Xifoide_SpeedTwo_CI])
Custo_Four_CI = [Custo_Joelho_SpeedFour_CI, Custo_Quadril_SpeedFour_CI, Custo_Umbigo_SpeedFour_CI, Custo_Xifoide_SpeedFour_CI]
Custo_Six_CI = [Custo_Joelho_SpeedSix_CI, Custo_Quadril_SpeedSix_CI, Custo_Umbigo_SpeedSix_CI, Custo_Xifoide_SpeedSix_CI]
Custo_Eight_CI= [Custo_Joelho_SpeedEight_CI, Custo_Quadril_SpeedEight_CI, Custo_Umbigo_SpeedEight_CI, Custo_Xifoide_SpeedEight_CI]

#Custo_Two_CI_List = Custo_Two_CI.tolist()
#Custo_Four_CI_List= Custo_Four_CI.tolist()
#Custo_Six_CI_List= Custo_Six_CI.tolist()
#Custo_Eight_CI_List=Custo_Eight_CI.tolist()


#3º) TOTAL MEAN DATA METABOLIC POWER NET (POT MET)

    #JOELHO
File_Path_PotMet_Mean_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Pot_Met_NET_Mean_Joelho.txt")
Data_PotMet_Mean_Joelho = pd.read_csv(File_Path_PotMet_Mean_Joelho,delimiter="\t",header = 0)
Data_Array_PotMet_Mean_Joelho = np.array(Data_PotMet_Mean_Joelho)

        #0.2 m/s
PotMet_Joelho_SpeedTwo_Mean = Data_Array_PotMet_Mean_Joelho[0,1]
PotMet_Joelho_SpeedTwo_StdError = Data_Array_PotMet_Mean_Joelho[0,2]
PotMet_Joelho_SpeedTwo_CILower = Data_Array_PotMet_Mean_Joelho[0,3]
PotMet_Joelho_SpeedTwo_CIUpper = Data_Array_PotMet_Mean_Joelho[0,4]
PotMet_Joelho_SpeedTwo_CI = PotMet_Joelho_SpeedTwo_CIUpper - PotMet_Joelho_SpeedTwo_Mean
        #0.4 m/s
PotMet_Joelho_SpeedFour_Mean = Data_Array_PotMet_Mean_Joelho[1,1]
PotMet_Joelho_SpeedFour_StdError = Data_Array_PotMet_Mean_Joelho[1,2]
PotMet_Joelho_SpeedFour_CILower = Data_Array_PotMet_Mean_Joelho[1,3]
PotMet_Joelho_SpeedFour_CIUpper = Data_Array_PotMet_Mean_Joelho[1,4]
PotMet_Joelho_SpeedFour_CI = PotMet_Joelho_SpeedFour_CIUpper - PotMet_Joelho_SpeedFour_Mean
        #0.6 m/s
PotMet_Joelho_SpeedSix_Mean = Data_Array_PotMet_Mean_Joelho[2,1]
PotMet_Joelho_SpeedSix_StdError = Data_Array_PotMet_Mean_Joelho[2,2]
PotMet_Joelho_SpeedSix_CILower = Data_Array_PotMet_Mean_Joelho[2,3]
PotMet_Joelho_SpeedSix_CIUpper = Data_Array_PotMet_Mean_Joelho[2,4]
PotMet_Joelho_SpeedSix_CI = PotMet_Joelho_SpeedSix_CIUpper - PotMet_Joelho_SpeedSix_Mean
        #0.8 m/s
PotMet_Joelho_SpeedEight_Mean = Data_Array_PotMet_Mean_Joelho[3,1]
PotMet_Joelho_SpeedEight_StdError = Data_Array_PotMet_Mean_Joelho[3,2]
PotMet_Joelho_SpeedEight_CILower = Data_Array_PotMet_Mean_Joelho[3,3]
PotMet_Joelho_SpeedEight_CIUpper = Data_Array_PotMet_Mean_Joelho[3,4]
PotMet_Joelho_SpeedEight_CI = PotMet_Joelho_SpeedEight_CIUpper - PotMet_Joelho_SpeedEight_Mean
    #All_Speeds
PotMet_Joelho_All_Speed_Mean = Data_Array_PotMet_Mean_Joelho[:,1]
PotMet_Joelho_All_Speed_StdError = Data_Array_PotMet_Mean_Joelho[:,2]
PotMet_Joelho_All_Speed_CILower = Data_Array_PotMet_Mean_Joelho[:,3]
PotMet_Joelho_All_Speed_CIUpper = Data_Array_PotMet_Mean_Joelho[:,4]
PotMet_Joelho_All_Speed_CI = PotMet_Joelho_All_Speed_CIUpper - PotMet_Joelho_All_Speed_Mean
PotMet_Joelho_All_Speed_Mean_list = PotMet_Joelho_All_Speed_Mean.tolist()
PotMet_Joelho_All_Speed_CI_list = PotMet_Joelho_All_Speed_CI.tolist()
PotMet_Joelho_All_Speed_Mean_withSpeedColumn = Data_Array_PotMet_Mean_Joelho[:,0:2]

    #QUADRIL
File_Path_PotMet_Mean_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Pot_Met_NET_Mean_Quadril.txt")
Data_PotMet_Mean_Quadril = pd.read_csv(File_Path_PotMet_Mean_Quadril,delimiter="\t",header = 0)
Data_Array_PotMet_Mean_Quadril = np.array(Data_PotMet_Mean_Quadril)

        #0.2 m/s
PotMet_Quadril_SpeedTwo_Mean = Data_Array_PotMet_Mean_Quadril[0,1]
PotMet_Quadril_SpeedTwo_StdError = Data_Array_PotMet_Mean_Quadril[0,2]
PotMet_Quadril_SpeedTwo_CILower = Data_Array_PotMet_Mean_Quadril[0,3]
PotMet_Quadril_SpeedTwo_CIUpper = Data_Array_PotMet_Mean_Quadril[0,4]
PotMet_Quadril_SpeedTwo_CI = PotMet_Quadril_SpeedTwo_CIUpper - PotMet_Quadril_SpeedTwo_Mean
        #0.4 m/s
PotMet_Quadril_SpeedFour_Mean = Data_Array_PotMet_Mean_Quadril[1,1]
PotMet_Quadril_SpeedFour_StdError = Data_Array_PotMet_Mean_Quadril[1,2]
PotMet_Quadril_SpeedFour_CILower = Data_Array_PotMet_Mean_Quadril[1,3]
PotMet_Quadril_SpeedFour_CIUpper = Data_Array_PotMet_Mean_Quadril[1,4]
PotMet_Quadril_SpeedFour_CI = PotMet_Quadril_SpeedFour_CIUpper - PotMet_Quadril_SpeedFour_Mean
        #0.6 m/s
PotMet_Quadril_SpeedSix_Mean = Data_Array_PotMet_Mean_Quadril[2,1]
PotMet_Quadril_SpeedSix_StdError = Data_Array_PotMet_Mean_Quadril[2,2]
PotMet_Quadril_SpeedSix_CILower = Data_Array_PotMet_Mean_Quadril[2,3]
PotMet_Quadril_SpeedSix_CIUpper = Data_Array_PotMet_Mean_Quadril[2,4]
PotMet_Quadril_SpeedSix_CI = PotMet_Quadril_SpeedSix_CIUpper - PotMet_Quadril_SpeedSix_Mean
        #0.8 m/s
PotMet_Quadril_SpeedEight_Mean = Data_Array_PotMet_Mean_Quadril[3,1]
PotMet_Quadril_SpeedEight_StdError = Data_Array_PotMet_Mean_Quadril[3,2]
PotMet_Quadril_SpeedEight_CILower = Data_Array_PotMet_Mean_Quadril[3,3]
PotMet_Quadril_SpeedEight_CIUpper = Data_Array_PotMet_Mean_Quadril[3,4]
PotMet_Quadril_SpeedEight_CI = PotMet_Quadril_SpeedEight_CIUpper - PotMet_Quadril_SpeedEight_Mean
    #All_Speeds
PotMet_Quadril_All_Speed_Mean = Data_Array_PotMet_Mean_Quadril[:,1]
PotMet_Quadril_All_Speed_StdError = Data_Array_PotMet_Mean_Quadril[:,2]
PotMet_Quadril_All_Speed_CILower = Data_Array_PotMet_Mean_Quadril[:,3]
PotMet_Quadril_All_Speed_CIUpper = Data_Array_PotMet_Mean_Quadril[:,4]
PotMet_Quadril_All_Speed_CI = PotMet_Quadril_All_Speed_CIUpper - PotMet_Quadril_All_Speed_Mean
PotMet_Quadril_All_Speed_Mean_list = PotMet_Quadril_All_Speed_Mean.tolist()
PotMet_Quadril_All_Speed_CI_list = PotMet_Quadril_All_Speed_CI.tolist()
PotMet_Quadril_All_Speed_Mean_withSpeedColumn = Data_Array_PotMet_Mean_Quadril[:,0:2]

    #UMBIGO
File_Path_PotMet_Mean_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Pot_Met_NET_Mean_Umbigo.txt")
Data_PotMet_Mean_Umbigo = pd.read_csv(File_Path_PotMet_Mean_Umbigo,delimiter="\t",header = 0)
Data_Array_PotMet_Mean_Umbigo = np.array(Data_PotMet_Mean_Umbigo)

        #0.2 m/s
PotMet_Umbigo_SpeedTwo_Mean = Data_Array_PotMet_Mean_Umbigo[0,1]
PotMet_Umbigo_SpeedTwo_StdError = Data_Array_PotMet_Mean_Umbigo[0,2]
PotMet_Umbigo_SpeedTwo_CILower = Data_Array_PotMet_Mean_Umbigo[0,3]
PotMet_Umbigo_SpeedTwo_CIUpper = Data_Array_PotMet_Mean_Umbigo[0,4]
PotMet_Umbigo_SpeedTwo_CI = PotMet_Umbigo_SpeedTwo_CIUpper - PotMet_Umbigo_SpeedTwo_Mean
        #0.4 m/s
PotMet_Umbigo_SpeedFour_Mean = Data_Array_PotMet_Mean_Umbigo[1,1]
PotMet_Umbigo_SpeedFour_StdError = Data_Array_PotMet_Mean_Umbigo[1,2]
PotMet_Umbigo_SpeedFour_CILower = Data_Array_PotMet_Mean_Umbigo[1,3]
PotMet_Umbigo_SpeedFour_CIUpper = Data_Array_PotMet_Mean_Umbigo[1,4]
PotMet_Umbigo_SpeedFour_CI = PotMet_Umbigo_SpeedFour_CIUpper - PotMet_Umbigo_SpeedFour_Mean
        #0.6 m/s
PotMet_Umbigo_SpeedSix_Mean = Data_Array_PotMet_Mean_Umbigo[2,1]
PotMet_Umbigo_SpeedSix_StdError = Data_Array_PotMet_Mean_Umbigo[2,2]
PotMet_Umbigo_SpeedSix_CILower = Data_Array_PotMet_Mean_Umbigo[2,3]
PotMet_Umbigo_SpeedSix_CIUpper = Data_Array_PotMet_Mean_Umbigo[2,4]
PotMet_Umbigo_SpeedSix_CI = PotMet_Umbigo_SpeedSix_CIUpper - PotMet_Umbigo_SpeedSix_Mean
        #0.8 m/s
PotMet_Umbigo_SpeedEight_Mean = Data_Array_PotMet_Mean_Umbigo[3,1]
PotMet_Umbigo_SpeedEight_StdError = Data_Array_PotMet_Mean_Umbigo[3,2]
PotMet_Umbigo_SpeedEight_CILower = Data_Array_PotMet_Mean_Umbigo[3,3]
PotMet_Umbigo_SpeedEight_CIUpper = Data_Array_PotMet_Mean_Umbigo[3,4]
PotMet_Umbigo_SpeedEight_CI = PotMet_Umbigo_SpeedEight_CIUpper - PotMet_Umbigo_SpeedEight_Mean
    #All_Speeds
PotMet_Umbigo_All_Speed_Mean = Data_Array_PotMet_Mean_Umbigo[:,1]
PotMet_Umbigo_All_Speed_StdError = Data_Array_PotMet_Mean_Umbigo[:,2]
PotMet_Umbigo_All_Speed_CILower = Data_Array_PotMet_Mean_Umbigo[:,3]
PotMet_Umbigo_All_Speed_CIUpper = Data_Array_PotMet_Mean_Umbigo[:,4]
PotMet_Umbigo_All_Speed_CI = PotMet_Umbigo_All_Speed_CIUpper - PotMet_Umbigo_All_Speed_Mean
PotMet_Umbigo_All_Speed_Mean_list = PotMet_Umbigo_All_Speed_Mean.tolist()
PotMet_Umbigo_All_Speed_CI_list = PotMet_Umbigo_All_Speed_CI.tolist()
PotMet_Umbigo_All_Speed_Mean_withSpeedColumn = Data_Array_PotMet_Mean_Umbigo[:,0:2]

    #XIFOIDE
File_Path_PotMet_Mean_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Pot_Met_NET_Mean_Xifoide_withoutDutyFactorUnder50.txt")
Data_PotMet_Mean_Xifoide = pd.read_csv(File_Path_PotMet_Mean_Xifoide,delimiter="\t",header = 0)
Data_Array_PotMet_Mean_Xifoide = np.array(Data_PotMet_Mean_Xifoide)

        #0.2 m/s
PotMet_Xifoide_SpeedTwo_Mean = Data_Array_PotMet_Mean_Xifoide[0,1]
PotMet_Xifoide_SpeedTwo_StdError = Data_Array_PotMet_Mean_Xifoide[0,2]
PotMet_Xifoide_SpeedTwo_CILower = Data_Array_PotMet_Mean_Xifoide[0,3]
PotMet_Xifoide_SpeedTwo_CIUpper = Data_Array_PotMet_Mean_Xifoide[0,4]
PotMet_Xifoide_SpeedTwo_CI = PotMet_Xifoide_SpeedTwo_CIUpper - PotMet_Xifoide_SpeedTwo_Mean
        #0.4 m/s
PotMet_Xifoide_SpeedFour_Mean = Data_Array_PotMet_Mean_Xifoide[1,1]
PotMet_Xifoide_SpeedFour_StdError = Data_Array_PotMet_Mean_Xifoide[1,2]
PotMet_Xifoide_SpeedFour_CILower = Data_Array_PotMet_Mean_Xifoide[1,3]
PotMet_Xifoide_SpeedFour_CIUpper = Data_Array_PotMet_Mean_Xifoide[1,4]
PotMet_Xifoide_SpeedFour_CI = PotMet_Xifoide_SpeedFour_CIUpper - PotMet_Xifoide_SpeedFour_Mean
        #0.6 m/s
PotMet_Xifoide_SpeedSix_Mean = Data_Array_PotMet_Mean_Xifoide[2,1]
PotMet_Xifoide_SpeedSix_StdError = Data_Array_PotMet_Mean_Xifoide[2,2]
PotMet_Xifoide_SpeedSix_CILower = Data_Array_PotMet_Mean_Xifoide[2,3]
PotMet_Xifoide_SpeedSix_CIUpper = Data_Array_PotMet_Mean_Xifoide[2,4]
PotMet_Xifoide_SpeedSix_CI = PotMet_Xifoide_SpeedSix_CIUpper - PotMet_Xifoide_SpeedSix_Mean
        #0.8 m/s
PotMet_Xifoide_SpeedEight_Mean = Data_Array_PotMet_Mean_Xifoide[3,1]
PotMet_Xifoide_SpeedEight_StdError = Data_Array_PotMet_Mean_Xifoide[3,2]
PotMet_Xifoide_SpeedEight_CILower = Data_Array_PotMet_Mean_Xifoide[3,3]
PotMet_Xifoide_SpeedEight_CIUpper = Data_Array_PotMet_Mean_Xifoide[3,4]
PotMet_Xifoide_SpeedEight_CI = PotMet_Xifoide_SpeedEight_CIUpper - PotMet_Xifoide_SpeedEight_Mean
    #All_Speeds
PotMet_Xifoide_All_Speed_Mean = Data_Array_PotMet_Mean_Xifoide[:,1]
PotMet_Xifoide_All_Speed_StdError = Data_Array_PotMet_Mean_Xifoide[:,2]
PotMet_Xifoide_All_Speed_CILower = Data_Array_PotMet_Mean_Xifoide[:,3]
PotMet_Xifoide_All_Speed_CIUpper = Data_Array_PotMet_Mean_Xifoide[:,4]
PotMet_Xifoide_All_Speed_CI = PotMet_Xifoide_All_Speed_CIUpper - PotMet_Xifoide_All_Speed_Mean
PotMet_Xifoide_All_Speed_Mean_list = PotMet_Xifoide_All_Speed_Mean.tolist()
PotMet_Xifoide_All_Speed_CI_list = PotMet_Xifoide_All_Speed_CI.tolist()
PotMet_Xifoide_All_Speed_Mean_withSpeedColumn = Data_Array_PotMet_Mean_Xifoide[:,0:2]


#4º) DEPTHS MEAN VALUES IN METRIC SCALE AND PERCENTUAL OF STATURE

    #METRIC SCALE
File_Path_Profundidade_Meters = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Profundidade_in_Meters.txt")
Data_Profundidade_Meters = pd.read_csv(File_Path_Profundidade_Meters,delimiter="\t",header = 0)
Data_Array_Profundidade_Meters = np.array(Data_Profundidade_Meters)

Depth_Joelho_Meters = Data_Array_Profundidade_Meters[0,0]
Depth_Quadril_Meters = Data_Array_Profundidade_Meters[1,0]
Depth_Umbigo_Meters = Data_Array_Profundidade_Meters[2,0]
Depth_Xifoide_Meters = Data_Array_Profundidade_Meters[3,0]

Depth_Meters_ALL = np.array([Depth_Joelho_Meters, Depth_Quadril_Meters, Depth_Umbigo_Meters, Depth_Xifoide_Meters])



    #PERCENTUAL OF STATURE
File_Path_Profundidade_Percentual = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Profundidade_in_Percentual_of_Stature.txt")
Data_Profundidade_Percentual  = pd.read_csv(File_Path_Profundidade_Percentual,delimiter="\t",header = 0)
Data_Array_Profundidade_Percentual = np.array(Data_Profundidade_Percentual)

Depth_Joelho_Percentual = Data_Array_Profundidade_Percentual[0,1] * 100
Depth_Quadril_Percentual = Data_Array_Profundidade_Percentual[1,1] * 100
Depth_Umbigo_Percentual = Data_Array_Profundidade_Percentual[2,1] * 100
Depth_Xifoide_Percentual = Data_Array_Profundidade_Percentual[3,1] * 100


#5º) VAS MEAN SPEED PER DEPTH
File_Path_VAS = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/VAS_Mean.txt")
Data_VAS  = pd.read_csv(File_Path_VAS,delimiter="\t",header = 0)
Data_Array_VAS = np.array(Data_VAS)

VAS_Joelho = Data_Array_VAS [0,1]
VAS_Quadril = Data_Array_VAS [1,1]
VAS_Umbigo = Data_Array_VAS [2,1]
VAS_Xifoide = Data_Array_VAS [3,1]


#6º) ARDIGÒ'S (2003) AND ZAMPARO'S (1992) CURVE OF COST OF TRANSPORT

def Custo_Ardigo(v):
    i = 0.0
    a = np.exp(4.911*i)
    b = np.exp(3.416*i)
    c = (45.72 * (i**2)) + (18.9 * i)
    return (1.866*a*(v**2)) - (3.773*b*v) + c + 5.8

def Custo_Zamparo(v):
     return (0.11*(v**2)) - (0.99*v) + 4.5

Custo_Ardigo_Two = Custo_Ardigo(0.2)
Custo_Ardigo_Four = Custo_Ardigo(0.4)
Custo_Ardigo_Six = Custo_Ardigo(0.6)
Custo_Ardigo_Eight = Custo_Ardigo(0.8)

X_Custo_Ardigo = np.linspace(0.2, 1.8, 50)
Y_Custo_Ardigo = Custo_Ardigo(X_Custo_Ardigo)

Custo_Zamparo_Two = Custo_Zamparo(0.2)
Custo_Zamparo_Four = Custo_Zamparo(0.4)
Custo_Zamparo_Six = Custo_Zamparo(0.6)
Custo_Zamparo_Eight = Custo_Zamparo(0.8)


#7º)  DRAG_F_STRIDE

    #JOELHO
File_Path_Drag_F_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Drag_F_Stride_Mean_Joelho.txt")
Data_Drag_F_Joelho = pd.read_csv(File_Path_Drag_F_Joelho,delimiter="\t",header = 0)
Data_Array_Drag_F_Joelho = np.array(Data_Drag_F_Joelho)

    # 0.2 m/s
Drag_F_Joelho_SpeedTwo_Mean = Data_Array_Drag_F_Joelho[0,1]
Drag_F_Joelho_SpeedTwo_CIUpper = Data_Array_Drag_F_Joelho[0,4]
Drag_F_Joelho_SpeedTwo_CI = Drag_F_Joelho_SpeedTwo_CIUpper - Drag_F_Joelho_SpeedTwo_Mean
    #0.4 m/s
Drag_F_Joelho_SpeedFour_Mean = Data_Array_Drag_F_Joelho[1,1]
Drag_F_Joelho_SpeedFour_CIUpper = Data_Array_Drag_F_Joelho[1,4]
Drag_F_Joelho_SpeedFour_CI = Drag_F_Joelho_SpeedFour_CIUpper - Drag_F_Joelho_SpeedFour_Mean
    #0.6 m/s
Drag_F_Joelho_SpeedSix_Mean = Data_Array_Drag_F_Joelho[2,1]
Drag_F_Joelho_SpeedSix_CIUpper = Data_Array_Drag_F_Joelho[2,4]
Drag_F_Joelho_SpeedSix_CI = Drag_F_Joelho_SpeedSix_CIUpper - Drag_F_Joelho_SpeedSix_Mean
    #0.8 m/s
Drag_F_Joelho_SpeedEight_Mean = Data_Array_Drag_F_Joelho[3,1]
Drag_F_Joelho_SpeedEight_CIUpper = Data_Array_Drag_F_Joelho[3,4]
Drag_F_Joelho_SpeedEight_CI = Drag_F_Joelho_SpeedEight_CIUpper - Drag_F_Joelho_SpeedEight_Mean


    #QUADRIL
File_Path_Drag_F_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Drag_F_Stride_Mean_Quadril.txt")
Data_Drag_F_Quadril = pd.read_csv(File_Path_Drag_F_Quadril,delimiter="\t",header = 0)
Data_Array_Drag_F_Quadril = np.array(Data_Drag_F_Quadril)

    # 0.2 m/s
Drag_F_Quadril_SpeedTwo_Mean = Data_Array_Drag_F_Quadril[0,1]
Drag_F_Quadril_SpeedTwo_CIUpper = Data_Array_Drag_F_Quadril[0,4]
Drag_F_Quadril_SpeedTwo_CI = Drag_F_Quadril_SpeedTwo_CIUpper - Drag_F_Quadril_SpeedTwo_Mean
    #0.4 m/s
Drag_F_Quadril_SpeedFour_Mean = Data_Array_Drag_F_Quadril[1,1]
Drag_F_Quadril_SpeedFour_CIUpper = Data_Array_Drag_F_Quadril[1,4]
Drag_F_Quadril_SpeedFour_CI = Drag_F_Quadril_SpeedFour_CIUpper - Drag_F_Quadril_SpeedFour_Mean
    #0.6 m/s
Drag_F_Quadril_SpeedSix_Mean = Data_Array_Drag_F_Quadril[2,1]
Drag_F_Quadril_SpeedSix_CIUpper = Data_Array_Drag_F_Quadril[2,4]
Drag_F_Quadril_SpeedSix_CI = Drag_F_Quadril_SpeedSix_CIUpper - Drag_F_Quadril_SpeedSix_Mean
    #0.8 m/s
Drag_F_Quadril_SpeedEight_Mean = Data_Array_Drag_F_Quadril[3,1]
Drag_F_Quadril_SpeedEight_CIUpper = Data_Array_Drag_F_Quadril[3,4]
Drag_F_Quadril_SpeedEight_CI = Drag_F_Quadril_SpeedEight_CIUpper - Drag_F_Quadril_SpeedEight_Mean

    #UMBIGO
File_Path_Drag_F_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Drag_F_Stride_Mean_Umbigo.txt")
Data_Drag_F_Umbigo = pd.read_csv(File_Path_Drag_F_Umbigo,delimiter="\t",header = 0)
Data_Array_Drag_F_Umbigo = np.array(Data_Drag_F_Umbigo)

    # 0.2 m/s
Drag_F_Umbigo_SpeedTwo_Mean = Data_Array_Drag_F_Umbigo[0,1]
Drag_F_Umbigo_SpeedTwo_CIUpper = Data_Array_Drag_F_Umbigo[0,4]
Drag_F_Umbigo_SpeedTwo_CI = Drag_F_Umbigo_SpeedTwo_CIUpper - Drag_F_Umbigo_SpeedTwo_Mean
    #0.4 m/s
Drag_F_Umbigo_SpeedFour_Mean = Data_Array_Drag_F_Umbigo[1,1]
Drag_F_Umbigo_SpeedFour_CIUpper = Data_Array_Drag_F_Umbigo[1,4]
Drag_F_Umbigo_SpeedFour_CI = Drag_F_Umbigo_SpeedFour_CIUpper - Drag_F_Umbigo_SpeedFour_Mean
    #0.6 m/s
Drag_F_Umbigo_SpeedSix_Mean = Data_Array_Drag_F_Umbigo[2,1]
Drag_F_Umbigo_SpeedSix_CIUpper = Data_Array_Drag_F_Umbigo[2,4]
Drag_F_Umbigo_SpeedSix_CI = Drag_F_Umbigo_SpeedSix_CIUpper - Drag_F_Umbigo_SpeedSix_Mean
    #0.8 m/s
Drag_F_Umbigo_SpeedEight_Mean = Data_Array_Drag_F_Umbigo[3,1]
Drag_F_Umbigo_SpeedEight_CIUpper = Data_Array_Drag_F_Umbigo[3,4]
Drag_F_Umbigo_SpeedEight_CI = Drag_F_Umbigo_SpeedEight_CIUpper - Drag_F_Umbigo_SpeedEight_Mean

    #XIFOIDE
File_Path_Drag_F_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Drag_F_Stride_Mean_Xifoide.txt")
Data_Drag_F_Xifoide = pd.read_csv(File_Path_Drag_F_Xifoide,delimiter="\t",header = 0)
Data_Array_Drag_F_Xifoide = np.array(Data_Drag_F_Xifoide)

    # 0.2 m/s
Drag_F_Xifoide_SpeedTwo_Mean = Data_Array_Drag_F_Xifoide[0,1]
Drag_F_Xifoide_SpeedTwo_CIUpper = Data_Array_Drag_F_Xifoide[0,4]
Drag_F_Xifoide_SpeedTwo_CI = Drag_F_Xifoide_SpeedTwo_CIUpper - Drag_F_Xifoide_SpeedTwo_Mean
    #0.4 m/s
Drag_F_Xifoide_SpeedFour_Mean = Data_Array_Drag_F_Xifoide[1,1]
Drag_F_Xifoide_SpeedFour_CIUpper = Data_Array_Drag_F_Xifoide[1,4]
Drag_F_Xifoide_SpeedFour_CI = Drag_F_Xifoide_SpeedFour_CIUpper - Drag_F_Xifoide_SpeedFour_Mean
    #0.6 m/s
Drag_F_Xifoide_SpeedSix_Mean = Data_Array_Drag_F_Xifoide[2,1]
Drag_F_Xifoide_SpeedSix_CIUpper = Data_Array_Drag_F_Xifoide[2,4]
Drag_F_Xifoide_SpeedSix_CI = Drag_F_Xifoide_SpeedSix_CIUpper - Drag_F_Xifoide_SpeedSix_Mean
    #0.8 m/s
Drag_F_Xifoide_SpeedEight_Mean = Data_Array_Drag_F_Xifoide[3,1]
Drag_F_Xifoide_SpeedEight_CIUpper = Data_Array_Drag_F_Xifoide[3,4]
Drag_F_Xifoide_SpeedEight_CI = Drag_F_Xifoide_SpeedEight_CIUpper - Drag_F_Xifoide_SpeedEight_Mean


#Drag Force Per Speed
    #Mean
Drag_F_Two_Mean = [Drag_F_Joelho_SpeedTwo_Mean, Drag_F_Quadril_SpeedTwo_Mean, Drag_F_Umbigo_SpeedTwo_Mean, Drag_F_Xifoide_SpeedTwo_Mean]
Drag_F_Four_Mean = [Drag_F_Joelho_SpeedFour_Mean, Drag_F_Quadril_SpeedFour_Mean, Drag_F_Umbigo_SpeedFour_Mean, Drag_F_Xifoide_SpeedFour_Mean]
Drag_F_Six_Mean = [Drag_F_Joelho_SpeedSix_Mean, Drag_F_Quadril_SpeedSix_Mean, Drag_F_Umbigo_SpeedSix_Mean, Drag_F_Xifoide_SpeedSix_Mean]
Drag_F_Eight_Mean= [Drag_F_Joelho_SpeedEight_Mean, Drag_F_Quadril_SpeedEight_Mean, Drag_F_Umbigo_SpeedEight_Mean, Drag_F_Xifoide_SpeedEight_Mean]

#Drag_F_Two_Mean_List = Drag_F_Two_Mean.tolist()
#Drag_F_Four_Mean_List= Drag_F_Four_Mean.tolist()
#Drag_F_Six_Mean_List= Drag_F_Six_Mean.tolist()
#Drag_F_Eight_Mean_List= Drag_F_Eight_Mean.tolist()

    #CI
Drag_F_Two_CI = [Drag_F_Joelho_SpeedTwo_CI, Drag_F_Quadril_SpeedTwo_CI, Drag_F_Umbigo_SpeedTwo_CI, Drag_F_Xifoide_SpeedTwo_CI]
Drag_F_Four_CI = [Drag_F_Joelho_SpeedFour_CI, Drag_F_Quadril_SpeedFour_CI, Drag_F_Umbigo_SpeedFour_CI, Drag_F_Xifoide_SpeedFour_CI]
Drag_F_Six_CI = [Drag_F_Joelho_SpeedSix_CI, Drag_F_Quadril_SpeedSix_CI, Drag_F_Umbigo_SpeedSix_CI, Drag_F_Xifoide_SpeedSix_CI]
Drag_F_Eight_CI= [Drag_F_Joelho_SpeedEight_CI, Drag_F_Quadril_SpeedEight_CI, Drag_F_Umbigo_SpeedEight_CI, Drag_F_Xifoide_SpeedEight_CI]

#Drag_F_Two_CI_List = Drag_F_Two_CI.tolist()
#Drag_F_Four_CI_List= Drag_F_Four_CI.tolist()
#Drag_F_Six_CI_List= Drag_F_Six_CI.tolist()
#Drag_F_Eight_CI_List= Drag_F_Eight_CI.tolist()


#7º)  DRAG_F_STRIDE_per_METER

    #JOELHO
File_Path_Drag_F_per_Meter_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Drag_F_Stride_per_Meter_Mean_Joelho.txt")
Data_Drag_F_per_Meter_Joelho = pd.read_csv(File_Path_Drag_F_per_Meter_Joelho,delimiter="\t",header = 0)
Data_Array_Drag_F_per_Meter_Joelho = np.array(Data_Drag_F_per_Meter_Joelho)

Drag_F_per_Meter_Joelho_SpeedTwo_Mean = Data_Array_Drag_F_per_Meter_Joelho[0,1]
Drag_F_per_Meter_Joelho_SpeedFour_Mean = Data_Array_Drag_F_per_Meter_Joelho[1,1]
Drag_F_per_Meter_Joelho_SpeedSix_Mean = Data_Array_Drag_F_per_Meter_Joelho[2,1]
Drag_F_per_Meter_Joelho_SpeedEight_Mean = Data_Array_Drag_F_per_Meter_Joelho[3,1]

    #QUADRIL
File_Path_Drag_F_per_Meter_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Drag_F_Stride_per_Meter_Mean_Quadril.txt")
Data_Drag_F_per_Meter_Quadril = pd.read_csv(File_Path_Drag_F_per_Meter_Quadril,delimiter="\t",header = 0)
Data_Array_Drag_F_per_Meter_Quadril = np.array(Data_Drag_F_per_Meter_Quadril)

Drag_F_per_Meter_Quadril_SpeedTwo_Mean = Data_Array_Drag_F_per_Meter_Quadril[0,1]
Drag_F_per_Meter_Quadril_SpeedFour_Mean = Data_Array_Drag_F_per_Meter_Quadril[1,1]
Drag_F_per_Meter_Quadril_SpeedSix_Mean = Data_Array_Drag_F_per_Meter_Quadril[2,1]
Drag_F_per_Meter_Quadril_SpeedEight_Mean = Data_Array_Drag_F_per_Meter_Quadril[3,1]

    #UMBIGO
File_Path_Drag_F_per_Meter_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Drag_F_Stride_per_Meter_Mean_Umbigo.txt")
Data_Drag_F_per_Meter_Umbigo = pd.read_csv(File_Path_Drag_F_per_Meter_Umbigo,delimiter="\t",header = 0)
Data_Array_Drag_F_per_Meter_Umbigo = np.array(Data_Drag_F_per_Meter_Umbigo)

Drag_F_per_Meter_Umbigo_SpeedTwo_Mean = Data_Array_Drag_F_per_Meter_Umbigo[0,1]
Drag_F_per_Meter_Umbigo_SpeedFour_Mean = Data_Array_Drag_F_per_Meter_Umbigo[1,1]
Drag_F_per_Meter_Umbigo_SpeedSix_Mean = Data_Array_Drag_F_per_Meter_Umbigo[2,1]
Drag_F_per_Meter_Umbigo_SpeedEight_Mean = Data_Array_Drag_F_per_Meter_Umbigo[3,1]

    #XIFOIDE
File_Path_Drag_F_per_Meter_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/Drag_F_Stride_per_Meter_Mean_Xifoide_withDutyUnder50.txt")
Data_Drag_F_per_Meter_Xifoide = pd.read_csv(File_Path_Drag_F_per_Meter_Xifoide,delimiter="\t",header = 0)
Data_Array_Drag_F_per_Meter_Xifoide = np.array(Data_Drag_F_per_Meter_Xifoide)

Drag_F_per_Meter_Xifoide_SpeedTwo_Mean = Data_Array_Drag_F_per_Meter_Xifoide[0,1]
Drag_F_per_Meter_Xifoide_SpeedFour_Mean = Data_Array_Drag_F_per_Meter_Xifoide[1,1]
Drag_F_per_Meter_Xifoide_SpeedSix_Mean = Data_Array_Drag_F_per_Meter_Xifoide[2,1]
Drag_F_per_Meter_Xifoide_SpeedEight_Mean = Data_Array_Drag_F_per_Meter_Xifoide[3,1]


#9º)  GRF_V PEAK

    #JOELHO
File_Path_GRF_V_Peak_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/GRF_V_Peak_Joelho.txt")
Data_GRF_V_Peak_Joelho = pd.read_csv(File_Path_GRF_V_Peak_Joelho,delimiter="\t",header = 0)
Data_Array_GRF_V_Peak_Joelho = np.array(Data_GRF_V_Peak_Joelho)

GRF_V_Peak_Joelho_SpeedTwo_Mean = Data_Array_GRF_V_Peak_Joelho[0,1]
GRF_V_Peak_Joelho_SpeedFour_Mean = Data_Array_GRF_V_Peak_Joelho[1,1]
GRF_V_Peak_Joelho_SpeedSix_Mean = Data_Array_GRF_V_Peak_Joelho[2,1]
GRF_V_Peak_Joelho_SpeedEight_Mean = Data_Array_GRF_V_Peak_Joelho[3,1]

    #QUADRIL
File_Path_GRF_V_Peak_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/GRF_V_Peak_Quadril.txt")
Data_GRF_V_Peak_Quadril = pd.read_csv(File_Path_GRF_V_Peak_Quadril,delimiter="\t",header = 0)
Data_Array_GRF_V_Peak_Quadril = np.array(Data_GRF_V_Peak_Quadril)

GRF_V_Peak_Quadril_SpeedTwo_Mean = Data_Array_GRF_V_Peak_Quadril[0,1]
GRF_V_Peak_Quadril_SpeedFour_Mean = Data_Array_GRF_V_Peak_Quadril[1,1]
GRF_V_Peak_Quadril_SpeedSix_Mean = Data_Array_GRF_V_Peak_Quadril[2,1]
GRF_V_Peak_Quadril_SpeedEight_Mean = Data_Array_GRF_V_Peak_Quadril[3,1]

    #UMBIGO
File_Path_GRF_V_Peak_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/GRF_V_Peak_Umbigo.txt")
Data_GRF_V_Peak_Umbigo = pd.read_csv(File_Path_GRF_V_Peak_Umbigo,delimiter="\t",header = 0)
Data_Array_GRF_V_Peak_Umbigo = np.array(Data_GRF_V_Peak_Umbigo)

GRF_V_Peak_Umbigo_SpeedTwo_Mean = Data_Array_GRF_V_Peak_Umbigo[0,1]
GRF_V_Peak_Umbigo_SpeedFour_Mean = Data_Array_GRF_V_Peak_Umbigo[1,1]
GRF_V_Peak_Umbigo_SpeedSix_Mean = Data_Array_GRF_V_Peak_Umbigo[2,1]
GRF_V_Peak_Umbigo_SpeedEight_Mean = Data_Array_GRF_V_Peak_Umbigo[3,1]

    #XIFOIDE
File_Path_GRF_V_Peak_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/GRF_V_Peak_Xifoide_withDutyUnder50.txt")
Data_GRF_V_Peak_Xifoide = pd.read_csv(File_Path_GRF_V_Peak_Xifoide,delimiter="\t",header = 0)
Data_Array_GRF_V_Peak_Xifoide = np.array(Data_GRF_V_Peak_Xifoide)

GRF_V_Peak_Xifoide_SpeedTwo_Mean = Data_Array_GRF_V_Peak_Xifoide[0,1]
GRF_V_Peak_Xifoide_SpeedFour_Mean = Data_Array_GRF_V_Peak_Xifoide[1,1]
GRF_V_Peak_Xifoide_SpeedSix_Mean = Data_Array_GRF_V_Peak_Xifoide[2,1]
GRF_V_Peak_Xifoide_SpeedEight_Mean = Data_Array_GRF_V_Peak_Xifoide[3,1]


#10º)  GRF_V MEAN (APPARENT BODY WEIGHT)

File_Path_GRF_V_MEAN_ALL_DEPTHS = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/GRF_V_Mean_ALL_DEPTHS.txt")
Data_GRF_V_MEAN_ALL_DEPTHS = pd.read_csv(File_Path_GRF_V_MEAN_ALL_DEPTHS,delimiter="\t",header = 0)
Data_Array_GRF_V_MEAN_ALL_DEPTHS = np.array(Data_GRF_V_MEAN_ALL_DEPTHS)

#JOELHO
GRF_V_MEAN_Joelho_Mean = Data_Array_GRF_V_MEAN_ALL_DEPTHS[0,1]
GRF_V_MEAN_Joelho_StdError = Data_Array_GRF_V_MEAN_ALL_DEPTHS[0,2]
GRF_V_MEAN_Joelho_CIUpper = Data_Array_GRF_V_MEAN_ALL_DEPTHS[0,4]
GRF_V_MEAN_Joelho_CI = GRF_V_MEAN_Joelho_CIUpper - GRF_V_MEAN_Joelho_Mean

#QUADRIL
GRF_V_MEAN_Quadril_Mean = Data_Array_GRF_V_MEAN_ALL_DEPTHS[1,1]
GRF_V_MEAN_Quadril_StdError = Data_Array_GRF_V_MEAN_ALL_DEPTHS[1,2]
GRF_V_MEAN_Quadril_CIUpper = Data_Array_GRF_V_MEAN_ALL_DEPTHS[1,4]
GRF_V_MEAN_Quadril_CI = GRF_V_MEAN_Quadril_CIUpper - GRF_V_MEAN_Quadril_Mean

#UMBIGO
GRF_V_MEAN_Umbigo_Mean = Data_Array_GRF_V_MEAN_ALL_DEPTHS[2,1]
GRF_V_MEAN_Umbigo_StdError = Data_Array_GRF_V_MEAN_ALL_DEPTHS[2,2]
GRF_V_MEAN_Umbigo_CIUpper = Data_Array_GRF_V_MEAN_ALL_DEPTHS[2,4]
GRF_V_MEAN_Umbigo_CI = GRF_V_MEAN_Umbigo_CIUpper - GRF_V_MEAN_Umbigo_Mean

#XIFOIDE
GRF_V_MEAN_Xifoide_Mean = Data_Array_GRF_V_MEAN_ALL_DEPTHS[3,1]
GRF_V_MEAN_Xifoide_StdError = Data_Array_GRF_V_MEAN_ALL_DEPTHS[3,2]
GRF_V_MEAN_Xifoide_CIUpper = Data_Array_GRF_V_MEAN_ALL_DEPTHS[3,4]
GRF_V_MEAN_Xifoide_CI = GRF_V_MEAN_Xifoide_CIUpper - GRF_V_MEAN_Xifoide_Mean

#ALL DEPTHS
GRF_V_MEAN_Mean = [GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]
#GRF_V_MEAN_Mean_List = GRF_V_MEAN_Mean.tolist()

GRF_V_MEAN_CI = [GRF_V_MEAN_Joelho_CI, GRF_V_MEAN_Quadril_CI, GRF_V_MEAN_Umbigo_CI, GRF_V_MEAN_Xifoide_CI]
#GRF_V_MEAN_CI_List = GRF_V_MEAN_CI.tolist()

#11º)  TOTAL SUM FORCES (DRAG FORCE AND GRF_V_MEAN)

#JOELHO
File_Path_TOTAL_SUM_FORCES_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics/TOTAL_SUM_FORCES_Drag_GRFVMean_Joelho.txt")
Data_TOTAL_SUM_FORCES_Joelho = pd.read_csv(File_Path_TOTAL_SUM_FORCES_Joelho,delimiter="\t",header = 0)
Data_Array_TOTAL_SUM_FORCES_Joelho = np.array(Data_TOTAL_SUM_FORCES_Joelho)

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



# 12º) FIGURES


#FIGURE 01
#COST AND DEPTH IN ANATOMICAL SCALE

#fig, ax = plt.subplots()
#fig.canvas.set_window_title('Cost of Transport per Depth in Anatomical Scale')
#ax.errorbar([1, 2, 3, 4], [Custo_Joelho_SpeedTwo_Mean, Custo_Quadril_SpeedTwo_Mean, Custo_Umbigo_SpeedTwo_Mean, Custo_Xifoide_SpeedTwo_Mean], yerr=CI_Two, fmt='--', color='goldenrod', linewidth=2.0, )
#ax.errorbar([1, 2, 3, 4], [Custo_Joelho_SpeedFour_Mean, Custo_Quadril_SpeedFour_Mean, Custo_Umbigo_SpeedFour_Mean, Custo_Xifoide_SpeedFour_Mean], yerr=CI_Four, fmt='-.', color='limegreen', linewidth=2.0)
#ax.errorbar([1, 2, 3, 4], [Custo_Joelho_SpeedSix_Mean, Custo_Quadril_SpeedSix_Mean, Custo_Umbigo_SpeedSix_Mean, Custo_Xifoide_SpeedSix_Mean],yerr=CI_Six, fmt='--', color='mediumorchid', linewidth=2.0)
#ax.errorbar([1, 2, 3, 4], [Custo_Joelho_SpeedEight_Mean, Custo_Quadril_SpeedEight_Mean, Custo_Umbigo_SpeedEight_Mean, Custo_Xifoide_SpeedEight_Mean],yerr=CI_Eight, fmt='--', color='dodgerblue', linewidth=2.0)

#xticks = [1, 2, 3, 4]
#xlabels = ["Knee", "Hip", "Umbilical","Xiphoid"]
#plt.xticks(xticks, xlabels)
#ax.set_ylim([0, 12])
#fig.suptitle('Cost of Transport', fontsize=20)
#plt.xlabel('Depths', fontsize=18)
#plt.ylabel('Cost of Transport (J/kg/m)', fontsize=16)
#ax.tick_params(labelsize=14)
#line_labels = ['0.2 m/s','0.4 m/s','0.6 m/s', '0.8 m/s']
#plt.legend(labels = line_labels, loc = 'best', title = 'Speed', fontsize=14)




'''
#FIGURE 02
#COST AND DEPTH IN METRIC SCALE


fig, ax = plt.subplots()
fig.canvas.set_window_title('Cost of Transport per Depth in Metric Scale')
ax.errorbar([Depth_Joelho_Meters, Depth_Quadril_Meters, Depth_Umbigo_Meters, Depth_Xifoide_Meters], [Custo_Joelho_SpeedTwo_Mean, Custo_Quadril_SpeedTwo_Mean, Custo_Umbigo_SpeedTwo_Mean, Custo_Xifoide_SpeedTwo_Mean], yerr=Custo_Two_CI, fmt='--', color='goldenrod', label="0.2", linewidth=2.0, )
ax.errorbar([Depth_Joelho_Meters, Depth_Quadril_Meters, Depth_Umbigo_Meters, Depth_Xifoide_Meters], [Custo_Joelho_SpeedFour_Mean, Custo_Quadril_SpeedFour_Mean, Custo_Umbigo_SpeedFour_Mean, Custo_Xifoide_SpeedFour_Mean], yerr=Custo_Four_CI, fmt='-.', color='limegreen', label="0.4", linewidth=2.0)
ax.errorbar([Depth_Joelho_Meters, Depth_Quadril_Meters, Depth_Umbigo_Meters, Depth_Xifoide_Meters], [Custo_Joelho_SpeedSix_Mean, Custo_Quadril_SpeedSix_Mean, Custo_Umbigo_SpeedSix_Mean, Custo_Xifoide_SpeedSix_Mean],yerr=Custo_Six_CI, fmt='--', color='mediumorchid', label="0.6", linewidth=2.0)
ax.errorbar([Depth_Joelho_Meters, Depth_Quadril_Meters, Depth_Umbigo_Meters, Depth_Xifoide_Meters], [Custo_Joelho_SpeedEight_Mean, Custo_Quadril_SpeedEight_Mean, Custo_Umbigo_SpeedEight_Mean, Custo_Xifoide_SpeedEight_Mean],yerr=Custo_Eight_CI, fmt='--', color='dodgerblue', label="0.8", linewidth=2.0)

ax.set_ylim([0, 12])
fig.suptitle('Cost of Transport', fontsize=20)
plt.xlabel('Depth (m)', fontsize=18)
plt.ylabel('Cost of Transport (J/kg/m)', fontsize=16)
ax.tick_params(labelsize=14)
line_labels = ['0.2 m/s','0.4 m/s','0.6 m/s', '0.8 m/s']
plt.legend(labels = line_labels, loc = 'best', title = 'Speed', fontsize=14)
'''




#FIGURE 03
#COST AND DEPTH IN PERCENTUAL OF STATURE SCALE

#fig, ax = plt.subplots()
#fig.canvas.set_window_title('Cost of Transport per Depth in Percentual of Stature Scale')
#ax.errorbar([Depth_Joelho_Percentual, Depth_Quadril_Percentual, Depth_Umbigo_Percentual, Depth_Xifoide_Percentual], [Custo_Joelho_SpeedTwo_Mean, Custo_Quadril_SpeedTwo_Mean, Custo_Umbigo_SpeedTwo_Mean, Custo_Xifoide_SpeedTwo_Mean], yerr=CI_Two, fmt='--', color='goldenrod', label="0.2", linewidth=2.0, )
#ax.errorbar([Depth_Joelho_Percentual, Depth_Quadril_Percentual, Depth_Umbigo_Percentual, Depth_Xifoide_Percentual], [Custo_Joelho_SpeedFour_Mean, Custo_Quadril_SpeedFour_Mean, Custo_Umbigo_SpeedFour_Mean, Custo_Xifoide_SpeedFour_Mean], yerr=CI_Four, fmt='-.', color='limegreen', label="0.4", linewidth=2.0)
#ax.errorbar([Depth_Joelho_Percentual, Depth_Quadril_Percentual, Depth_Umbigo_Percentual, Depth_Xifoide_Percentual], [Custo_Joelho_SpeedSix_Mean, Custo_Quadril_SpeedSix_Mean, Custo_Umbigo_SpeedSix_Mean, Custo_Xifoide_SpeedSix_Mean],yerr=CI_Six, fmt='--', color='mediumorchid', label="0.6", linewidth=2.0)
#ax.errorbar([Depth_Joelho_Percentual, Depth_Quadril_Percentual, Depth_Umbigo_Percentual, Depth_Xifoide_Percentual], [Custo_Joelho_SpeedEight_Mean, Custo_Quadril_SpeedEight_Mean, Custo_Umbigo_SpeedEight_Mean, Custo_Xifoide_SpeedEight_Mean],yerr=CI_Eight, fmt='--', color='dodgerblue', label="0.8", linewidth=2.0)
#ax.set_ylim([0, 12])
#fig.suptitle('Cost of Transport', fontsize=20)
#plt.xlabel('Depth (% of Stature)', fontsize=18)
#plt.ylabel('Cost of Transport (J/kg/m)', fontsize=16)
#ax.tick_params(labelsize=14)
#plt.legend(labels = line_labels, loc = 'best', title = 'Speed', fontsize=14)




'''
#FIGURE 04
#COST PER SPEED, WITH LINES OF DEPTHS

VAS_Joelho = VAS_Joelho*4/0.8
VAS_Quadril = VAS_Quadril*4/0.8
VAS_Umbigo = VAS_Umbigo*4/0.8
VAS_Xifoide = VAS_Xifoide*4/0.8

fig, ax = plt.subplots()
fig.canvas.set_window_title('Cost of Transport per Walking Speed')
ax.errorbar([1, 2, 3, 4], Custo_Joelho_All_Speed_Mean_list, yerr=Custo_Joelho_All_Speed_CI_list, fmt='--', color='goldenrod', linewidth=2.5)
ax.errorbar([1, 2, 3, 4], Custo_Quadril_All_Speed_Mean_list, yerr= Custo_Quadril_All_Speed_CI_list, fmt='-.', color='limegreen', linewidth=2.5)
ax.errorbar([1, 2, 3, 4], Custo_Umbigo_All_Speed_Mean_list, yerr= Custo_Umbigo_All_Speed_CI_list, fmt='--', color='mediumorchid', linewidth=2.5)
ax.errorbar([1, 2, 3, 4], Custo_Xifoide_All_Speed_Mean_list, yerr= Custo_Xifoide_All_Speed_CI_list, fmt='--', color='dodgerblue', linewidth=2.5)
ax.errorbar([1, 2, 3, 4], [Custo_Ardigo_Two, Custo_Ardigo_Four, Custo_Ardigo_Six, Custo_Ardigo_Eight], fmt='--', color='black', linewidth=2.5)

xticks = [1, 2, 3, 4]
xlabels = ["0.2", "0.4", "0.6","0.8"]
plt.xticks(xticks, xlabels)
ax.set_ylim([0, 12])
fig.suptitle('Cost of Transport', fontsize=20)
plt.xlabel('Speed (m/s)', fontsize=22)
plt.ylabel('Cost of Transport (J/kg/m)', fontsize=22)
ax.tick_params(labelsize=20)
line_labels = ['Knee','Hip','Umbilical', 'Xiphoid', 'Land (Ardigò 2003)','VAS']
plt.legend(labels = line_labels, loc = 'best', title = 'Depth', fontsize=18)
ax.axvline(VAS_Joelho, linestyle=':', color='goldenrod', linewidth=2.0)
ax.axvline(VAS_Quadril, linestyle=':', color='limegreen', linewidth=2.0)
ax.axvline(VAS_Umbigo, linestyle=':', color='mediumorchid', linewidth=2.0)
ax.axvline(VAS_Xifoide, linestyle=':', color='dodgerblue', linewidth=2.0)
'''




#FIGURE 05
#COST AND DRAG FORCE AND GRFV_MEAN (Lines: Speeds)


#fig, ax = plt.subplots(2, sharex=True, sharey=True)
#fig.canvas.set_window_title('Cost of Transport and Drag Force and GRFV_Mean')
#fig.suptitle('Cost of Transport and Drag Force and GRFV_Mean', fontsize = 14)
#ax[0].set_title('0.2 and 0.4 m/s')
#ax[0].plot([Drag_F_Joelho_SpeedTwo_Mean, Drag_F_Quadril_SpeedTwo_Mean, Drag_F_Umbigo_SpeedTwo_Mean, Drag_F_Xifoide_SpeedTwo_Mean], [Custo_Joelho_SpeedTwo_Mean, Custo_Quadril_SpeedTwo_Mean, Custo_Umbigo_SpeedTwo_Mean, Custo_Xifoide_SpeedTwo_Mean], '-', color='goldenrod', linewidth=2.0, label ='Drag Force 0.2')
#ax[0].plot([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean], [Custo_Joelho_SpeedTwo_Mean, Custo_Quadril_SpeedTwo_Mean, Custo_Umbigo_SpeedTwo_Mean, Custo_Xifoide_SpeedTwo_Mean], '--', color='limegreen', linewidth=2.0, label ='GRFV Mean 0.2')
#ax[0].plot([Drag_F_Joelho_SpeedFour_Mean, Drag_F_Quadril_SpeedFour_Mean, Drag_F_Umbigo_SpeedFour_Mean, Drag_F_Xifoide_SpeedFour_Mean], [Custo_Joelho_SpeedFour_Mean, Custo_Quadril_SpeedFour_Mean, Custo_Umbigo_SpeedFour_Mean, Custo_Xifoide_SpeedFour_Mean], '-', color='mediumorchid', linewidth=2.0, label ='Drag Force 0.4')
#ax[0].plot([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean], [Custo_Joelho_SpeedFour_Mean, Custo_Quadril_SpeedFour_Mean, Custo_Umbigo_SpeedFour_Mean, Custo_Xifoide_SpeedFour_Mean], '--', color='dodgerblue', linewidth=2.0, label ='GRFV Mean 0.4')
#s = 70
#ax[0].scatter(Drag_F_Joelho_SpeedTwo_Mean,Custo_Joelho_SpeedTwo_Mean,  color='black', s=s, marker='o', label = 'Knee')
#ax[0].scatter(GRF_V_MEAN_Joelho_Mean,Custo_Joelho_SpeedTwo_Mean,  color='black', s=s, marker='o')
#ax[0].scatter(Drag_F_Xifoide_SpeedTwo_Mean,Custo_Xifoide_SpeedTwo_Mean,  color='black', s=s, marker='s', label = 'Xiphoid')
#ax[0].scatter(GRF_V_MEAN_Xifoide_Mean,Custo_Xifoide_SpeedTwo_Mean,  color='black', s=s, marker='s')
#ax[0].scatter(Drag_F_Joelho_SpeedFour_Mean,Custo_Joelho_SpeedFour_Mean,  color='black', s=s, marker='o')
#ax[0].scatter(GRF_V_MEAN_Joelho_Mean,Custo_Joelho_SpeedFour_Mean,  color='black', s=s, marker='o')
#ax[0].scatter(Drag_F_Xifoide_SpeedFour_Mean,Custo_Xifoide_SpeedFour_Mean,  color='black', s=s, marker='s')
#ax[0].scatter(GRF_V_MEAN_Xifoide_Mean,Custo_Xifoide_SpeedFour_Mean,  color='black', s=s, marker='s')

#ax[0].legend(fontsize=10, frameon=False, loc='upper right')

#ax[1].set_title('0.6 and 0.8 m/s')
#ax[1].plot([Drag_F_Joelho_SpeedSix_Mean, Drag_F_Quadril_SpeedSix_Mean, Drag_F_Umbigo_SpeedSix_Mean, Drag_F_Xifoide_SpeedSix_Mean], [Custo_Joelho_SpeedSix_Mean, Custo_Quadril_SpeedSix_Mean, Custo_Umbigo_SpeedSix_Mean, Custo_Xifoide_SpeedSix_Mean], '-', color='goldenrod', linewidth=2.0, label ='Drag Force 0.6')
#ax[1].plot([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean], [Custo_Joelho_SpeedSix_Mean, Custo_Quadril_SpeedSix_Mean, Custo_Umbigo_SpeedSix_Mean, Custo_Xifoide_SpeedSix_Mean], '--', color='limegreen', linewidth=2.0, label ='GRFV Mean 0.6')
#ax[1].plot([Drag_F_Joelho_SpeedEight_Mean, Drag_F_Quadril_SpeedEight_Mean, Drag_F_Umbigo_SpeedEight_Mean, Drag_F_Xifoide_SpeedEight_Mean], [Custo_Joelho_SpeedEight_Mean, Custo_Quadril_SpeedEight_Mean, Custo_Umbigo_SpeedEight_Mean, Custo_Xifoide_SpeedEight_Mean], '-', color='mediumorchid', linewidth=2.0, label ='Drag Force 0.8')
#ax[1].plot([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean], [Custo_Joelho_SpeedEight_Mean, Custo_Quadril_SpeedEight_Mean, Custo_Umbigo_SpeedEight_Mean, Custo_Xifoide_SpeedEight_Mean], '--', color='dodgerblue', linewidth=2.0, label ='GRFV Mean 0.8')

#ax[1].scatter(Drag_F_Joelho_SpeedSix_Mean,Custo_Joelho_SpeedSix_Mean,  color='black', s=s, marker='o', label = 'Knee')
#ax[1].scatter(GRF_V_MEAN_Joelho_Mean,Custo_Joelho_SpeedSix_Mean,  color='black', s=s, marker='o')
#ax[1].scatter(Drag_F_Xifoide_SpeedSix_Mean,Custo_Xifoide_SpeedSix_Mean,  color='black', s=s, marker='s', label = 'Xiphoid')
#ax[1].scatter(GRF_V_MEAN_Xifoide_Mean,Custo_Xifoide_SpeedSix_Mean,  color='black', s=s, marker='s')
#ax[1].scatter(Drag_F_Joelho_SpeedEight_Mean,Custo_Joelho_SpeedEight_Mean,  color='black', s=s, marker='o')
#ax[1].scatter(GRF_V_MEAN_Joelho_Mean,Custo_Joelho_SpeedEight_Mean,  color='black', s=s, marker='o')
#ax[1].scatter(Drag_F_Xifoide_SpeedEight_Mean,Custo_Xifoide_SpeedEight_Mean,  color='black', s=s, marker='s')
#ax[1].scatter(GRF_V_MEAN_Xifoide_Mean,Custo_Xifoide_SpeedEight_Mean,  color='black', s=s, marker='s')

#ax[1].legend(fontsize=10, frameon=False, loc='upper right')
#ax[1].set_ylim([0, 12])
#ax[1].set_xlabel('Force (N)', fontsize=18)
#ax[0].tick_params(labelsize=14)
#fig.text(0.05, 0.5, 'Cost of Transport (J/kg/m)', va='center', rotation='vertical', fontsize=18)




#FIGURE 06
#COST AND DRAG FORCE PER METER (Lines: Depths)


#fig, ax = plt.subplots()
#fig.canvas.set_window_title('Cost of Transport and Drag Force per Meter')

#ax.plot([Drag_F_per_Meter_Joelho_SpeedTwo_Mean, Drag_F_per_Meter_Joelho_SpeedFour_Mean, Drag_F_per_Meter_Joelho_SpeedSix_Mean, Drag_F_per_Meter_Joelho_SpeedEight_Mean], [Custo_Joelho_SpeedTwo_Mean, Custo_Joelho_SpeedFour_Mean, Custo_Joelho_SpeedSix_Mean, Custo_Joelho_SpeedEight_Mean], '--', color='goldenrod', linewidth=2.0, label ='Knee')
#ax.plot([Drag_F_per_Meter_Quadril_SpeedTwo_Mean, Drag_F_per_Meter_Quadril_SpeedFour_Mean, Drag_F_per_Meter_Quadril_SpeedSix_Mean, Drag_F_per_Meter_Quadril_SpeedEight_Mean], [Custo_Quadril_SpeedTwo_Mean, Custo_Quadril_SpeedFour_Mean, Custo_Quadril_SpeedSix_Mean, Custo_Quadril_SpeedEight_Mean], '-.', color='limegreen', linewidth=2.0, label ='Hip')
#ax.plot([Drag_F_per_Meter_Umbigo_SpeedTwo_Mean, Drag_F_per_Meter_Umbigo_SpeedFour_Mean, Drag_F_per_Meter_Umbigo_SpeedSix_Mean, Drag_F_per_Meter_Umbigo_SpeedEight_Mean], [Custo_Umbigo_SpeedTwo_Mean, Custo_Umbigo_SpeedFour_Mean, Custo_Umbigo_SpeedSix_Mean, Custo_Umbigo_SpeedEight_Mean], '--', color='mediumorchid', linewidth=2.0, label ='Umbilical')
#ax.plot([Drag_F_per_Meter_Xifoide_SpeedTwo_Mean, Drag_F_per_Meter_Xifoide_SpeedFour_Mean, Drag_F_per_Meter_Xifoide_SpeedSix_Mean, Drag_F_per_Meter_Xifoide_SpeedEight_Mean], [Custo_Xifoide_SpeedTwo_Mean, Custo_Xifoide_SpeedFour_Mean, Custo_Xifoide_SpeedSix_Mean, Custo_Xifoide_SpeedEight_Mean], '--', color='dodgerblue', linewidth=2.0, label ='Xiphoid')

#ax.set_ylim([0, 12])
#ax.set_title('Cost of Transport and Drag Force per Meter', fontsize=20)
#ax.set_xlabel('Drag Force per Meter (N/m)', fontsize=18)
#ax.set_ylabel('Cost of Transport (J/kg/m)', fontsize=16)
#ax.tick_params(labelsize=14)
#ax.legend(loc = 'best', title = 'Depth', fontsize=12)





#FIGURE 07
#COST AND GRF-V PEAK (Lines: Depths)

#fig, ax = plt.subplots()
#fig.canvas.set_window_title('Cost of Transport and peak of TOTAL_SUM_FORCES')

#ax.plot([TOTAL_SUM_FORCES_Joelho_SpeedTwo_Mean, TOTAL_SUM_FORCES_Joelho_SpeedFour_Mean, TOTAL_SUM_FORCES_Joelho_SpeedSix_Mean, TOTAL_SUM_FORCES_Joelho_SpeedEight_Mean], [Custo_Joelho_SpeedTwo_Mean, Custo_Joelho_SpeedFour_Mean, Custo_Joelho_SpeedSix_Mean, Custo_Joelho_SpeedEight_Mean], '--', color='goldenrod', linewidth=2.0, label ='Knee')
#ax.plot([TOTAL_SUM_FORCES_Quadril_SpeedTwo_Mean, TOTAL_SUM_FORCES_Quadril_SpeedFour_Mean, TOTAL_SUM_FORCES_Quadril_SpeedSix_Mean, TOTAL_SUM_FORCES_Quadril_SpeedEight_Mean], [Custo_Quadril_SpeedTwo_Mean, Custo_Quadril_SpeedFour_Mean, Custo_Quadril_SpeedSix_Mean, Custo_Quadril_SpeedEight_Mean], '-.', color='limegreen', linewidth=2.0, label ='Hip')
#ax.plot([TOTAL_SUM_FORCES_Umbigo_SpeedTwo_Mean, TOTAL_SUM_FORCES_Umbigo_SpeedFour_Mean, TOTAL_SUM_FORCES_Umbigo_SpeedSix_Mean, TOTAL_SUM_FORCES_Umbigo_SpeedEight_Mean], [Custo_Umbigo_SpeedTwo_Mean, Custo_Umbigo_SpeedFour_Mean, Custo_Umbigo_SpeedSix_Mean, Custo_Umbigo_SpeedEight_Mean], '--', color='mediumorchid', linewidth=2.0, label ='Umbilical')
#ax.plot([TOTAL_SUM_FORCES_Xifoide_SpeedTwo_Mean, TOTAL_SUM_FORCES_Xifoide_SpeedFour_Mean, TOTAL_SUM_FORCES_Xifoide_SpeedSix_Mean, TOTAL_SUM_FORCES_Xifoide_SpeedEight_Mean], [Custo_Xifoide_SpeedTwo_Mean, Custo_Xifoide_SpeedFour_Mean, Custo_Xifoide_SpeedSix_Mean, Custo_Xifoide_SpeedEight_Mean], '--', color='dodgerblue', linewidth=2.0, label ='Xiphoid')

#ax.set_ylim([0, 12])
#ax.set_title('Cost of Transport and TOTAL_SUM_FORCES', fontsize=20)
#ax.set_xlabel('TOTAL_SUM_FORCES (N)', fontsize=18)
#ax.set_ylabel('Cost of Transport (J/kg/m)', fontsize=16)
#ax.tick_params(labelsize=14)
#ax.legend(loc = 'best', title = 'Depth', fontsize=14)





#FIGURE 08
# COST AND DRAG AND GRFV_MEAN WITH TWO VERTICAL AXIS 0.2 m/s

#Create "truncate" function to round the values of Axis Ticks
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

# Editing the Font Size of Axis Labels and Ticks (numeric values)
plt.rcParams['axes.labelsize']=22
plt.rcParams['ytick.labelsize']=20
plt.rcParams['xtick.labelsize']=20

#Markersize (ms)
ms = 20
#Linewidth (lw)
lw = 4

# Creating figure with 02 Parasite Y Axis
fig = plt.figure()
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
fig.canvas.set_window_title('Cost of Transport and Drag Force and GRFV_Mean 0.2 m/s')
fig.suptitle('0.2 m/s', fontsize = 20)

par1 = host.twinx()
par2 = host.twinx()

# Setting Parasite Y Axis Position
offset = 0
new_fixed_axis = par1.get_grid_helper().new_fixed_axis
par1.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par1,
                                    offset=(offset, 0))
par1.axis["right"].toggle(all=True)

offset = 80
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par2,
                                    offset=(offset, 0))
par2.axis["right"].toggle(all=True)


# Setting Axis Labels and Min/Max Values
host.set_xlim([0.3, 1.5])

# The Axis Values limits are defined in the following manner:
    # COST AXIS: Minimum is Zero. Maximum is the Maximum Value obtained in the respective plot plus 50% of the Maximum Value obtained in the respective plot.
    # DRAG and GRFV_MEAN: Minimum is the Minimum Value obtained in the respective plot minus 50% of the Minimum Value obtained in the respective plot. Maximum obey the same criteria from Cost Maximum.

Cost_Two_ymax = max(([Custo_Joelho_SpeedTwo_Mean, Custo_Quadril_SpeedTwo_Mean, Custo_Umbigo_SpeedTwo_Mean, Custo_Xifoide_SpeedTwo_Mean]) + 0.5*max([Custo_Joelho_SpeedTwo_Mean, Custo_Quadril_SpeedTwo_Mean, Custo_Umbigo_SpeedTwo_Mean, Custo_Xifoide_SpeedTwo_Mean]))
Drag_F_Two_ymin = min(([Drag_F_Joelho_SpeedTwo_Mean, Drag_F_Quadril_SpeedTwo_Mean, Drag_F_Umbigo_SpeedTwo_Mean, Drag_F_Xifoide_SpeedTwo_Mean]) - 0.5*min([Drag_F_Joelho_SpeedTwo_Mean, Drag_F_Quadril_SpeedTwo_Mean, Drag_F_Umbigo_SpeedTwo_Mean, Drag_F_Xifoide_SpeedTwo_Mean]))
Drag_F_Two_ymax = max(([Drag_F_Joelho_SpeedTwo_Mean, Drag_F_Quadril_SpeedTwo_Mean, Drag_F_Umbigo_SpeedTwo_Mean, Drag_F_Xifoide_SpeedTwo_Mean]) + 0.5*max([Drag_F_Joelho_SpeedTwo_Mean, Drag_F_Quadril_SpeedTwo_Mean, Drag_F_Umbigo_SpeedTwo_Mean, Drag_F_Xifoide_SpeedTwo_Mean]))
GRFV_MEAN_ymin = min(([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]) - 0.5*min([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]))
GRFV_MEAN_ymax = max(([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]) + 0.5*max([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]))

host.set_ylim(0,Cost_Two_ymax)
par1.set_ylim(Drag_F_Two_ymin, Drag_F_Two_ymax)
par2.set_ylim(GRFV_MEAN_ymin, GRFV_MEAN_ymax)

host.yaxis.set_ticks(np.arange(1,Cost_Two_ymax, 1))
par2.yaxis.set_ticks(np.arange(truncate(GRFV_MEAN_ymin,-2),GRFV_MEAN_ymax,200))


#Polynomial Fit Lines Calculation

# Polynomial 1º Degree Custo 0.2 m/s
Z_1_Custo_SpeedTwo,error_1_Custo_SpeedTwo,_,_,_ = np.polyfit(Depth_Meters_ALL, Custo_Two_Mean, 1, full=True)
f_1_Custo_SpeedTwo = np.poly1d(Z_1_Custo_SpeedTwo)
# calculate new x's and y's
X_1_Custo_SpeedTwo_new = np.linspace(Depth_Meters_ALL[0], Depth_Meters_ALL[-1], 50)
Y_1_Custo_SpeedTwo_new = f_1_Custo_SpeedTwo(X_1_Custo_SpeedTwo_new)

# Polynomial 2º Degree Custo 0.2 m/s
X_Custo_SpeedTwo = Depth_Meters_ALL
Y_Custo_SpeedTwo = Custo_Two_Mean

Z_Custo_SpeedTwo,error_2_Custo_SpeedTwo,_,_,_ = np.polyfit(X_Custo_SpeedTwo, Y_Custo_SpeedTwo, 2, full=True)
f_Custo_SpeedTwo  = np.poly1d(Z_Custo_SpeedTwo)
# calculate new x's and y's
X_Custo_SpeedTwo_new = np.linspace(min(X_Custo_SpeedTwo ), max(X_Custo_SpeedTwo), 50)
Y_Custo_SpeedTwo_new = f_Custo_SpeedTwo(X_Custo_SpeedTwo_new)
'''
print('Custo_0.2_1º_Degree_Error')
print(error_1_Custo_SpeedTwo)
print('Custo_0.2_2º_Degree_Error')
print(error_2_Custo_SpeedTwo)
'''
# Polynomial 1º Degree Drag_F 0.2 m/s
Z_1_Drag_F_SpeedTwo,error_1_Drag_F_SpeedTwo,_,_,_ = np.polyfit(Depth_Meters_ALL, Drag_F_Two_Mean, 1, full=True)
f_1_Drag_F_SpeedTwo = np.poly1d(Z_1_Drag_F_SpeedTwo)
# calculate new x's and y's
X_1_Drag_F_SpeedTwo_new = np.linspace(Depth_Meters_ALL[0], Depth_Meters_ALL[-1], 50)
Y_1_Drag_F_SpeedTwo_new = f_1_Drag_F_SpeedTwo(X_1_Drag_F_SpeedTwo_new)


# Polynomial 2º Degree Drag_F 0.2 m/s
X_Drag_F_SpeedTwo = Depth_Meters_ALL
Y_Drag_F_SpeedTwo = Drag_F_Two_Mean

Z_Drag_F_SpeedTwo,error_2_Drag_F_SpeedTwo,_,_,_ = np.polyfit(X_Drag_F_SpeedTwo, Y_Drag_F_SpeedTwo, 2, full=True)
f_Drag_F_SpeedTwo  = np.poly1d(Z_Drag_F_SpeedTwo)
# calculate new x's and y's
X_Drag_F_SpeedTwo_new = np.linspace(min(X_Drag_F_SpeedTwo ), max(X_Drag_F_SpeedTwo), 50)
Y_Drag_F_SpeedTwo_new = f_Drag_F_SpeedTwo(X_Drag_F_SpeedTwo_new)
'''
print('Drag_F_0.2_1º_Degree_Error')
print(error_1_Drag_F_SpeedTwo)
print('Drag_F_0.2_2º_Degree_Error')
print(error_2_Drag_F_SpeedTwo)
'''

# Polynomial 1º Degree GRF_V_Mean (There is only one for all speeds)
Z_1_GRF_V_MEAN,error_1_GRF_V_MEAN,_,_,_ = np.polyfit(Depth_Meters_ALL, GRF_V_MEAN_Mean, 1, full=True)
f_1_GRF_V_MEAN = np.poly1d(Z_1_GRF_V_MEAN)
# calculate new x's and y's
X_1_GRF_V_MEAN_new = np.linspace(Depth_Meters_ALL[0], Depth_Meters_ALL[-1], 50)
Y_1_GRF_V_MEAN_new = f_1_GRF_V_MEAN(X_1_GRF_V_MEAN_new)

# Polynomial 2º Degree GRF_V_Mean (There is only one for all speeds)
X_GRF_V_MEAN = Depth_Meters_ALL
Y_GRF_V_MEAN = GRF_V_MEAN_Mean

Z_GRF_V_MEAN,error_2_GRF_V_MEAN,_,_,_ = np.polyfit(X_GRF_V_MEAN, Y_GRF_V_MEAN, 2, full=True)
f_GRF_V_MEAN  = np.poly1d(Z_GRF_V_MEAN)
# calculate new x's and y's
X_GRF_V_MEAN_new = np.linspace(min(X_GRF_V_MEAN ), max(X_GRF_V_MEAN), 50)
Y_GRF_V_MEAN_new = f_GRF_V_MEAN(X_GRF_V_MEAN_new)
'''
print('GRF_V_MEAN_1º_Degree_Error')
print(error_1_GRF_V_MEAN)
print('GRF_V_MEAN_2º_Degree_Error')
print(error_2_GRF_V_MEAN)
'''

# Getting the Data to be Plotted

#Error bar
for i in np.arange(0, len(Custo_Two_Mean)):
    p1, = host.plot((Depth_Meters_ALL[i], Depth_Meters_ALL[i]), (Custo_Two_Mean[i]+Custo_Two_CI[i], Custo_Two_Mean[i]-Custo_Two_CI[i]) ,linestyle = '-' ,color='darkgoldenrod', linewidth=lw)
    p2, = par1.plot([Depth_Meters_ALL[i], Depth_Meters_ALL[i]], [Drag_F_Two_Mean[i]+Drag_F_Two_CI[i], Drag_F_Two_Mean[i]-Drag_F_Two_CI[i]], linestyle ='-', color = 'firebrick',  linewidth=lw)
    p3, = par2.plot([Depth_Meters_ALL[i], Depth_Meters_ALL[i]], [GRF_V_MEAN_Mean[i]+GRF_V_MEAN_CI[i], GRF_V_MEAN_Mean[i]-GRF_V_MEAN_CI[i]], linestyle = '-', color = 'mediumblue',  linewidth=lw)

#Lines (Polynomials)
p1, = host.plot(X_Custo_SpeedTwo_new, Y_Custo_SpeedTwo_new, linestyle = '-' ,color='darkgoldenrod', linewidth=lw, label = 'Cost of Transport')
p2, = par1.plot(X_Drag_F_SpeedTwo_new , Y_Drag_F_SpeedTwo_new , linestyle ='--', color = 'firebrick',  linewidth=lw, label = 'Drag Force')
p3, = par2.plot(X_GRF_V_MEAN_new, Y_GRF_V_MEAN_new, linestyle = ':', color = 'mediumblue',  linewidth=lw, label='Apparent Weight')

host.legend(fontsize=16, frameon=False, loc='upper left')
tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', **tkw)
par1.tick_params(axis='y', **tkw)
par2.tick_params(axis='y', **tkw)
host.tick_params(axis='x', **tkw)

host.set_xlabel("Depth (m)")
host.set_ylabel("Cost of Transport (J/kg/m)")
par1.set_ylabel("Drag Force (N)")
par2.set_ylabel("Apparent Weight (N)")




#FIGURE 09
# COST AND DRAG AND GRFV_MEAN WITH TWO VERTICAL AXIS 0.4 m/s

# Creating figure with 02 Parasite Y Axis
fig = plt.figure()
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
fig.canvas.set_window_title('Cost of Transport and Drag Force and GRFV_Mean 0.4 m/s')
fig.suptitle('0.4 m/s', fontsize = 20)

par1 = host.twinx()
par2 = host.twinx()

# Setting Parasite Y Axis Position
offset = 0
new_fixed_axis = par1.get_grid_helper().new_fixed_axis
par1.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par1,
                                    offset=(offset, 0))
par1.axis["right"].toggle(all=True)

offset = 80
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par2,
                                    offset=(offset, 0))
par2.axis["right"].toggle(all=True)


# Setting Axis Labels and Min/Max Values
host.set_xlim([0.3, 1.5])
# The Axis Values limits are defined in the following manner:
    # COST AXIS: Minimum is Zero. Maximum is the Maximum Value obtained in the respective plot plus 50% of the Maximum Value obtained in the respective plot.
    # DRAG and GRFV_MEAN: Minimum is the Minimum Value obtained in the respective plot minus 50% of the Minimum Value obtained in the respective plot. Maximum obey the same criteria from Cost Maximum.

Cost_Four_ymax = max(([Custo_Joelho_SpeedFour_Mean, Custo_Quadril_SpeedFour_Mean, Custo_Umbigo_SpeedFour_Mean, Custo_Xifoide_SpeedFour_Mean]) + 0.5*max([Custo_Joelho_SpeedFour_Mean, Custo_Quadril_SpeedFour_Mean, Custo_Umbigo_SpeedFour_Mean, Custo_Xifoide_SpeedFour_Mean]))
Drag_F_Four_ymin = min(([Drag_F_Joelho_SpeedFour_Mean, Drag_F_Quadril_SpeedFour_Mean, Drag_F_Umbigo_SpeedFour_Mean, Drag_F_Xifoide_SpeedFour_Mean]) - 0.5*min([Drag_F_Joelho_SpeedFour_Mean, Drag_F_Quadril_SpeedFour_Mean, Drag_F_Umbigo_SpeedFour_Mean, Drag_F_Xifoide_SpeedFour_Mean]))
Drag_F_Four_ymax = max(([Drag_F_Joelho_SpeedFour_Mean, Drag_F_Quadril_SpeedFour_Mean, Drag_F_Umbigo_SpeedFour_Mean, Drag_F_Xifoide_SpeedFour_Mean]) + 0.5*max([Drag_F_Joelho_SpeedFour_Mean, Drag_F_Quadril_SpeedFour_Mean, Drag_F_Umbigo_SpeedFour_Mean, Drag_F_Xifoide_SpeedFour_Mean]))
GRFV_MEAN_ymin = min(([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]) - 0.5*min([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]))
GRFV_MEAN_ymax = max(([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]) + 0.5*max([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]))

host.set_ylim(0,Cost_Four_ymax)
par1.set_ylim(Drag_F_Four_ymin, Drag_F_Four_ymax)
par2.set_ylim(GRFV_MEAN_ymin, GRFV_MEAN_ymax)

host.yaxis.set_ticks(np.arange(2,Cost_Four_ymax, 2))
par2.yaxis.set_ticks(np.arange(truncate(GRFV_MEAN_ymin,-2),GRFV_MEAN_ymax,200))


#Polynomial Fit Lines Calculation

# Polynomial 1º Degree Custo 0.4 m/s
Z_1_Custo_SpeedFour,error_1_Custo_SpeedFour,_,_,_ = np.polyfit(Depth_Meters_ALL, Custo_Four_Mean, 1, full=True)
f_1_Custo_SpeedFour = np.poly1d(Z_1_Custo_SpeedFour)
# calculate new x's and y's
X_1_Custo_SpeedFour_new = np.linspace(Depth_Meters_ALL[0], Depth_Meters_ALL[-1], 50)
Y_1_Custo_SpeedFour_new = f_1_Custo_SpeedFour(X_1_Custo_SpeedFour_new)

# Polynomial 2º Degree Custo 0.4 m/s
X_Custo_SpeedFour = Depth_Meters_ALL
Y_Custo_SpeedFour = Custo_Four_Mean

Z_Custo_SpeedFour,error_2_Custo_SpeedFour,_,_,_ = np.polyfit(X_Custo_SpeedFour, Y_Custo_SpeedFour, 2, full=True)
f_Custo_SpeedFour  = np.poly1d(Z_Custo_SpeedFour)
# calculate new x's and y's
X_Custo_SpeedFour_new = np.linspace(min(X_Custo_SpeedFour), max(X_Custo_SpeedFour), 50)
Y_Custo_SpeedFour_new = f_Custo_SpeedFour(X_Custo_SpeedFour_new)
'''
print('Custo_0.4_1º_Degree_Error')
print(error_1_Custo_SpeedFour)
print('Custo_0.4_2º_Degree_Error')
print(error_2_Custo_SpeedFour)
'''

# Polynomial 1º Degree Drag_F 0.4 m/s
Z_1_Drag_F_SpeedFour,error_1_Drag_F_SpeedFour,_,_,_ = np.polyfit(Depth_Meters_ALL, Drag_F_Four_Mean, 1, full=True)
f_1_Drag_F_SpeedFour = np.poly1d(Z_1_Drag_F_SpeedFour)
# calculate new x's and y's
X_1_Drag_F_SpeedFour_new = np.linspace(Depth_Meters_ALL[0], Depth_Meters_ALL[-1], 50)
Y_1_Drag_F_SpeedFour_new = f_1_Drag_F_SpeedFour(X_1_Drag_F_SpeedFour_new)

# Polynomial 2º Degree Drag_F 0.4 m/s
X_Drag_F_SpeedFour = Depth_Meters_ALL
Y_Drag_F_SpeedFour = Drag_F_Four_Mean

Z_Drag_F_SpeedFour,error_2_Drag_F_SpeedFour,_,_,_ = np.polyfit(X_Drag_F_SpeedFour, Y_Drag_F_SpeedFour, 2, full=True)
f_Drag_F_SpeedFour  = np.poly1d(Z_Drag_F_SpeedFour)
# calculate new x's and y's
X_Drag_F_SpeedFour_new = np.linspace(min(X_Drag_F_SpeedFour), max(X_Drag_F_SpeedFour), 50)
Y_Drag_F_SpeedFour_new = f_Drag_F_SpeedFour(X_Drag_F_SpeedFour_new)
'''
print('Drag_F_0.4_1º_Degree_Error')
print(error_1_Drag_F_SpeedFour)
print('Drag_F_0.4_2º_Degree_Error')
print(error_2_Drag_F_SpeedFour)
'''



# Getting the Data to be Plotted
#Error bar
for i in np.arange(0, len(Custo_Four_Mean)):
    p1, = host.plot((Depth_Meters_ALL[i], Depth_Meters_ALL[i]), (Custo_Four_Mean[i]+Custo_Four_CI[i], Custo_Four_Mean[i]-Custo_Four_CI[i]) ,linestyle = '-' ,color='darkgoldenrod', linewidth=lw)
    p2, = par1.plot([Depth_Meters_ALL[i], Depth_Meters_ALL[i]], [Drag_F_Four_Mean[i]+Drag_F_Four_CI[i], Drag_F_Four_Mean[i]-Drag_F_Four_CI[i]], linestyle ='--', color = 'firebrick',  linewidth=lw)
    p3, = par2.plot([Depth_Meters_ALL[i], Depth_Meters_ALL[i]], [GRF_V_MEAN_Mean[i]+GRF_V_MEAN_CI[i], GRF_V_MEAN_Mean[i]-GRF_V_MEAN_CI[i]], linestyle = ':', color = 'mediumblue',  linewidth=lw)
#Lines (Polynomials)
p1, = host.plot(X_Custo_SpeedFour_new, Y_Custo_SpeedFour_new, linestyle = '-' ,color='darkgoldenrod', linewidth=lw, label = 'Cost of Transport')
p2, = par1.plot(X_Drag_F_SpeedFour_new , Y_Drag_F_SpeedFour_new , linestyle ='--', color = 'firebrick',  linewidth=lw, label = 'Drag Force')
p3, = par2.plot(X_GRF_V_MEAN_new, Y_GRF_V_MEAN_new, linestyle = ':', color = 'mediumblue',  linewidth=lw, label='Apparent Weight')

host.legend(fontsize=16, frameon=False, loc='upper left')


tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', **tkw)
par1.tick_params(axis='y', **tkw)
par2.tick_params(axis='y', **tkw)
host.tick_params(axis='x', **tkw)

host.set_xlabel("Depth (m)")
host.set_ylabel("Cost of Transport (J/kg/m)")
par1.set_ylabel("Drag Force (N)")
par2.set_ylabel("Apparent Weight (N)")







#FIGURE 10
# COST AND DRAG AND GRFV_MEAN WITH TWO VERTICAL AXIS 0.6 m/s

# Creating figure with 02 Parasite Y Axis
fig = plt.figure()
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
fig.canvas.set_window_title('Cost of Transport and Drag Force and GRFV_Mean 0.6 m/s')
fig.suptitle('0.6 m/s', fontsize = 20)

par1 = host.twinx()
par2 = host.twinx()

# Setting Parasite Y Axis Position
offset = 0
new_fixed_axis = par1.get_grid_helper().new_fixed_axis
par1.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par1,
                                    offset=(offset, 0))
par1.axis["right"].toggle(all=True)

offset = 80
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par2,
                                    offset=(offset, 0))
par2.axis["right"].toggle(all=True)


# Setting Axis Labels and Min/Max Values
host.set_xlim([0.3, 1.5])
#host.set_xticks(np.arange(0.3, 1.1, 0.1))
# The Axis Values limits are defined in the following manner:
    # COST AXIS: Minimum is Zero. Maximum is the Maximum Value obtained in the respective plot plus 50% of the Maximum Value obtained in the respective plot.
    # DRAG and GRFV_MEAN: Minimum is the Minimum Value obtained in the respective plot minus 50% of the Minimum Value obtained in the respective plot. Maximum obey the same criteria from Cost Maximum.

Cost_Six_ymax = max(([Custo_Joelho_SpeedSix_Mean, Custo_Quadril_SpeedSix_Mean, Custo_Umbigo_SpeedSix_Mean, Custo_Xifoide_SpeedSix_Mean]) + 0.5*max([Custo_Joelho_SpeedSix_Mean, Custo_Quadril_SpeedSix_Mean, Custo_Umbigo_SpeedSix_Mean, Custo_Xifoide_SpeedSix_Mean]))
Drag_F_Six_ymin = min(([Drag_F_Joelho_SpeedSix_Mean, Drag_F_Quadril_SpeedSix_Mean, Drag_F_Umbigo_SpeedSix_Mean, Drag_F_Xifoide_SpeedSix_Mean]) - 0.5*min([Drag_F_Joelho_SpeedSix_Mean, Drag_F_Quadril_SpeedSix_Mean, Drag_F_Umbigo_SpeedSix_Mean, Drag_F_Xifoide_SpeedSix_Mean]))
Drag_F_Six_ymax = max(([Drag_F_Joelho_SpeedSix_Mean, Drag_F_Quadril_SpeedSix_Mean, Drag_F_Umbigo_SpeedSix_Mean, Drag_F_Xifoide_SpeedSix_Mean]) + 0.5*max([Drag_F_Joelho_SpeedSix_Mean, Drag_F_Quadril_SpeedSix_Mean, Drag_F_Umbigo_SpeedSix_Mean, Drag_F_Xifoide_SpeedSix_Mean]))
GRFV_MEAN_ymin = min(([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]) - 0.5*min([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]))
GRFV_MEAN_ymax = max(([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]) + 0.5*max([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]))

host.set_ylim(0,Cost_Six_ymax)
par1.set_ylim(Drag_F_Six_ymin, Drag_F_Six_ymax)
par2.set_ylim(GRFV_MEAN_ymin, GRFV_MEAN_ymax)

host.yaxis.set_ticks(np.arange(2,Cost_Six_ymax, 4))
par1.yaxis.set_ticks(np.arange(20,180,40))
par2.yaxis.set_ticks(np.arange(truncate(GRFV_MEAN_ymin,-2),GRFV_MEAN_ymax,200))


#Polynomial Fit Lines Calculation

# Polynomial 1º Degree Custo 0.6 m/s
Z_1_Custo_SpeedSix,error_1_Custo_SpeedSix,_,_,_ = np.polyfit(Depth_Meters_ALL, Custo_Six_Mean, 1, full=True)
f_1_Custo_SpeedSix = np.poly1d(Z_1_Custo_SpeedSix)
# calculate new x's and y's
X_1_Custo_SpeedSix_new = np.linspace(Depth_Meters_ALL[0], Depth_Meters_ALL[-1], 50)
Y_1_Custo_SpeedSix_new = f_1_Custo_SpeedSix(X_1_Custo_SpeedSix_new)

# Polynomial 2º Degree Custo 0.6 m/s
X_Custo_SpeedSix = Depth_Meters_ALL
Y_Custo_SpeedSix = Custo_Six_Mean

Z_Custo_SpeedSix,error_2_Custo_SpeedSix,_,_,_ = np.polyfit(X_Custo_SpeedSix, Y_Custo_SpeedSix, 2, full=True)
f_Custo_SpeedSix  = np.poly1d(Z_Custo_SpeedSix)
# calculate new x's and y's
X_Custo_SpeedSix_new = np.linspace(min(X_Custo_SpeedSix), max(X_Custo_SpeedSix), 50)
Y_Custo_SpeedSix_new = f_Custo_SpeedSix(X_Custo_SpeedSix_new)
'''
print('Custo_0.6_1º_Degree_Error')
print(error_1_Custo_SpeedSix)
print('Custo_0.6_2º_Degree_Error')
print(error_2_Custo_SpeedSix)
'''

# Polynomial 1º Degree Drag_F 0.6 m/s
Z_1_Drag_F_SpeedSix,error_1_Drag_F_SpeedSix,_,_,_ = np.polyfit(Depth_Meters_ALL, Drag_F_Six_Mean, 1, full=True)
f_1_Drag_F_SpeedSix = np.poly1d(Z_1_Drag_F_SpeedSix)
# calculate new x's and y's
X_1_Drag_F_SpeedSix_new = np.linspace(Depth_Meters_ALL[0], Depth_Meters_ALL[-1], 50)
Y_1_Drag_F_SpeedSix_new = f_1_Drag_F_SpeedSix(X_1_Drag_F_SpeedSix_new)

# Polynomial 2º Degree Drag_F 0.6 m/s
X_Drag_F_SpeedSix = Depth_Meters_ALL
Y_Drag_F_SpeedSix = Drag_F_Six_Mean

Z_Drag_F_SpeedSix,error_2_Drag_F_SpeedSix,_,_,_ = np.polyfit(X_Drag_F_SpeedSix, Y_Drag_F_SpeedSix, 2, full=True)
f_Drag_F_SpeedSix  = np.poly1d(Z_Drag_F_SpeedSix)
# calculate new x's and y's
X_Drag_F_SpeedSix_new = np.linspace(min(X_Drag_F_SpeedSix), max(X_Drag_F_SpeedSix), 50)
Y_Drag_F_SpeedSix_new = f_Drag_F_SpeedSix(X_Drag_F_SpeedSix_new)
'''
print('Drag_F_0.6_1º_Degree_Error')
print(error_1_Drag_F_SpeedSix)
print('Drag_F_0.6_2º_Degree_Error')
print(error_2_Drag_F_SpeedSix)
'''



# Getting the Data to be Plotted
#Error bar
for i in np.arange(0, len(Custo_Four_Mean)):
    p1, = host.plot((Depth_Meters_ALL[i], Depth_Meters_ALL[i]), (Custo_Six_Mean[i]+Custo_Six_CI[i], Custo_Six_Mean[i]-Custo_Six_CI[i]) ,linestyle = '-' ,color='darkgoldenrod', linewidth=lw)
    p2, = par1.plot([Depth_Meters_ALL[i], Depth_Meters_ALL[i]], [Drag_F_Six_Mean[i]+Drag_F_Six_CI[i], Drag_F_Six_Mean[i]-Drag_F_Six_CI[i]], linestyle ='--', color = 'firebrick',  linewidth=lw)
    p3, = par2.plot([Depth_Meters_ALL[i], Depth_Meters_ALL[i]], [GRF_V_MEAN_Mean[i]+GRF_V_MEAN_CI[i], GRF_V_MEAN_Mean[i]-GRF_V_MEAN_CI[i]], linestyle = ':', color = 'mediumblue',  linewidth=lw)
#Lines (Polynomials)
p1, = host.plot(X_Custo_SpeedSix_new, Y_Custo_SpeedSix_new, linestyle = '-' ,color='darkgoldenrod', linewidth=lw, label = 'Cost of Transport')
p2, = par1.plot(X_Drag_F_SpeedSix_new , Y_Drag_F_SpeedSix_new , linestyle ='--', color = 'firebrick',  linewidth=lw, label = 'Drag Force')
p3, = par2.plot(X_GRF_V_MEAN_new, Y_GRF_V_MEAN_new, linestyle = ':', color = 'mediumblue',  linewidth=lw, label='Apparent Weight')

host.legend(fontsize=16, frameon=False, loc='upper left')

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', **tkw)
par1.tick_params(axis='y', **tkw)
par2.tick_params(axis='y', **tkw)
host.tick_params(axis='x', **tkw)

host.set_xlabel("Depth (m)")
host.set_ylabel("Cost of Transport (J/kg/m)")
par1.set_ylabel("Drag Force (N)")
par2.set_ylabel("Apparent Weight (N)")






#FIGURE 11
# COST AND DRAG AND GRFV_MEAN WITH TWO VERTICAL AXIS 0.8 m/s

# Creating figure with 02 Parasite Y Axis
fig = plt.figure()
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
fig.canvas.set_window_title('Cost of Transport and Drag Force and GRFV_Mean 0.8 m/s')
fig.suptitle('0.8 m/s', fontsize = 20)

par1 = host.twinx()
par2 = host.twinx()

# Setting Parasite Y Axis Position
offset = 0
new_fixed_axis = par1.get_grid_helper().new_fixed_axis
par1.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par1,
                                    offset=(offset, 0))
par1.axis["right"].toggle(all=True)

offset = 80
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par2,
                                    offset=(offset, 0))
par2.axis["right"].toggle(all=True)


# Setting Axis Labels and Min/Max Values
host.set_xlim([0.3, 1.5])
# The Axis Values limits are defined in the following manner:
    # COST AXIS: Minimum is Zero. Maximum is the Maximum Value obtained in the respective plot plus 50% of the Maximum Value obtained in the respective plot.
    # DRAG and GRFV_MEAN: Minimum is the Minimum Value obtained in the respective plot minus 50% of the Minimum Value obtained in the respective plot. Maximum obey the same criteria from Cost Maximum.

Cost_Eight_ymax = max(([Custo_Joelho_SpeedEight_Mean, Custo_Quadril_SpeedEight_Mean, Custo_Umbigo_SpeedEight_Mean, Custo_Xifoide_SpeedEight_Mean]) + 0.5*max([Custo_Joelho_SpeedEight_Mean, Custo_Quadril_SpeedEight_Mean, Custo_Umbigo_SpeedEight_Mean, Custo_Xifoide_SpeedEight_Mean]))
Drag_F_Eight_ymin = min(([Drag_F_Joelho_SpeedEight_Mean, Drag_F_Quadril_SpeedEight_Mean, Drag_F_Umbigo_SpeedEight_Mean, Drag_F_Xifoide_SpeedEight_Mean]) - 0.5*min([Drag_F_Joelho_SpeedEight_Mean, Drag_F_Quadril_SpeedEight_Mean, Drag_F_Umbigo_SpeedEight_Mean, Drag_F_Xifoide_SpeedEight_Mean]))
Drag_F_Eight_ymax = max(([Drag_F_Joelho_SpeedEight_Mean, Drag_F_Quadril_SpeedEight_Mean, Drag_F_Umbigo_SpeedEight_Mean, Drag_F_Xifoide_SpeedEight_Mean]) + 0.5*max([Drag_F_Joelho_SpeedEight_Mean, Drag_F_Quadril_SpeedEight_Mean, Drag_F_Umbigo_SpeedEight_Mean, Drag_F_Xifoide_SpeedEight_Mean]))
GRFV_MEAN_ymin = min(([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]) - 0.5*min([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]))
GRFV_MEAN_ymax = max(([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]) + 0.5*max([GRF_V_MEAN_Joelho_Mean, GRF_V_MEAN_Quadril_Mean, GRF_V_MEAN_Umbigo_Mean, GRF_V_MEAN_Xifoide_Mean]))

host.set_ylim(0,14)
par1.set_ylim(Drag_F_Eight_ymin, Drag_F_Eight_ymax)
par2.set_ylim(GRFV_MEAN_ymin, GRFV_MEAN_ymax)

host.yaxis.set_ticks(np.arange(2,16, 4))
par2.yaxis.set_ticks(np.arange(truncate(GRFV_MEAN_ymin,-2),GRFV_MEAN_ymax,200))


#Polynomial Fit Lines Calculation

# Polynomial 1º Degree Custo 0.8 m/s
Z_1_Custo_SpeedEight,error_1_Custo_SpeedEight,_,_,_ = np.polyfit(Depth_Meters_ALL, Custo_Eight_Mean, 1, full=True)
f_1_Custo_SpeedEight = np.poly1d(Z_1_Custo_SpeedEight)
# calculate new x's and y's
X_1_Custo_SpeedEight_new = np.linspace(Depth_Meters_ALL[0], Depth_Meters_ALL[-1], 50)
Y_1_Custo_SpeedEight_new = f_1_Custo_SpeedEight(X_1_Custo_SpeedEight_new)

# Polynomial 2º Degree Custo 0.8 m/s
X_Custo_SpeedEight = Depth_Meters_ALL
Y_Custo_SpeedEight = Custo_Eight_Mean

Z_Custo_SpeedEight,error_2_Custo_SpeedEight,_,_,_ = np.polyfit(X_Custo_SpeedEight, Y_Custo_SpeedEight, 2, full=True)
f_Custo_SpeedEight  = np.poly1d(Z_Custo_SpeedEight)
# calculate new x's and y's
X_Custo_SpeedEight_new = np.linspace(min(X_Custo_SpeedEight), max(X_Custo_SpeedEight), 50)
Y_Custo_SpeedEight_new = f_Custo_SpeedEight(X_Custo_SpeedEight_new)
'''
print('Custo_0.8_1º_Degree_Error')
print(error_1_Custo_SpeedEight)
print('Custo_0.8_2º_Degree_Error')
print(error_2_Custo_SpeedEight)
'''

# Polynomial 1º Degree Drag_F 0.8 m/s
Z_1_Drag_F_SpeedEight,error_1_Drag_F_SpeedEight,_,_,_ = np.polyfit(Depth_Meters_ALL, Drag_F_Eight_Mean, 1, full=True)
f_1_Drag_F_SpeedEight = np.poly1d(Z_1_Drag_F_SpeedEight)
# calculate new x's and y's
X_1_Drag_F_SpeedEight_new = np.linspace(Depth_Meters_ALL[0], Depth_Meters_ALL[-1], 50)
Y_1_Drag_F_SpeedEight_new = f_1_Drag_F_SpeedEight(X_1_Drag_F_SpeedEight_new)

# Polynomial 2º Degree Drag_F 0.8 m/s
X_Drag_F_SpeedEight = Depth_Meters_ALL
Y_Drag_F_SpeedEight = Drag_F_Eight_Mean

Z_Drag_F_SpeedEight,error_2_Drag_F_SpeedEight,_,_,_ = np.polyfit(X_Drag_F_SpeedEight, Y_Drag_F_SpeedEight, 2, full=True)
f_Drag_F_SpeedEight  = np.poly1d(Z_Drag_F_SpeedEight)
# calculate new x's and y's
X_Drag_F_SpeedEight_new = np.linspace(min(X_Drag_F_SpeedEight), max(X_Drag_F_SpeedEight), 50)
Y_Drag_F_SpeedEight_new = f_Drag_F_SpeedEight(X_Drag_F_SpeedEight_new)
'''
print('Drag_F_0.8_1º_Degree_Error')
print(error_1_Drag_F_SpeedEight)
print('Drag_F_0.8_2º_Degree_Error')
print(error_2_Drag_F_SpeedEight)
'''


# Getting the Data to be Plotted
#Error bar
for i in np.arange(0, len(Custo_Four_Mean)):
    p1, = host.plot((Depth_Meters_ALL[i], Depth_Meters_ALL[i]), (Custo_Eight_Mean[i]+Custo_Eight_CI[i], Custo_Eight_Mean[i]-Custo_Eight_CI[i]) ,linestyle = '-' ,color='darkgoldenrod', linewidth=lw)
    p2, = par1.plot([Depth_Meters_ALL[i], Depth_Meters_ALL[i]], [Drag_F_Eight_Mean[i]+Drag_F_Eight_CI[i], Drag_F_Eight_Mean[i]-Drag_F_Eight_CI[i]], linestyle ='--', color = 'firebrick',  linewidth=lw)
    p3, = par2.plot([Depth_Meters_ALL[i], Depth_Meters_ALL[i]], [GRF_V_MEAN_Mean[i]+GRF_V_MEAN_CI[i], GRF_V_MEAN_Mean[i]-GRF_V_MEAN_CI[i]], linestyle = ':', color = 'mediumblue',  linewidth=lw)
#Lines (Polynomials)
p1, = host.plot(X_Custo_SpeedEight_new, Y_Custo_SpeedEight_new, linestyle = '-' ,color='darkgoldenrod', linewidth=lw, label = 'Cost of Transport')
p2, = par1.plot(X_Drag_F_SpeedEight_new , Y_Drag_F_SpeedEight_new , linestyle ='--', color = 'firebrick',  linewidth=lw, label = 'Drag Force')
p3, = par2.plot(X_GRF_V_MEAN_new, Y_GRF_V_MEAN_new, linestyle = ':', color = 'mediumblue',  linewidth=lw, label='Apparent Weight')

host.legend(fontsize=16, frameon=False, loc='upper left')

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', **tkw)
par1.tick_params(axis='y', **tkw)
par2.tick_params(axis='y', **tkw)
host.tick_params(axis='x', **tkw)

host.set_xlabel("Depth (m)")
host.set_ylabel("Cost of Transport (J/kg/m)")
par1.set_ylabel("Drag Force (N)")
par2.set_ylabel("Apparent Weight (N)")


#FIGURE 12
#COST PER SPEED, WITH LINES OF DEPTHS (POLYNOMIAL FIT)

#Prepare Matrix to PloyFit
Custo_AllDepths_Mean_withSpeedColumn = np.vstack((Custo_Joelho_All_Speed_Mean_withSpeedColumn, Custo_Quadril_All_Speed_Mean_withSpeedColumn))
Custo_AllDepths_Mean_withSpeedColumn = np.vstack((Custo_AllDepths_Mean_withSpeedColumn, Custo_Umbigo_All_Speed_Mean_withSpeedColumn))
Custo_AllDepths_Mean_withSpeedColumn = np.vstack((Custo_AllDepths_Mean_withSpeedColumn, Custo_Xifoide_All_Speed_Mean_withSpeedColumn))
X_Custo_AllDepths = Custo_AllDepths_Mean_withSpeedColumn[:,0]   #Speed
Y_Custo_AllDepths = Custo_AllDepths_Mean_withSpeedColumn[:,1]   #Custo

'''
# Calculate Polynomial Parameters of 1º Degree
Z_1,error_1,_,_,_ = np.polyfit(X, Y, 1, full=True)
f_1 = np.poly1d(Z_1)
Text_1 = ["%.2f" % x for x in Z_1]
Error_1 = ["%.2f" % x for x in error_1]
# calculate new x's and y's
X_1_new = np.linspace(X[0], X[-1], 50)
Y_1_new = f_1(X_1_new)
'''

# Calculate Polynomial Parameters of 2º Degree All Depths
Z_Custo_AllDepths,error_Custo_AllDepths,_,_,_ = np.polyfit(X_Custo_AllDepths, Y_Custo_AllDepths, 2, full=True)
f_Custo_AllDepths = np.poly1d(Z_Custo_AllDepths)
#Text_2 = ["%.2f" % x for x in Z_Custo_AllDepths]
#Error_2 = ["%.2f" % x for x in error_Custo_AllDepths]
# calculate new x's and y's
X_Custo_AllDepths_new = np.linspace(min(X_Custo_AllDepths), max(X_Custo_AllDepths), 50)
Y_Custo_AllDepths_new = f_Custo_AllDepths(X_Custo_AllDepths_new)

# Polynomial 2º Degree Joelho
X_Custo_Joelho = Custo_Joelho_All_Speed_Mean_withSpeedColumn[:,0]
Y_Custo_Joelho = Custo_Joelho_All_Speed_Mean_withSpeedColumn[:,1]

Z_Custo_Joelho,error_2,_,_,_ = np.polyfit(X_Custo_Joelho, Y_Custo_Joelho, 2, full=True)
f_Custo_Joelho  = np.poly1d(Z_Custo_Joelho)
# calculate new x's and y's
X_Custo_Joelho_new = np.linspace(min(X_Custo_Joelho ), 1.05, 50)
Y_Custo_Joelho_new = f_Custo_Joelho(X_Custo_Joelho_new)

# Polynomial 2º Degree Quadril
X_Custo_Quadril = Custo_Quadril_All_Speed_Mean_withSpeedColumn[:,0]
Y_Custo_Quadril = Custo_Quadril_All_Speed_Mean_withSpeedColumn[:,1]

Z_Custo_Quadril,error_2,_,_,_ = np.polyfit(X_Custo_Quadril, Y_Custo_Quadril, 2, full=True)
f_Custo_Quadril  = np.poly1d(Z_Custo_Quadril)
# calculate new x's and y's
X_Custo_Quadril_new = np.linspace(min(X_Custo_Quadril), 0.8, 50)
Y_Custo_Quadril_new = f_Custo_Quadril(X_Custo_Quadril_new)

# Polynomial 2º Degree Umbigo
X_Custo_Umbigo = Custo_Umbigo_All_Speed_Mean_withSpeedColumn[:,0]
Y_Custo_Umbigo = Custo_Umbigo_All_Speed_Mean_withSpeedColumn[:,1]

Z_Custo_Umbigo,error_2,_,_,_ = np.polyfit(X_Custo_Umbigo, Y_Custo_Umbigo, 2, full=True)
f_Custo_Umbigo  = np.poly1d(Z_Custo_Umbigo)
# calculate new x's and y's
X_Custo_Umbigo_new = np.linspace(min(X_Custo_Umbigo), 0.8, 50)
Y_Custo_Umbigo_new = f_Custo_Umbigo(X_Custo_Umbigo_new)

# Polynomial 2º Degree Xifoide
X_Custo_Xifoide = Custo_Xifoide_All_Speed_Mean_withSpeedColumn[:,0]
Y_Custo_Xifoide = Custo_Xifoide_All_Speed_Mean_withSpeedColumn[:,1]

Z_Custo_Xifoide,error_2,_,_,_ = np.polyfit(X_Custo_Xifoide, Y_Custo_Xifoide, 2, full=True)
f_Custo_Xifoide  = np.poly1d(Z_Custo_Xifoide)
# calculate new x's and y's
X_Custo_Xifoide_new = np.linspace(min(X_Custo_Xifoide), 0.8, 50)
Y_Custo_Xifoide_new = f_Custo_Xifoide(X_Custo_Xifoide_new)

#Create figure
fig, ax = plt.subplots()
fig.canvas.set_window_title('Cost of Transport per Walking Speed POLYNOMIAL FIT')

ax.errorbar([0.2, 0.4, 0.6, 0.72], Custo_Joelho_All_Speed_Mean_list, yerr=Custo_Joelho_All_Speed_CI_list, fmt='s', color='darkcyan', markersize = ms, linewidth=lw, label = 'Knee')
ax.errorbar([0.2, 0.4, 0.6, 0.73], Custo_Quadril_All_Speed_Mean_list, yerr=Custo_Quadril_All_Speed_CI_list, fmt='o', color='firebrick', markersize = ms, linewidth=lw, label= 'Hip')
ax.errorbar([0.2, 0.4, 0.6, 0.76], Custo_Umbigo_All_Speed_Mean_list, yerr=Custo_Umbigo_All_Speed_CI_list, fmt='d', color='c', markersize = ms, linewidth=lw, label ='Umbilical')
ax.errorbar([0.2, 0.4, 0.6, 0.64], Custo_Xifoide_All_Speed_Mean_list, yerr=Custo_Xifoide_All_Speed_CI_list, fmt='X', color='darkmagenta', markersize = ms, linewidth=lw,  label = 'Xiphoid')
ax.plot([0.2, 0.4, 0.6, 0.8], [Custo_Ardigo_Two, Custo_Ardigo_Four, Custo_Ardigo_Six, Custo_Ardigo_Eight], '-', color='black', linewidth=lw, label = 'Land (Ardigò et al., 2003)')
ax.plot(X_Custo_Ardigo, Y_Custo_Ardigo, '-', color='black', linewidth=lw, label = 'Land (Ardigò et al., 2003)')

ax.plot(X_Custo_Joelho_new, Y_Custo_Joelho_new, '--', color = 'darkcyan',linewidth =lw)
ax.plot(X_Custo_Quadril_new, Y_Custo_Quadril_new, '--', color = 'firebrick',linewidth =lw)
ax.plot(X_Custo_Umbigo_new, Y_Custo_Umbigo_new, '--', color = 'c',linewidth =lw)
ax.plot(X_Custo_Xifoide_new, Y_Custo_Xifoide_new, '--', color = 'darkmagenta',linewidth =lw)

ax.xaxis.set_ticks(np.arange(0.2, 1.8, 0.4))
ax.set_ylim([2, 8])
ax.yaxis.set_ticks(np.arange(2, 8, 2))
fig.suptitle('Cost of Transport', fontsize=20)
plt.xlabel('Speed (m/s)', fontsize=22)
plt.ylabel('Cost of Transport (J/kg/m)', fontsize=22)
ax.tick_params(labelsize=20)

plt.legend(loc = 'best', frameon=False, fontsize=18)

#Print Polynomial Coefficients as Text
#ax.text(0.40, 14.5, 'Polynomial 2º parameters:', fontsize=14)
#ax.text(0.57, 14.5, Text_2[0], fontsize=14)
#ax.text(0.60, 14.5, 'X^2 +', fontsize=14)
#ax.text(0.64, 14.5, Text_2[1], fontsize=14)
#ax.text(0.67, 14.5, 'X +', fontsize=14)
#ax.text(0.70, 14.5, Text_2[2], fontsize=14)
#ax.text(0.40, 13.6, 'Fit error 2º:', fontsize=14)
#ax.text(0.48, 13.6, Error_2[0], fontsize=14)





#FIGURE 13
#METABOLIC POWER NET PER SPEED, WITH LINES OF DEPTHS (POLYNOMIAL FIT)

#Prepare Matrix to PloyFit

PotMet_AllDepths_Mean_withSpeedColumn = np.vstack((PotMet_Joelho_All_Speed_Mean_withSpeedColumn, PotMet_Quadril_All_Speed_Mean_withSpeedColumn))
PotMet_AllDepths_Mean_withSpeedColumn = np.vstack((PotMet_AllDepths_Mean_withSpeedColumn, PotMet_Umbigo_All_Speed_Mean_withSpeedColumn))
PotMet_AllDepths_Mean_withSpeedColumn = np.vstack((PotMet_AllDepths_Mean_withSpeedColumn, PotMet_Xifoide_All_Speed_Mean_withSpeedColumn))
X_PotMet = PotMet_AllDepths_Mean_withSpeedColumn[:,0]   #Speed
Y_PotMet = PotMet_AllDepths_Mean_withSpeedColumn[:,1]   #Custo

# Calculate Polynomial Parameters of 1º Degree
Z_1_PotMet,error_1_PotMet,_,_,_ = np.polyfit(X_PotMet, Y_PotMet, 1, full=True)
f_1_PotMet = np.poly1d(Z_1_PotMet)
Text_1_PotMet = ["%.2f" % x for x in Z_1_PotMet]
Error_1_PotMet = ["%.2f" % x for x in error_1_PotMet]
# calculate new x's and y's
X_1_new_PotMet = np.linspace(X_PotMet[0], X_PotMet[-1], 50)
Y_1_new_PotMet = f_1_PotMet(X_1_new_PotMet)

# Calculate Polynomial Parameters of 2º Degree
Z_2_PotMet,error_2_PotMet,_,_,_ = np.polyfit(X_PotMet, Y_PotMet, 2, full=True)
f_2_PotMet = np.poly1d(Z_2_PotMet)
Text_2_PotMet = ["%.2f" % x for x in Z_2_PotMet]
Error_2_PotMet = ["%.2f" % x for x in error_2_PotMet]
# calculate new x's and y's
X_2_new_PotMet = np.linspace(min(X_PotMet), 0.8, 50)
Y_2_new_PotMet = f_2_PotMet(X_2_new_PotMet)


# Polynomial 2º Degree Joelho
X_PotMet_Joelho = PotMet_Joelho_All_Speed_Mean_withSpeedColumn[:,0]
Y_PotMet_Joelho = PotMet_Joelho_All_Speed_Mean_withSpeedColumn[:,1]

Z_PotMet_Joelho,error_2,_,_,_ = np.polyfit(X_PotMet_Joelho, Y_PotMet_Joelho, 2, full=True)
f_PotMet_Joelho  = np.poly1d(Z_PotMet_Joelho)
# calculate new x's and y's
X_PotMet_Joelho_new = np.linspace(min(X_PotMet_Joelho ), 0.8, 50)
Y_PotMet_Joelho_new = f_PotMet_Joelho(X_PotMet_Joelho_new)

# Polynomial 2º Degree Quadril
X_PotMet_Quadril = PotMet_Quadril_All_Speed_Mean_withSpeedColumn[:,0]
Y_PotMet_Quadril = PotMet_Quadril_All_Speed_Mean_withSpeedColumn[:,1]

Z_PotMet_Quadril,error_2,_,_,_ = np.polyfit(X_PotMet_Quadril, Y_PotMet_Quadril, 2, full=True)
f_PotMet_Quadril  = np.poly1d(Z_PotMet_Quadril)
# calculate new x's and y's
X_PotMet_Quadril_new = np.linspace(min(X_PotMet_Quadril), 0.8, 50)
Y_PotMet_Quadril_new = f_PotMet_Quadril(X_PotMet_Quadril_new)

# Polynomial 2º Degree Umbigo
X_PotMet_Umbigo = PotMet_Umbigo_All_Speed_Mean_withSpeedColumn[:,0]
Y_PotMet_Umbigo = PotMet_Umbigo_All_Speed_Mean_withSpeedColumn[:,1]

Z_PotMet_Umbigo,error_2,_,_,_ = np.polyfit(X_PotMet_Umbigo, Y_PotMet_Umbigo, 2, full=True)
f_PotMet_Umbigo  = np.poly1d(Z_PotMet_Umbigo)
# calculate new x's and y's
X_PotMet_Umbigo_new = np.linspace(min(X_PotMet_Umbigo), 0.8, 50)
Y_PotMet_Umbigo_new = f_PotMet_Umbigo(X_PotMet_Umbigo_new)

# Polynomial 2º Degree Xifoide
X_PotMet_Xifoide = PotMet_Xifoide_All_Speed_Mean_withSpeedColumn[:,0]
Y_PotMet_Xifoide = PotMet_Xifoide_All_Speed_Mean_withSpeedColumn[:,1]

Z_PotMet_Xifoide,error_2,_,_,_ = np.polyfit(X_PotMet_Xifoide, Y_PotMet_Xifoide, 2, full=True)
f_PotMet_Xifoide  = np.poly1d(Z_PotMet_Xifoide)
# calculate new x's and y's
X_PotMet_Xifoide_new = np.linspace(min(X_PotMet_Xifoide), 0.8, 50)
Y_PotMet_Xifoide_new = f_PotMet_Xifoide(X_PotMet_Xifoide_new)

#Create figure
fig, ax = plt.subplots()
fig.canvas.set_window_title('Metabolic Power Net per Walking Speed POLYNOMIAL FIT')

ax.errorbar([0.2, 0.4, 0.6, 0.72], PotMet_Joelho_All_Speed_Mean_list, yerr=PotMet_Joelho_All_Speed_CI_list,fmt='s', color='darkcyan', markersize = ms, linewidth=lw, label = 'Knee')
ax.errorbar([0.2, 0.4, 0.6, 0.73], PotMet_Quadril_All_Speed_Mean_list, yerr=PotMet_Quadril_All_Speed_CI_list, fmt='o', color='firebrick', markersize = ms, linewidth=lw, label= 'Hip')
ax.errorbar([0.2, 0.4, 0.6, 0.76], PotMet_Umbigo_All_Speed_Mean_list, yerr=PotMet_Umbigo_All_Speed_CI_list, fmt='d', color='c', markersize = ms, linewidth=lw, label ='Umbilical')
ax.errorbar([0.2, 0.4, 0.6, 0.64], PotMet_Xifoide_All_Speed_Mean_list, yerr=PotMet_Xifoide_All_Speed_CI_list, fmt='X', color='darkmagenta', markersize = ms, linewidth=lw,  label = 'Xiphoid')

ax.plot(X_PotMet_Joelho_new, Y_PotMet_Joelho_new, '--', color = 'darkcyan',linewidth =lw)
ax.plot(X_PotMet_Quadril_new, Y_PotMet_Quadril_new, '--', color = 'firebrick',linewidth =lw)
ax.plot(X_PotMet_Umbigo_new, Y_PotMet_Umbigo_new, '--', color = 'c',linewidth =lw)
ax.plot(X_PotMet_Xifoide_new, Y_PotMet_Xifoide_new, '--', color = 'darkmagenta',linewidth =lw)

ax.set_ylim([0, 1050])
fig.suptitle('Net Metabolic Power', fontsize=20)
plt.xlabel('Speed (m/s)', fontsize=22)
plt.ylabel('Net Metabolic Power (J/kg/min)', fontsize=22)
ax.tick_params(labelsize=20)
plt.legend(loc = 'best', fontsize=18)

#ax.text(0.40, 700, 'Polynomial 2º parameters:', fontsize=14)
#ax.text(0.57, 700, Text_2_PotMet[0], fontsize=14)
#ax.text(0.62, 700, 'X^2 +', fontsize=14)
#ax.text(0.66, 700, Text_2_PotMet[1], fontsize=14)
#ax.text(0.70, 700, 'X +', fontsize=14)
#ax.text(0.73, 700, Text_2_PotMet[2], fontsize=14)
#ax.text(0.40, 650, 'Fit error 2º:', fontsize=14)
#ax.text(0.48, 650, Error_2_PotMet[0], fontsize=14)

#ax.text(0.40, 600, 'Polynomial 1º parameters:', fontsize=14)
#ax.text(0.57, 600, Text_1_PotMet[0], fontsize=14)
#ax.text(0.62, 600, 'X +', fontsize=14)
#ax.text(0.65, 600, Text_1_PotMet[1], fontsize=14)
#ax.text(0.40, 550, 'Fit error 1º:', fontsize=14)
#ax.text(0.48, 550, Error_1_PotMet[0], fontsize=14)





'''
#FIGURE 14
#COST OF TRANSPORT PER DEPTH (METRIC SCALE) WITH LINES OF SPEEDS (POLYNOMIAL FIT)

#Prepare Matrix to PloyFit
Depth_Meters = Data_Array_Profundidade_Meters[:,1]
Depth_Meters_FullMatrix = np.append(Depth_Meters, Depth_Meters)
Depth_Meters_FullMatrix = np.append(Depth_Meters_FullMatrix, Depth_Meters)
Depth_Meters_FullMatrix = np.append(Depth_Meters_FullMatrix, Depth_Meters)

Custo_SpeedTwo_AllDepths = np.array([Custo_Joelho_SpeedTwo_Mean, Custo_Quadril_SpeedTwo_Mean, Custo_Umbigo_SpeedTwo_Mean, Custo_Xifoide_SpeedTwo_Mean])
Custo_SpeedFour_AllDepths = np.array([Custo_Joelho_SpeedFour_Mean, Custo_Quadril_SpeedFour_Mean, Custo_Umbigo_SpeedFour_Mean, Custo_Xifoide_SpeedFour_Mean])
Custo_SpeedSix_AllDepths = np.array([Custo_Joelho_SpeedSix_Mean, Custo_Quadril_SpeedSix_Mean, Custo_Umbigo_SpeedSix_Mean, Custo_Xifoide_SpeedSix_Mean])
Custo_SpeedEight_AllDepths = np.array([Custo_Joelho_SpeedEight_Mean, Custo_Quadril_SpeedEight_Mean, Custo_Umbigo_SpeedEight_Mean, Custo_Xifoide_SpeedEight_Mean])
Custo_AllSpeeds_perDepth_FullMatrix = np.append(Custo_SpeedTwo_AllDepths, Custo_SpeedFour_AllDepths)
Custo_AllSpeeds_perDepth_FullMatrix = np.append(Custo_AllSpeeds_perDepth_FullMatrix, Custo_SpeedSix_AllDepths)
Custo_AllSpeeds_perDepth_FullMatrix = np.append(Custo_AllSpeeds_perDepth_FullMatrix, Custo_SpeedEight_AllDepths)

Custo_SpeedTwo_AllDepths_list = Custo_SpeedTwo_AllDepths.tolist()
Custo_SpeedFour_AllDepths_list = Custo_SpeedFour_AllDepths.tolist()
Custo_SpeedSix_AllDepths_list = Custo_SpeedSix_AllDepths.tolist()
Custo_SpeedEight_AllDepths_list = Custo_SpeedEight_AllDepths.tolist()

#95%CI MATRIX
Custo_SpeedTwo_AllDepths_CI = np.array([Custo_Joelho_SpeedTwo_CI, Custo_Quadril_SpeedTwo_CI, Custo_Umbigo_SpeedTwo_CI, Custo_Xifoide_SpeedTwo_CI])
Custo_SpeedFour_AllDepths_CI = np.array([Custo_Joelho_SpeedFour_CI, Custo_Quadril_SpeedFour_CI, Custo_Umbigo_SpeedFour_CI, Custo_Xifoide_SpeedFour_CI])
Custo_SpeedSix_AllDepths_CI = np.array([Custo_Joelho_SpeedSix_CI, Custo_Quadril_SpeedSix_CI, Custo_Umbigo_SpeedSix_CI, Custo_Xifoide_SpeedSix_CI])
Custo_SpeedEight_AllDepths_CI = np.array([Custo_Joelho_SpeedEight_CI, Custo_Quadril_SpeedEight_CI, Custo_Umbigo_SpeedEight_CI, Custo_Xifoide_SpeedEight_CI])

Custo_SpeedTwo_AllDepths_CI_list = Custo_SpeedTwo_AllDepths_CI.tolist()
Custo_SpeedFour_AllDepths_CI_list = Custo_SpeedFour_AllDepths_CI.tolist()
Custo_SpeedSix_AllDepths_CI_list = Custo_SpeedSix_AllDepths_CI.tolist()
Custo_SpeedEight_AllDepths_CI_list = Custo_SpeedEight_AllDepths_CI.tolist()

# Calculate Polynomial Parameters of 1º Degree
Z_1_CustoperDepth,error_1_CustoperDepth,_,_,_ = np.polyfit(Depth_Meters_FullMatrix, Custo_AllSpeeds_perDepth_FullMatrix, 1, full=True)
f_1_CustoperDepth = np.poly1d(Z_1_CustoperDepth)
Text_1_CustoperDepth = ["%.2f" % x for x in Z_1_CustoperDepth]
Error_1_CustoperDepth = ["%.2f" % x for x in error_1_CustoperDepth]
# calculate new x's and y's
X_1_new_CustoperDepth = np.linspace(Depth_Meters_FullMatrix[0], Depth_Meters_FullMatrix[-1], 50)
Y_1_new_CustoperDepth = f_1_CustoperDepth(X_1_new_CustoperDepth)

# Calculate Polynomial Parameters of 2º Degree
Z_2_CustoperDepth,error_2_CustoperDepth,_,_,_ = np.polyfit(Depth_Meters_FullMatrix, Custo_AllSpeeds_perDepth_FullMatrix, 2, full=True)
f_2_CustoperDepth = np.poly1d(Z_2_CustoperDepth)
Text_2_CustoperDepth = ["%.2f" % x for x in Z_2_CustoperDepth]
Error_2_CustoperDepth = ["%.2f" % x for x in error_2_CustoperDepth]
# calculate new x's and y's
X_2_new_CustoperDepth = np.linspace(Depth_Meters_FullMatrix[0], Depth_Meters_FullMatrix[-1], 50)
Y_2_new_CustoperDepth = f_2_CustoperDepth(X_2_new_CustoperDepth)

fig, ax = plt.subplots()
fig.canvas.set_window_title('Cost of Transport per Depth POLYNOMIAL FIT')
ax.plot(X_2_new_CustoperDepth, Y_2_new_CustoperDepth, '--', color = 'black',linewidth = 2.5, label= 'Fit Line 2º Degree')
ax.plot(X_1_new_CustoperDepth, Y_1_new_CustoperDepth, '-', color = 'black',linewidth = 2.5, label= 'Fit Line 1º Degree')
ax.errorbar(Depth_Meters, Custo_SpeedTwo_AllDepths_list, yerr=Custo_SpeedTwo_AllDepths_CI_list, fmt='s:', color='darkgray', linewidth=2.5, label = '0.2 m/s')
ax.errorbar(Depth_Meters, Custo_SpeedFour_AllDepths_list, yerr=Custo_SpeedFour_AllDepths_CI_list, fmt='o--', color='darkgray', linewidth=2.5, label= '0.4 m/s')
ax.errorbar(Depth_Meters, Custo_SpeedSix_AllDepths_list, yerr=Custo_SpeedSix_AllDepths_CI_list, fmt='d-.', color='darkgray', linewidth=2.5, label ='0.6 m/s')
ax.errorbar(Depth_Meters, Custo_SpeedEight_AllDepths_list, yerr=Custo_SpeedEight_AllDepths_CI_list, fmt='^--', color='darkgray', linewidth=2.5,  label = '0.8 m/s')
plt.legend(loc = 'best', fontsize=16)

ax.set_ylim([0, 16])
fig.suptitle('Cost of Transport', fontsize=20)
plt.xlabel('Depth (m)', fontsize=18)
plt.ylabel('Cost of Transport (J/kg/m)', fontsize=16)
ax.tick_params(labelsize=14)
plt.legend(loc = 'best', fontsize=16)

ax.text(0.80, 14.5, 'Polynomial 2º parameters:', fontsize=14)
ax.text(1.02, 14.5, Text_2_CustoperDepth[0], fontsize=14)
ax.text(1.06, 14.5, 'X^2 +', fontsize=14)
ax.text(1.12, 14.5, Text_2_CustoperDepth[1], fontsize=14)
ax.text(1.17, 14.5, 'X +', fontsize=14)
ax.text(1.20, 14.5, Text_2_CustoperDepth[2], fontsize=14)
ax.text(0.80, 13.6, 'Fit error 2º:', fontsize=14)
ax.text(0.90, 13.6, Error_2_CustoperDepth[0], fontsize=14)

ax.text(0.80, 12.7, 'Polynomial 1º parameters:', fontsize=14)
ax.text(1.02, 12.7, Text_1_CustoperDepth[0], fontsize=14)
ax.text(1.06, 12.7, 'X +', fontsize=14)
ax.text(1.095, 12.7, Text_1_CustoperDepth[1], fontsize=14)
ax.text(0.80, 11.8, 'Fit error 1º:', fontsize=14)
ax.text(0.90, 11.8, Error_1_CustoperDepth[0], fontsize=14)
'''






'''
#FIGURE 15
#METABOLIC POWER NET PER DEPTH (METRIC SCALE) WITH LINES OF SPEEDS (POLYNOMIAL FIT)

#Prepare Matrix to PloyFit
PotMet_SpeedTwo_AllDepths = np.array([PotMet_Joelho_SpeedTwo_Mean, PotMet_Quadril_SpeedTwo_Mean, PotMet_Umbigo_SpeedTwo_Mean, PotMet_Xifoide_SpeedTwo_Mean])
PotMet_SpeedFour_AllDepths = np.array([PotMet_Joelho_SpeedFour_Mean, PotMet_Quadril_SpeedFour_Mean, PotMet_Umbigo_SpeedFour_Mean, PotMet_Xifoide_SpeedFour_Mean])
PotMet_SpeedSix_AllDepths = np.array([PotMet_Joelho_SpeedSix_Mean, PotMet_Quadril_SpeedSix_Mean, PotMet_Umbigo_SpeedSix_Mean, PotMet_Xifoide_SpeedSix_Mean])
PotMet_SpeedEight_AllDepths = np.array([PotMet_Joelho_SpeedEight_Mean, PotMet_Quadril_SpeedEight_Mean, PotMet_Umbigo_SpeedEight_Mean, PotMet_Xifoide_SpeedEight_Mean])
PotMet_AllSpeeds_perDepth_FullMatrix = np.append(PotMet_SpeedTwo_AllDepths, PotMet_SpeedFour_AllDepths)
PotMet_AllSpeeds_perDepth_FullMatrix = np.append(PotMet_AllSpeeds_perDepth_FullMatrix, PotMet_SpeedSix_AllDepths)
PotMet_AllSpeeds_perDepth_FullMatrix = np.append(PotMet_AllSpeeds_perDepth_FullMatrix, PotMet_SpeedEight_AllDepths)

PotMet_SpeedTwo_AllDepths_list = PotMet_SpeedTwo_AllDepths.tolist()
PotMet_SpeedFour_AllDepths_list = PotMet_SpeedFour_AllDepths.tolist()
PotMet_SpeedSix_AllDepths_list = PotMet_SpeedSix_AllDepths.tolist()
PotMet_SpeedEight_AllDepths_list = PotMet_SpeedEight_AllDepths.tolist()

#95%CI MATRIX
PotMet_SpeedTwo_AllDepths_CI = np.array([PotMet_Joelho_SpeedTwo_CI, PotMet_Quadril_SpeedTwo_CI, PotMet_Umbigo_SpeedTwo_CI, PotMet_Xifoide_SpeedTwo_CI])
PotMet_SpeedFour_AllDepths_CI = np.array([PotMet_Joelho_SpeedFour_CI, PotMet_Quadril_SpeedFour_CI, PotMet_Umbigo_SpeedFour_CI, PotMet_Xifoide_SpeedFour_CI])
PotMet_SpeedSix_AllDepths_CI = np.array([PotMet_Joelho_SpeedSix_CI, PotMet_Quadril_SpeedSix_CI, PotMet_Umbigo_SpeedSix_CI, PotMet_Xifoide_SpeedSix_CI])
PotMet_SpeedEight_AllDepths_CI = np.array([PotMet_Joelho_SpeedEight_CI, PotMet_Quadril_SpeedEight_CI, PotMet_Umbigo_SpeedEight_CI, PotMet_Xifoide_SpeedEight_CI])

PotMet_SpeedTwo_AllDepths_CI_list = PotMet_SpeedTwo_AllDepths_CI.tolist()
PotMet_SpeedFour_AllDepths_CI_list = PotMet_SpeedFour_AllDepths_CI.tolist()
PotMet_SpeedSix_AllDepths_CI_list = PotMet_SpeedSix_AllDepths_CI.tolist()
PotMet_SpeedEight_AllDepths_CI_list = PotMet_SpeedEight_AllDepths_CI.tolist()

# Calculate Polynomial Parameters of 1º Degree
Z_1_PotMetperDepth,error_1_PotMetperDepth,_,_,_ = np.polyfit(Depth_Meters_FullMatrix, PotMet_AllSpeeds_perDepth_FullMatrix, 1, full=True)
f_1_PotMetperDepth = np.poly1d(Z_1_PotMetperDepth)
Text_1_PotMetperDepth = ["%.2f" % x for x in Z_1_PotMetperDepth]
Error_1_PotMetperDepth = ["%.2f" % x for x in error_1_PotMetperDepth]
# calculate new x's and y's
X_1_new_PotMetperDepth = np.linspace(Depth_Meters_FullMatrix[0], Depth_Meters_FullMatrix[-1], 50)
Y_1_new_PotMetperDepth = f_1_PotMetperDepth(X_1_new_PotMetperDepth)

# Calculate Polynomial Parameters of 2º Degree
Z_2_PotMetperDepth,error_2_PotMetperDepth,_,_,_ = np.polyfit(Depth_Meters_FullMatrix, PotMet_AllSpeeds_perDepth_FullMatrix, 2, full=True)
f_2_PotMetperDepth = np.poly1d(Z_2_PotMetperDepth)
Text_2_PotMetperDepth = ["%.2f" % x for x in Z_2_PotMetperDepth]
Error_2_PotMetperDepth = ["%.2f" % x for x in error_2_PotMetperDepth]
# calculate new x's and y's
X_2_new_PotMetperDepth = np.linspace(Depth_Meters_FullMatrix[0], Depth_Meters_FullMatrix[-1], 50)
Y_2_new_PotMetperDepth = f_2_PotMetperDepth(X_2_new_PotMetperDepth)

#Create figure
fig, ax = plt.subplots()
fig.canvas.set_window_title('Metabolic Power Net per Depth POLYNOMIAL FIT')
ax.plot(X_2_new_PotMetperDepth, Y_2_new_PotMetperDepth, '--', color = 'black',linewidth = 2.5, label= 'Fit Line 2º Degree')
ax.plot(X_1_new_PotMetperDepth, Y_1_new_PotMetperDepth, '-', color = 'black',linewidth = 2.5, label= 'Fit Line 1º Degree')
ax.errorbar(Depth_Meters, PotMet_SpeedTwo_AllDepths_list, yerr=PotMet_SpeedTwo_AllDepths_CI_list, fmt='s:', color='darkgray', linewidth=2.5, label = '0.2 m/s')
ax.errorbar(Depth_Meters, PotMet_SpeedFour_AllDepths_list, yerr=PotMet_SpeedFour_AllDepths_CI_list, fmt='o--', color='darkgray', linewidth=2.5, label= 'Hip')
ax.errorbar(Depth_Meters, PotMet_SpeedSix_AllDepths_list, yerr=PotMet_SpeedSix_AllDepths_CI_list, fmt='d-.', color='darkgray', linewidth=2.5, label ='Umbilical')
ax.errorbar(Depth_Meters, PotMet_SpeedEight_AllDepths_list, yerr=PotMet_SpeedEight_AllDepths_CI_list, fmt='^--', color='darkgray', linewidth=2.5,  label = 'Xiphoid')

ax.set_ylim([0, 800])
fig.suptitle('Metabolic Power Net', fontsize=20)
plt.xlabel('Depth (m)', fontsize=18)
plt.ylabel('Metabolic Power (J/kg/min)', fontsize=16)
ax.tick_params(labelsize=14)
plt.legend(loc = 'best', fontsize=16)

ax.text(0.80, 700, 'Polynomial 2º parameters:', fontsize=14)
ax.text(1.02, 700, Text_2_PotMetperDepth[0], fontsize=14)
ax.text(1.08, 700, 'X^2 +', fontsize=14)
ax.text(1.14, 700, Text_2_PotMetperDepth[1], fontsize=14)
ax.text(1.21, 700, 'X +', fontsize=14)
ax.text(1.24, 700, Text_2_PotMetperDepth[2], fontsize=14)
ax.text(0.80, 650, 'Fit error 2º:', fontsize=14)
ax.text(0.90, 650, Error_2_PotMetperDepth[0], fontsize=14)

ax.text(0.80, 600, 'Polynomial 1º parameters:', fontsize=14)
ax.text(1.02, 600, Text_1_PotMetperDepth[0], fontsize=14)
ax.text(1.08, 600, 'X +', fontsize=14)
ax.text(1.11, 600, Text_1_PotMetperDepth[1], fontsize=14)
ax.text(0.80, 550, 'Fit error 1º:', fontsize=14)
ax.text(0.90, 550, Error_1_PotMetperDepth[0], fontsize=14)
'''







#Figure 16
# Cost of Transport Knee and Dry Land (Ardigò et al. 2003)


# Creating figure with 01 Parasite Y Axis
fig = plt.figure()
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
fig.canvas.set_window_title('Cost of Transport Knee and Dry Land')
fig.suptitle('Cost of Transport Knee and Dry Land', fontsize = 20)

par1 = host.twinx()


# Setting Parasite Y Axis Position
offset = 0
new_fixed_axis = par1.get_grid_helper().new_fixed_axis
par1.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par1,
                                    offset=(offset, 0))
par1.axis["right"].toggle(all=True)


# Setting Axis Labels and Min/Max Values
host.set_xlim([0, 2])

host.set_ylim(2,8.5)
par1.set_ylim(4,7)

host.xaxis.set_ticks(np.arange(0.2, 2.2, 0.4))
host.yaxis.set_ticks(np.arange(2,10, 2))
par1.yaxis.set_ticks(np.arange(3,7,1))

# Getting the Data to be Plotted
Custo_Ardigo_Minimum_Index = np.argmin(Y_Custo_Ardigo)
Y_Custo_Ardigo_Minimum = Y_Custo_Ardigo[Custo_Ardigo_Minimum_Index]
X_Custo_Ardigo_Minimum = X_Custo_Ardigo[Custo_Ardigo_Minimum_Index]

Custo_Joelho_Minimum_Index = np.argmin(Y_Custo_Joelho_new)
Y_Custo_Joelho_Minimum = Y_Custo_Joelho_new[Custo_Joelho_Minimum_Index]
X_Custo_Joelho_Minimum = X_Custo_Joelho_new[Custo_Joelho_Minimum_Index]

print("X_Custo_Ardigo_Minimum")
print(X_Custo_Ardigo_Minimum)

print("Y_Custo_Ardigo_Minimum")
print(Y_Custo_Ardigo_Minimum)

print("X_Custo_Joelho_Minimum")
print(X_Custo_Joelho_Minimum)

print("Y_Custo_Joelho_Minimum")
print(Y_Custo_Joelho_Minimum)

#Error bar
Knee_Depth_Speeds = [0.2, 0.4, 0.6, 0.72]
for i in np.arange(0, len(Knee_Depth_Speeds)):
    host.plot((Knee_Depth_Speeds[i], Knee_Depth_Speeds[i]), (Custo_Joelho_All_Speed_Mean_list[i]+Custo_Joelho_All_Speed_CI_list[i], Custo_Joelho_All_Speed_Mean_list[i]-Custo_Joelho_All_Speed_CI_list[i]), linestyle = '-', color='darkcyan', linewidth=lw)

#Lines (Polynomials)
host.plot(X_Custo_Joelho_new, Y_Custo_Joelho_new, '--', color = 'darkcyan',linewidth =lw, label = 'Knee')
par1.plot(X_Custo_Ardigo, Y_Custo_Ardigo, '-', color='black', linewidth=lw, label = 'Dry Land (Ardigò et al., 2003)')
host.scatter(X_Custo_Joelho_Minimum, Y_Custo_Joelho_Minimum , color='darkcyan', s=1000, marker='d')
par1.scatter(X_Custo_Ardigo_Minimum, Y_Custo_Ardigo_Minimum , color='black', s=1000, marker='d')

host.legend(fontsize=16, frameon=False, loc='upper left')

tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', **tkw)
par1.tick_params(axis='y', **tkw)

host.tick_params(axis='x', **tkw)

host.set_xlabel("Speed (m/s)")
host.set_ylabel("Cost Water Knee (J/kg/m)")
par1.set_ylabel("Cost Dry Land (J/kg/m)")


plt.show()