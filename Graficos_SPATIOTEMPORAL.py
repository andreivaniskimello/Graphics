import numpy as np
import os
import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#1º)IMPORT AND PREPARE MATRIX

#DUTY_FACTOR

#JOELHO
File_Path_Duty_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\DutyFactor_Joelho.txt")
Data_Duty_Joelho = pd.read_csv(File_Path_Duty_Joelho,delimiter="\t",header = 0)
Data_Array_Duty_Joelho = np.array(Data_Duty_Joelho)

#0.2 m/s
Duty_Joelho_SpeedTwo_Mean = Data_Array_Duty_Joelho[0,1]
Duty_Joelho_SpeedTwo_CIUpper = Data_Array_Duty_Joelho[0,4]
Duty_Joelho_SpeedTwo_CI = Duty_Joelho_SpeedTwo_CIUpper - Duty_Joelho_SpeedTwo_Mean
    #0.4 m/s
Duty_Joelho_SpeedFour_Mean = Data_Array_Duty_Joelho[1,1]
Duty_Joelho_SpeedFour_CIUpper = Data_Array_Duty_Joelho[1,4]
Duty_Joelho_SpeedFour_CI = Duty_Joelho_SpeedFour_CIUpper - Duty_Joelho_SpeedFour_Mean
    #0.6 m/s
Duty_Joelho_SpeedSix_Mean = Data_Array_Duty_Joelho[2,1]
Duty_Joelho_SpeedSix_CIUpper = Data_Array_Duty_Joelho[2,4]
Duty_Joelho_SpeedSix_CI = Duty_Joelho_SpeedSix_CIUpper - Duty_Joelho_SpeedSix_Mean
    #0.8 m/s
Duty_Joelho_SpeedEight_Mean = Data_Array_Duty_Joelho[3,1]
Duty_Joelho_SpeedEight_CIUpper = Data_Array_Duty_Joelho[3,4]
Duty_Joelho_SpeedEight_CI = Duty_Joelho_SpeedEight_CIUpper - Duty_Joelho_SpeedEight_Mean

    #ALL SPEEDS
Duty_Joelho_Speed_Column = Data_Array_Duty_Joelho[:,0]
Duty_Joelho_All_Speed_Mean = Data_Array_Duty_Joelho[:,1]
Duty_Joelho_All_Speed_CIUpper = Data_Array_Duty_Joelho[:,4]
Duty_Joelho_All_Speed_CI = Duty_Joelho_All_Speed_CIUpper - Duty_Joelho_All_Speed_Mean
Duty_Joelho_All_Speed_Mean_list = Duty_Joelho_All_Speed_Mean.tolist()
Duty_Joelho_All_Speed_CI_list = Duty_Joelho_All_Speed_CI.tolist()

#QUADRIL
File_Path_Duty_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\DutyFactor_Quadril.txt")
Data_Duty_Quadril = pd.read_csv(File_Path_Duty_Quadril,delimiter="\t",header = 0)
Data_Array_Duty_Quadril = np.array(Data_Duty_Quadril)

#0.2 m/s
Duty_Quadril_SpeedTwo_Mean = Data_Array_Duty_Quadril[0,1]
Duty_Quadril_SpeedTwo_CIUpper = Data_Array_Duty_Quadril[0,4]
Duty_Quadril_SpeedTwo_CI = Duty_Quadril_SpeedTwo_CIUpper - Duty_Quadril_SpeedTwo_Mean
    #0.4 m/s
Duty_Quadril_SpeedFour_Mean = Data_Array_Duty_Quadril[1,1]
Duty_Quadril_SpeedFour_CIUpper = Data_Array_Duty_Quadril[1,4]
Duty_Quadril_SpeedFour_CI = Duty_Quadril_SpeedFour_CIUpper - Duty_Quadril_SpeedFour_Mean
    #0.6 m/s
Duty_Quadril_SpeedSix_Mean = Data_Array_Duty_Quadril[2,1]
Duty_Quadril_SpeedSix_CIUpper = Data_Array_Duty_Quadril[2,4]
Duty_Quadril_SpeedSix_CI = Duty_Quadril_SpeedSix_CIUpper - Duty_Quadril_SpeedSix_Mean
    #0.8 m/s
Duty_Quadril_SpeedEight_Mean = Data_Array_Duty_Quadril[3,1]
Duty_Quadril_SpeedEight_CIUpper = Data_Array_Duty_Quadril[3,4]
Duty_Quadril_SpeedEight_CI = Duty_Quadril_SpeedEight_CIUpper - Duty_Quadril_SpeedEight_Mean

    #ALL SPEEDS
Duty_Quadril_Speed_Column = Data_Array_Duty_Quadril[:,0]
Duty_Quadril_All_Speed_Mean = Data_Array_Duty_Quadril[:,1]
Duty_Quadril_All_Speed_CIUpper = Data_Array_Duty_Quadril[:,4]
Duty_Quadril_All_Speed_CI = Duty_Quadril_All_Speed_CIUpper - Duty_Quadril_All_Speed_Mean
Duty_Quadril_All_Speed_Mean_list = Duty_Quadril_All_Speed_Mean.tolist()
Duty_Quadril_All_Speed_CI_list = Duty_Quadril_All_Speed_CI.tolist()

#UMBIGO
File_Path_Duty_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\DutyFactor_Umbigo.txt")
Data_Duty_Umbigo = pd.read_csv(File_Path_Duty_Umbigo,delimiter="\t",header = 0)
Data_Array_Duty_Umbigo = np.array(Data_Duty_Umbigo)

#0.2 m/s
Duty_Umbigo_SpeedTwo_Mean = Data_Array_Duty_Umbigo[0,1]
Duty_Umbigo_SpeedTwo_CIUpper = Data_Array_Duty_Umbigo[0,4]
Duty_Umbigo_SpeedTwo_CI = Duty_Umbigo_SpeedTwo_CIUpper - Duty_Umbigo_SpeedTwo_Mean
    #0.4 m/s
Duty_Umbigo_SpeedFour_Mean = Data_Array_Duty_Umbigo[1,1]
Duty_Umbigo_SpeedFour_CIUpper = Data_Array_Duty_Umbigo[1,4]
Duty_Umbigo_SpeedFour_CI = Duty_Umbigo_SpeedFour_CIUpper - Duty_Umbigo_SpeedFour_Mean
    #0.6 m/s
Duty_Umbigo_SpeedSix_Mean = Data_Array_Duty_Umbigo[2,1]
Duty_Umbigo_SpeedSix_CIUpper = Data_Array_Duty_Umbigo[2,4]
Duty_Umbigo_SpeedSix_CI = Duty_Umbigo_SpeedSix_CIUpper - Duty_Umbigo_SpeedSix_Mean
    #0.8 m/s
Duty_Umbigo_SpeedEight_Mean = Data_Array_Duty_Umbigo[3,1]
Duty_Umbigo_SpeedEight_CIUpper = Data_Array_Duty_Umbigo[3,4]
Duty_Umbigo_SpeedEight_CI = Duty_Umbigo_SpeedEight_CIUpper - Duty_Umbigo_SpeedEight_Mean

    #ALL SPEEDS
Duty_Umbigo_Speed_Column = Data_Array_Duty_Umbigo[:,0]
Duty_Umbigo_All_Speed_Mean = Data_Array_Duty_Umbigo[:,1]
Duty_Umbigo_All_Speed_CIUpper = Data_Array_Duty_Umbigo[:,4]
Duty_Umbigo_All_Speed_CI = Duty_Umbigo_All_Speed_CIUpper - Duty_Umbigo_All_Speed_Mean
Duty_Umbigo_All_Speed_Mean_list = Duty_Umbigo_All_Speed_Mean.tolist()
Duty_Umbigo_All_Speed_CI_list = Duty_Umbigo_All_Speed_CI.tolist()

#XIFOIDE
File_Path_Duty_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\DutyFactor_Xifoide.txt")
Data_Duty_Xifoide = pd.read_csv(File_Path_Duty_Xifoide,delimiter="\t",header = 0)
Data_Array_Duty_Xifoide = np.array(Data_Duty_Xifoide)

#0.2 m/s
Duty_Xifoide_SpeedTwo_Mean = Data_Array_Duty_Xifoide[0,1]
Duty_Xifoide_SpeedTwo_CIUpper = Data_Array_Duty_Xifoide[0,4]
Duty_Xifoide_SpeedTwo_CI = Duty_Xifoide_SpeedTwo_CIUpper - Duty_Xifoide_SpeedTwo_Mean
    #0.4 m/s
Duty_Xifoide_SpeedFour_Mean = Data_Array_Duty_Xifoide[1,1]
Duty_Xifoide_SpeedFour_CIUpper = Data_Array_Duty_Xifoide[1,4]
Duty_Xifoide_SpeedFour_CI = Duty_Xifoide_SpeedFour_CIUpper - Duty_Xifoide_SpeedFour_Mean
    #0.6 m/s
Duty_Xifoide_SpeedSix_Mean = Data_Array_Duty_Xifoide[2,1]
Duty_Xifoide_SpeedSix_CIUpper = Data_Array_Duty_Xifoide[2,4]
Duty_Xifoide_SpeedSix_CI = Duty_Xifoide_SpeedSix_CIUpper - Duty_Xifoide_SpeedSix_Mean
    #0.8 m/s
Duty_Xifoide_SpeedEight_Mean = Data_Array_Duty_Xifoide[3,1]
Duty_Xifoide_SpeedEight_CIUpper = Data_Array_Duty_Xifoide[3,4]
Duty_Xifoide_SpeedEight_CI = Duty_Xifoide_SpeedEight_CIUpper - Duty_Xifoide_SpeedEight_Mean

    #ALL SPEEDS
Duty_Xifoide_Speed_Column = Data_Array_Duty_Xifoide[:,0]
Duty_Xifoide_All_Speed_Mean = Data_Array_Duty_Xifoide[:,1]
Duty_Xifoide_All_Speed_CIUpper = Data_Array_Duty_Xifoide[:,4]
Duty_Xifoide_All_Speed_CI = Duty_Xifoide_All_Speed_CIUpper - Duty_Xifoide_All_Speed_Mean
Duty_Xifoide_All_Speed_Mean_list = Duty_Xifoide_All_Speed_Mean.tolist()
Duty_Xifoide_All_Speed_CI_list = Duty_Xifoide_All_Speed_CI.tolist()


#STRIDE_FREQUENCY (SF)
File_Path_SF_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\SF_Joelho.txt")
Data_SF_Joelho = pd.read_csv(File_Path_SF_Joelho,delimiter="\t",header = 0)
Data_Array_SF_Joelho = np.array(Data_SF_Joelho)

#0.2 m/s
SF_Joelho_SpeedTwo_Mean = Data_Array_SF_Joelho[0,1]
SF_Joelho_SpeedTwo_CIUpper = Data_Array_SF_Joelho[0,4]
SF_Joelho_SpeedTwo_CI = SF_Joelho_SpeedTwo_CIUpper - SF_Joelho_SpeedTwo_Mean
    #0.4 m/s
SF_Joelho_SpeedFour_Mean = Data_Array_SF_Joelho[1,1]
SF_Joelho_SpeedFour_CIUpper = Data_Array_SF_Joelho[1,4]
SF_Joelho_SpeedFour_CI = SF_Joelho_SpeedFour_CIUpper - SF_Joelho_SpeedFour_Mean
    #0.6 m/s
SF_Joelho_SpeedSix_Mean = Data_Array_SF_Joelho[2,1]
SF_Joelho_SpeedSix_CIUpper = Data_Array_SF_Joelho[2,4]
SF_Joelho_SpeedSix_CI = SF_Joelho_SpeedSix_CIUpper - SF_Joelho_SpeedSix_Mean
    #0.8 m/s
SF_Joelho_SpeedEight_Mean = Data_Array_SF_Joelho[3,1]
SF_Joelho_SpeedEight_CIUpper = Data_Array_SF_Joelho[3,4]
SF_Joelho_SpeedEight_CI = SF_Joelho_SpeedEight_CIUpper - SF_Joelho_SpeedEight_Mean

    #ALL SPEEDS
SF_Joelho_Speed_Column = Data_Array_SF_Joelho[:,0]
SF_Joelho_All_Speed_Mean = Data_Array_SF_Joelho[:,1]
SF_Joelho_All_Speed_CIUpper = Data_Array_SF_Joelho[:,4]
SF_Joelho_All_Speed_CI = SF_Joelho_All_Speed_CIUpper - SF_Joelho_All_Speed_Mean
SF_Joelho_All_Speed_Mean_list = SF_Joelho_All_Speed_Mean.tolist()
SF_Joelho_All_Speed_CI_list = SF_Joelho_All_Speed_CI.tolist()

#QUADRIL
File_Path_SF_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\SF_Quadril.txt")
Data_SF_Quadril = pd.read_csv(File_Path_SF_Quadril,delimiter="\t",header = 0)
Data_Array_SF_Quadril = np.array(Data_SF_Quadril)

#0.2 m/s
SF_Quadril_SpeedTwo_Mean = Data_Array_SF_Quadril[0,1]
SF_Quadril_SpeedTwo_CIUpper = Data_Array_SF_Quadril[0,4]
SF_Quadril_SpeedTwo_CI = SF_Quadril_SpeedTwo_CIUpper - SF_Quadril_SpeedTwo_Mean
    #0.4 m/s
SF_Quadril_SpeedFour_Mean = Data_Array_SF_Quadril[1,1]
SF_Quadril_SpeedFour_CIUpper = Data_Array_SF_Quadril[1,4]
SF_Quadril_SpeedFour_CI = SF_Quadril_SpeedFour_CIUpper - SF_Quadril_SpeedFour_Mean
    #0.6 m/s
SF_Quadril_SpeedSix_Mean = Data_Array_SF_Quadril[2,1]
SF_Quadril_SpeedSix_CIUpper = Data_Array_SF_Quadril[2,4]
SF_Quadril_SpeedSix_CI = SF_Quadril_SpeedSix_CIUpper - SF_Quadril_SpeedSix_Mean
    #0.8 m/s
SF_Quadril_SpeedEight_Mean = Data_Array_SF_Quadril[3,1]
SF_Quadril_SpeedEight_CIUpper = Data_Array_SF_Quadril[3,4]
SF_Quadril_SpeedEight_CI = SF_Quadril_SpeedEight_CIUpper - SF_Quadril_SpeedEight_Mean

    #ALL SPEEDS
SF_Quadril_Speed_Column = Data_Array_SF_Quadril[:,0]
SF_Quadril_All_Speed_Mean = Data_Array_SF_Quadril[:,1]
SF_Quadril_All_Speed_CIUpper = Data_Array_SF_Quadril[:,4]
SF_Quadril_All_Speed_CI = SF_Quadril_All_Speed_CIUpper - SF_Quadril_All_Speed_Mean
SF_Quadril_All_Speed_Mean_list = SF_Quadril_All_Speed_Mean.tolist()
SF_Quadril_All_Speed_CI_list = SF_Quadril_All_Speed_CI.tolist()

#UMBIGO
File_Path_SF_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\SF_Umbigo.txt")
Data_SF_Umbigo = pd.read_csv(File_Path_SF_Umbigo,delimiter="\t",header = 0)
Data_Array_SF_Umbigo = np.array(Data_SF_Umbigo)

#0.2 m/s
SF_Umbigo_SpeedTwo_Mean = Data_Array_SF_Umbigo[0,1]
SF_Umbigo_SpeedTwo_CIUpper = Data_Array_SF_Umbigo[0,4]
SF_Umbigo_SpeedTwo_CI = SF_Umbigo_SpeedTwo_CIUpper - SF_Umbigo_SpeedTwo_Mean
    #0.4 m/s
SF_Umbigo_SpeedFour_Mean = Data_Array_SF_Umbigo[1,1]
SF_Umbigo_SpeedFour_CIUpper = Data_Array_SF_Umbigo[1,4]
SF_Umbigo_SpeedFour_CI = SF_Umbigo_SpeedFour_CIUpper - SF_Umbigo_SpeedFour_Mean
    #0.6 m/s
SF_Umbigo_SpeedSix_Mean = Data_Array_SF_Umbigo[2,1]
SF_Umbigo_SpeedSix_CIUpper = Data_Array_SF_Umbigo[2,4]
SF_Umbigo_SpeedSix_CI = SF_Umbigo_SpeedSix_CIUpper - SF_Umbigo_SpeedSix_Mean
    #0.8 m/s
SF_Umbigo_SpeedEight_Mean = Data_Array_SF_Umbigo[3,1]
SF_Umbigo_SpeedEight_CIUpper = Data_Array_SF_Umbigo[3,4]
SF_Umbigo_SpeedEight_CI = SF_Umbigo_SpeedEight_CIUpper - SF_Umbigo_SpeedEight_Mean

    #ALL SPEEDS
SF_Umbigo_Speed_Column = Data_Array_SF_Umbigo[:,0]
SF_Umbigo_All_Speed_Mean = Data_Array_SF_Umbigo[:,1]
SF_Umbigo_All_Speed_CIUpper = Data_Array_SF_Umbigo[:,4]
SF_Umbigo_All_Speed_CI = SF_Umbigo_All_Speed_CIUpper - SF_Umbigo_All_Speed_Mean
SF_Umbigo_All_Speed_Mean_list = SF_Umbigo_All_Speed_Mean.tolist()
SF_Umbigo_All_Speed_CI_list = SF_Umbigo_All_Speed_CI.tolist()

#XIFOIDE
File_Path_SF_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\SF_Xifoide.txt")
Data_SF_Xifoide = pd.read_csv(File_Path_SF_Xifoide,delimiter="\t",header = 0)
Data_Array_SF_Xifoide = np.array(Data_SF_Xifoide)

#0.2 m/s
SF_Xifoide_SpeedTwo_Mean = Data_Array_SF_Xifoide[0,1]
SF_Xifoide_SpeedTwo_CIUpper = Data_Array_SF_Xifoide[0,4]
SF_Xifoide_SpeedTwo_CI = SF_Xifoide_SpeedTwo_CIUpper - SF_Xifoide_SpeedTwo_Mean
    #0.4 m/s
SF_Xifoide_SpeedFour_Mean = Data_Array_SF_Xifoide[1,1]
SF_Xifoide_SpeedFour_CIUpper = Data_Array_SF_Xifoide[1,4]
SF_Xifoide_SpeedFour_CI = SF_Xifoide_SpeedFour_CIUpper - SF_Xifoide_SpeedFour_Mean
    #0.6 m/s
SF_Xifoide_SpeedSix_Mean = Data_Array_SF_Xifoide[2,1]
SF_Xifoide_SpeedSix_CIUpper = Data_Array_SF_Xifoide[2,4]
SF_Xifoide_SpeedSix_CI = SF_Xifoide_SpeedSix_CIUpper - SF_Xifoide_SpeedSix_Mean
    #0.8 m/s
SF_Xifoide_SpeedEight_Mean = Data_Array_SF_Xifoide[3,1]
SF_Xifoide_SpeedEight_CIUpper = Data_Array_SF_Xifoide[3,4]
SF_Xifoide_SpeedEight_CI = SF_Xifoide_SpeedEight_CIUpper - SF_Xifoide_SpeedEight_Mean

    #ALL SPEEDS
SF_Xifoide_Speed_Column = Data_Array_SF_Xifoide[:,0]
SF_Xifoide_All_Speed_Mean = Data_Array_SF_Xifoide[:,1]
SF_Xifoide_All_Speed_CIUpper = Data_Array_SF_Xifoide[:,4]
SF_Xifoide_All_Speed_CI = SF_Xifoide_All_Speed_CIUpper - SF_Xifoide_All_Speed_Mean
SF_Xifoide_All_Speed_Mean_list = SF_Xifoide_All_Speed_Mean.tolist()
SF_Xifoide_All_Speed_CI_list = SF_Xifoide_All_Speed_CI.tolist()



#STRIDE_LENGTH (SL)
File_Path_SL_Joelho = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\SL_Joelho.txt")
Data_SL_Joelho = pd.read_csv(File_Path_SL_Joelho,delimiter="\t",header = 0)
Data_Array_SL_Joelho = np.array(Data_SL_Joelho)

#0.2 m/s
SL_Joelho_SpeedTwo_Mean = Data_Array_SL_Joelho[0,1]
SL_Joelho_SpeedTwo_CIUpper = Data_Array_SL_Joelho[0,4]
SL_Joelho_SpeedTwo_CI = SL_Joelho_SpeedTwo_CIUpper - SL_Joelho_SpeedTwo_Mean
    #0.4 m/s
SL_Joelho_SpeedFour_Mean = Data_Array_SL_Joelho[1,1]
SL_Joelho_SpeedFour_CIUpper = Data_Array_SL_Joelho[1,4]
SL_Joelho_SpeedFour_CI = SL_Joelho_SpeedFour_CIUpper - SL_Joelho_SpeedFour_Mean
    #0.6 m/s
SL_Joelho_SpeedSix_Mean = Data_Array_SL_Joelho[2,1]
SL_Joelho_SpeedSix_CIUpper = Data_Array_SL_Joelho[2,4]
SL_Joelho_SpeedSix_CI = SL_Joelho_SpeedSix_CIUpper - SL_Joelho_SpeedSix_Mean
    #0.8 m/s
SL_Joelho_SpeedEight_Mean = Data_Array_SL_Joelho[3,1]
SL_Joelho_SpeedEight_CIUpper = Data_Array_SL_Joelho[3,4]
SL_Joelho_SpeedEight_CI = SL_Joelho_SpeedEight_CIUpper - SL_Joelho_SpeedEight_Mean

    #ALL SPEEDS
SL_Joelho_Speed_Column = Data_Array_SL_Joelho[:,0]
SL_Joelho_All_Speed_Mean = Data_Array_SL_Joelho[:,1]
SL_Joelho_All_Speed_CIUpper = Data_Array_SL_Joelho[:,4]
SL_Joelho_All_Speed_CI = SL_Joelho_All_Speed_CIUpper - SL_Joelho_All_Speed_Mean
SL_Joelho_All_Speed_Mean_list = SL_Joelho_All_Speed_Mean.tolist()
SL_Joelho_All_Speed_CI_list = SL_Joelho_All_Speed_CI.tolist()

#QUADRIL
File_Path_SL_Quadril = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\SL_Quadril.txt")
Data_SL_Quadril = pd.read_csv(File_Path_SL_Quadril,delimiter="\t",header = 0)
Data_Array_SL_Quadril = np.array(Data_SL_Quadril)

#0.2 m/s
SL_Quadril_SpeedTwo_Mean = Data_Array_SL_Quadril[0,1]
SL_Quadril_SpeedTwo_CIUpper = Data_Array_SL_Quadril[0,4]
SL_Quadril_SpeedTwo_CI = SL_Quadril_SpeedTwo_CIUpper - SL_Quadril_SpeedTwo_Mean
    #0.4 m/s
SL_Quadril_SpeedFour_Mean = Data_Array_SL_Quadril[1,1]
SL_Quadril_SpeedFour_CIUpper = Data_Array_SL_Quadril[1,4]
SL_Quadril_SpeedFour_CI = SL_Quadril_SpeedFour_CIUpper - SL_Quadril_SpeedFour_Mean
    #0.6 m/s
SL_Quadril_SpeedSix_Mean = Data_Array_SL_Quadril[2,1]
SL_Quadril_SpeedSix_CIUpper = Data_Array_SL_Quadril[2,4]
SL_Quadril_SpeedSix_CI = SL_Quadril_SpeedSix_CIUpper - SL_Quadril_SpeedSix_Mean
    #0.8 m/s
SL_Quadril_SpeedEight_Mean = Data_Array_SL_Quadril[3,1]
SL_Quadril_SpeedEight_CIUpper = Data_Array_SL_Quadril[3,4]
SL_Quadril_SpeedEight_CI = SL_Quadril_SpeedEight_CIUpper - SL_Quadril_SpeedEight_Mean

    #ALL SPEEDS
SL_Quadril_Speed_Column = Data_Array_SL_Quadril[:,0]
SL_Quadril_All_Speed_Mean = Data_Array_SL_Quadril[:,1]
SL_Quadril_All_Speed_CIUpper = Data_Array_SL_Quadril[:,4]
SL_Quadril_All_Speed_CI = SL_Quadril_All_Speed_CIUpper - SL_Quadril_All_Speed_Mean
SL_Quadril_All_Speed_Mean_list = SL_Quadril_All_Speed_Mean.tolist()
SL_Quadril_All_Speed_CI_list = SL_Quadril_All_Speed_CI.tolist()


#UMBIGO
File_Path_SL_Umbigo = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\SL_Umbigo.txt")
Data_SL_Umbigo = pd.read_csv(File_Path_SL_Umbigo,delimiter="\t",header = 0)
Data_Array_SL_Umbigo = np.array(Data_SL_Umbigo)

#0.2 m/s
SL_Umbigo_SpeedTwo_Mean = Data_Array_SL_Umbigo[0,1]
SL_Umbigo_SpeedTwo_CIUpper = Data_Array_SL_Umbigo[0,4]
SL_Umbigo_SpeedTwo_CI = SL_Umbigo_SpeedTwo_CIUpper - SL_Umbigo_SpeedTwo_Mean
    #0.4 m/s
SL_Umbigo_SpeedFour_Mean = Data_Array_SL_Umbigo[1,1]
SL_Umbigo_SpeedFour_CIUpper = Data_Array_SL_Umbigo[1,4]
SL_Umbigo_SpeedFour_CI = SL_Umbigo_SpeedFour_CIUpper - SL_Umbigo_SpeedFour_Mean
    #0.6 m/s
SL_Umbigo_SpeedSix_Mean = Data_Array_SL_Umbigo[2,1]
SL_Umbigo_SpeedSix_CIUpper = Data_Array_SL_Umbigo[2,4]
SL_Umbigo_SpeedSix_CI = SL_Umbigo_SpeedSix_CIUpper - SL_Umbigo_SpeedSix_Mean
    #0.8 m/s
SL_Umbigo_SpeedEight_Mean = Data_Array_SL_Umbigo[3,1]
SL_Umbigo_SpeedEight_CIUpper = Data_Array_SL_Umbigo[3,4]
SL_Umbigo_SpeedEight_CI = SL_Umbigo_SpeedEight_CIUpper - SL_Umbigo_SpeedEight_Mean

    #ALL SPEEDS
SL_Umbigo_Speed_Column = Data_Array_SL_Umbigo[:,0]
SL_Umbigo_All_Speed_Mean = Data_Array_SL_Umbigo[:,1]
SL_Umbigo_All_Speed_CIUpper = Data_Array_SL_Umbigo[:,4]
SL_Umbigo_All_Speed_CI = SL_Umbigo_All_Speed_CIUpper - SL_Umbigo_All_Speed_Mean
SL_Umbigo_All_Speed_Mean_list = SL_Umbigo_All_Speed_Mean.tolist()
SL_Umbigo_All_Speed_CI_list = SL_Umbigo_All_Speed_CI.tolist()


#XIFOIDE
File_Path_SL_Xifoide = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilhas Gráficos Python/Mean_from_Statistics\SL_Xifoide.txt")
Data_SL_Xifoide = pd.read_csv(File_Path_SL_Xifoide,delimiter="\t",header = 0)
Data_Array_SL_Xifoide = np.array(Data_SL_Xifoide)

#0.2 m/s
SL_Xifoide_SpeedTwo_Mean = Data_Array_SL_Xifoide[0,1]
SL_Xifoide_SpeedTwo_CIUpper = Data_Array_SL_Xifoide[0,4]
SL_Xifoide_SpeedTwo_CI = SL_Xifoide_SpeedTwo_CIUpper - SL_Xifoide_SpeedTwo_Mean
    #0.4 m/s
SL_Xifoide_SpeedFour_Mean = Data_Array_SL_Xifoide[1,1]
SL_Xifoide_SpeedFour_CIUpper = Data_Array_SL_Xifoide[1,4]
SL_Xifoide_SpeedFour_CI = SL_Xifoide_SpeedFour_CIUpper - SL_Xifoide_SpeedFour_Mean
    #0.6 m/s
SL_Xifoide_SpeedSix_Mean = Data_Array_SL_Xifoide[2,1]
SL_Xifoide_SpeedSix_CIUpper = Data_Array_SL_Xifoide[2,4]
SL_Xifoide_SpeedSix_CI = SL_Xifoide_SpeedSix_CIUpper - SL_Xifoide_SpeedSix_Mean
    #0.8 m/s
SL_Xifoide_SpeedEight_Mean = Data_Array_SL_Xifoide[3,1]
SL_Xifoide_SpeedEight_CIUpper = Data_Array_SL_Xifoide[3,4]
SL_Xifoide_SpeedEight_CI = SL_Xifoide_SpeedEight_CIUpper - SL_Xifoide_SpeedEight_Mean

    #ALL SPEEDS
SL_Xifoide_Speed_Column = Data_Array_SL_Xifoide[:,0]
SL_Xifoide_All_Speed_Mean = Data_Array_SL_Xifoide[:,1]
SL_Xifoide_All_Speed_CIUpper = Data_Array_SL_Xifoide[:,4]
SL_Xifoide_All_Speed_CI = SL_Xifoide_All_Speed_CIUpper - SL_Xifoide_All_Speed_Mean
SL_Xifoide_All_Speed_Mean_list = SL_Xifoide_All_Speed_Mean.tolist()
SL_Xifoide_All_Speed_CI_list = SL_Xifoide_All_Speed_CI.tolist()


#2º)FIGURES PLOT


#2D PLOT
#fig, ax = plt.subplots(2, sharex=True)        #Create figure with 2 subplots
#fig.canvas.set_window_title('Spatiotemporal')                 #Set Figure Window Title
#fig.suptitle('Spatiotemporal', fontsize = 14)
ms = 20
lw = 3.5

# FIGURE 1: DUTY FACTOR
#Create figure
fig = plt.figure()
fig.canvas.set_window_title('DUTY FACTOR')
fig.suptitle('Duty Factor', fontsize=20)
bax = brokenaxes(ylims=((0,10), (40, 80)))


# Calculate Polynomial Parameters of 2º Degree

X_Duty_Joelho = Duty_Joelho_Speed_Column      #Speed X
Y_Duty_Joelho = Duty_Joelho_All_Speed_Mean    #Duty Factor Y
Z_2_Duty_Joelho,error_2_Duty_Joelho,_,_,_ = np.polyfit(X_Duty_Joelho, Y_Duty_Joelho, 2, full=True)
f_2_Duty_Joelho = np.poly1d(Z_2_Duty_Joelho)
# calculate new x's and y's
X_2_Duty_Joelho = np.linspace(min(X_Duty_Joelho), max(X_Duty_Joelho), 50)
Y_2_Duty_Joelho = f_2_Duty_Joelho(X_2_Duty_Joelho)

X_Duty_Quadril = Duty_Quadril_Speed_Column      #Speed X
Y_Duty_Quadril = Duty_Quadril_All_Speed_Mean    #Duty Factor Y
Z_2_Duty_Quadril,error_2_Duty_Quadril,_,_,_ = np.polyfit(X_Duty_Quadril, Y_Duty_Quadril, 2, full=True)
f_2_Duty_Quadril = np.poly1d(Z_2_Duty_Quadril)
# calculate new x's and y's
X_2_Duty_Quadril = np.linspace(min(X_Duty_Quadril), max(X_Duty_Quadril), 50)
Y_2_Duty_Quadril = f_2_Duty_Quadril(X_2_Duty_Quadril)

X_Duty_Umbigo = Duty_Umbigo_Speed_Column      #Speed X
Y_Duty_Umbigo = Duty_Umbigo_All_Speed_Mean    #Duty Factor Y
Z_2_Duty_Umbigo,error_2_Duty_Umbigo,_,_,_ = np.polyfit(X_Duty_Umbigo, Y_Duty_Umbigo, 2, full=True)
f_2_Duty_Umbigo = np.poly1d(Z_2_Duty_Umbigo)
# calculate new x's and y's
X_2_Duty_Umbigo = np.linspace(min(X_Duty_Umbigo), max(X_Duty_Umbigo), 50)
Y_2_Duty_Umbigo = f_2_Duty_Umbigo(X_2_Duty_Umbigo)

X_Duty_Xifoide = Duty_Xifoide_Speed_Column      #Speed X
Y_Duty_Xifoide = Duty_Xifoide_All_Speed_Mean    #Duty Factor Y
Z_2_Duty_Xifoide,error_2_Duty_Xifoide,_,_,_ = np.polyfit(X_Duty_Xifoide, Y_Duty_Xifoide, 2, full=True)
f_2_Duty_Xifoide = np.poly1d(Z_2_Duty_Xifoide)
# calculate new x's and y's
X_2_Duty_Xifoide = np.linspace(min(X_Duty_Xifoide), max(X_Duty_Xifoide), 50)
Y_2_Duty_Xifoide = f_2_Duty_Xifoide(X_2_Duty_Xifoide)


bax.errorbar([0.2, 0.4, 0.6, 0.72], Duty_Joelho_All_Speed_Mean_list, yerr=Duty_Joelho_All_Speed_CI_list, fmt='s', color='darkcyan', markersize = ms, linewidth=lw, label = 'Knee')
bax.errorbar([0.2, 0.4, 0.6, 0.73], Duty_Quadril_All_Speed_Mean_list, yerr=Duty_Quadril_All_Speed_CI_list, fmt='o', color='firebrick', markersize = ms, linewidth=lw, label= 'Hip')
bax.errorbar([0.2, 0.4, 0.6, 0.76], Duty_Umbigo_All_Speed_Mean_list, yerr=Duty_Umbigo_All_Speed_CI_list, fmt='d', color='c', markersize = ms, linewidth=lw, label ='Umbilical')
bax.errorbar([0.2, 0.4, 0.6, 0.64], Duty_Xifoide_All_Speed_Mean_list, yerr=Duty_Xifoide_All_Speed_CI_list, fmt='X', color='darkmagenta', markersize = ms, linewidth=lw,  label = 'Xiphoid')

bax.plot(X_2_Duty_Joelho, Y_2_Duty_Joelho, '--', color = 'darkcyan',linewidth =lw)
bax.plot(X_2_Duty_Quadril, Y_2_Duty_Quadril, '--', color = 'firebrick',linewidth =lw)
bax.plot(X_2_Duty_Umbigo, Y_2_Duty_Umbigo, '--', color = 'c',linewidth =lw)
bax.plot(X_2_Duty_Xifoide, Y_2_Duty_Xifoide, '--', color = 'darkmagenta',linewidth =lw)

bax.set_xlabel('Speed (m/s)', fontsize=22)
bax.set_ylabel('Duty Factor (%)', fontsize=22)
#bax.yaxis.set_label_coords(-0.2, 50)
bax.tick_params(labelsize=20)
bax.legend(loc='center left', frameon=False, fontsize=18)




# FIGURE 2: STRIDE FREQUENCY

#Create figure
fig, ax = plt.subplots()
fig.canvas.set_window_title('STRIDE_FREQUENCY')
fig.suptitle('Stride Frequency', fontsize=20)

# Calculate Polynomial Parameters of 2º Degree

X_SF_Joelho = SF_Joelho_Speed_Column      #Speed X
Y_SF_Joelho = SF_Joelho_All_Speed_Mean    #Duty Factor Y
Z_2_SF_Joelho,error_2_SF_Joelho,_,_,_ = np.polyfit(X_SF_Joelho, Y_SF_Joelho, 2, full=True)
f_2_SF_Joelho = np.poly1d(Z_2_SF_Joelho)
# calculate new x's and y's
X_2_SF_Joelho = np.linspace(min(X_SF_Joelho), max(X_SF_Joelho), 50)
Y_2_SF_Joelho = f_2_SF_Joelho(X_2_SF_Joelho)

X_SF_Quadril = SF_Quadril_Speed_Column      #Speed X
Y_SF_Quadril = SF_Quadril_All_Speed_Mean    #Duty Factor Y
Z_2_SF_Quadril,error_2_SF_Quadril,_,_,_ = np.polyfit(X_SF_Quadril, Y_SF_Quadril, 2, full=True)
f_2_SF_Quadril = np.poly1d(Z_2_SF_Quadril)
# calculate new x's and y's
X_2_SF_Quadril = np.linspace(min(X_SF_Quadril), max(X_SF_Quadril), 50)
Y_2_SF_Quadril = f_2_SF_Quadril(X_2_SF_Quadril)

X_SF_Umbigo = SF_Umbigo_Speed_Column      #Speed X
Y_SF_Umbigo = SF_Umbigo_All_Speed_Mean    #Duty Factor Y
Z_2_SF_Umbigo,error_2_SF_Umbigo,_,_,_ = np.polyfit(X_SF_Umbigo, Y_SF_Umbigo, 2, full=True)
f_2_SF_Umbigo = np.poly1d(Z_2_SF_Umbigo)
# calculate new x's and y's
X_2_SF_Umbigo = np.linspace(min(X_SF_Umbigo), max(X_SF_Umbigo), 50)
Y_2_SF_Umbigo = f_2_SF_Umbigo(X_2_SF_Umbigo)

X_SF_Xifoide = SF_Xifoide_Speed_Column      #Speed X
Y_SF_Xifoide = SF_Xifoide_All_Speed_Mean    #Duty Factor Y
Z_2_SF_Xifoide,error_2_SF_Xifoide,_,_,_ = np.polyfit(X_SF_Xifoide, Y_SF_Xifoide, 2, full=True)
f_2_SF_Xifoide = np.poly1d(Z_2_SF_Xifoide)
# calculate new x's and y's
X_2_SF_Xifoide = np.linspace(min(X_SF_Xifoide), max(X_SF_Xifoide), 50)
Y_2_SF_Xifoide = f_2_SF_Xifoide(X_2_SF_Xifoide)


ax.errorbar([0.2, 0.4, 0.6, 0.72], SF_Joelho_All_Speed_Mean_list, yerr=SF_Joelho_All_Speed_CI_list, fmt='s', color='darkcyan', markersize = ms, linewidth=lw, label = 'Knee')
ax.errorbar([0.2, 0.4, 0.6, 0.73], SF_Quadril_All_Speed_Mean_list, yerr=SF_Quadril_All_Speed_CI_list, fmt='o', color='firebrick', markersize = ms, linewidth=lw, label= 'Hip')
ax.errorbar([0.2, 0.4, 0.6, 0.76], SF_Umbigo_All_Speed_Mean_list, yerr=SF_Umbigo_All_Speed_CI_list, fmt='d', color='c', markersize = ms, linewidth=lw, label ='Umbilical')
ax.errorbar([0.2, 0.4, 0.6, 0.64], SF_Xifoide_All_Speed_Mean_list, yerr=SF_Xifoide_All_Speed_CI_list, fmt='X', color='darkmagenta', markersize = ms, linewidth=lw, label ='Xiphoid')

ax.plot(X_2_SF_Joelho, Y_2_SF_Joelho, '--', color = 'darkcyan',linewidth =lw)
ax.plot(X_2_SF_Quadril, Y_2_SF_Quadril, '--', color = 'firebrick',linewidth =lw)
ax.plot(X_2_SF_Umbigo, Y_2_SF_Umbigo, '--', color = 'c',linewidth =lw)
ax.plot(X_2_SF_Xifoide, Y_2_SF_Xifoide, '--', color = 'darkmagenta',linewidth =lw)

ax.set_xlabel('Speed (m/s)', fontsize=22)
ax.set_ylabel('Stride Frequency (Hz)', fontsize=22)
ax.set_ylim([0, 0.8])
ax.tick_params(labelsize=20)
ax.xaxis.set_ticks(np.arange(0.2,1.0,0.2))
ax.yaxis.set_ticks(np.arange(0,1.0,0.2))
ax.legend(loc='best', frameon=False, fontsize=18)


# FIGURE 3: STRIDE LENGTH

#Create figure
fig, ax = plt.subplots()
fig.canvas.set_window_title('STRIDE_LENGTH')
fig.suptitle('Stride Length', fontsize=20)


# Calculate Polynomial Parameters of 2º Degree

X_SL_Joelho = SL_Joelho_Speed_Column      #Speed X
Y_SL_Joelho = SL_Joelho_All_Speed_Mean    #Duty Factor Y
Z_2_SL_Joelho,error_2_SL_Joelho,_,_,_ = np.polyfit(X_SL_Joelho, Y_SL_Joelho, 2, full=True)
f_2_SL_Joelho = np.poly1d(Z_2_SL_Joelho)
# calculate new x's and y's
X_2_SL_Joelho = np.linspace(min(X_SL_Joelho), max(X_SL_Joelho), 50)
Y_2_SL_Joelho = f_2_SL_Joelho(X_2_SL_Joelho)

X_SL_Quadril = SL_Quadril_Speed_Column      #Speed X
Y_SL_Quadril = SL_Quadril_All_Speed_Mean    #Duty Factor Y
Z_2_SL_Quadril,error_2_SL_Quadril,_,_,_ = np.polyfit(X_SL_Quadril, Y_SL_Quadril, 2, full=True)
f_2_SL_Quadril = np.poly1d(Z_2_SL_Quadril)
# calculate new x's and y's
X_2_SL_Quadril = np.linspace(min(X_SL_Quadril), max(X_SL_Quadril), 50)
Y_2_SL_Quadril = f_2_SL_Quadril(X_2_SL_Quadril)

X_SL_Umbigo = SL_Umbigo_Speed_Column      #Speed X
Y_SL_Umbigo = SL_Umbigo_All_Speed_Mean    #Duty Factor Y

Z_2_SL_Umbigo,error_2_SL_Umbigo,_,_,_ = np.polyfit(X_SL_Umbigo, Y_SL_Umbigo, 2, full=True)
f_2_SL_Umbigo = np.poly1d(Z_2_SL_Umbigo)
# calculate new x's and y's
X_2_SL_Umbigo = np.linspace(min(X_SL_Umbigo), max(X_SL_Umbigo), 50)
Y_2_SL_Umbigo = f_2_SL_Umbigo(X_2_SL_Umbigo)

X_SL_Xifoide = SL_Xifoide_Speed_Column      #Speed X
Y_SL_Xifoide = SL_Xifoide_All_Speed_Mean    #Duty Factor Y
Z_2_SL_Xifoide,error_2_SL_Xifoide,_,_,_ = np.polyfit(X_SL_Xifoide, Y_SL_Xifoide, 2, full=True)
f_2_SL_Xifoide = np.poly1d(Z_2_SL_Xifoide)
# calculate new x's and y's
X_2_SL_Xifoide = np.linspace(min(X_SL_Xifoide), max(X_SL_Xifoide), 50)
Y_2_SL_Xifoide = f_2_SL_Xifoide(X_2_SL_Xifoide)


ax.errorbar([0.2, 0.4, 0.6, 0.72], SL_Joelho_All_Speed_Mean_list, yerr=SL_Joelho_All_Speed_CI_list, fmt='s', color='darkcyan', markersize = ms, linewidth=lw, label = 'Knee')
ax.errorbar([0.2, 0.4, 0.6, 0.73], SL_Quadril_All_Speed_Mean_list, yerr=SL_Quadril_All_Speed_CI_list, fmt='o', color='firebrick', markersize = ms, linewidth=lw, label= 'Hip')
ax.errorbar([0.2, 0.4, 0.6, 0.76], SL_Umbigo_All_Speed_Mean_list, yerr=SL_Umbigo_All_Speed_CI_list, fmt='d', color='c', markersize = ms, linewidth=lw, label ='Umbilical')
ax.errorbar([0.2, 0.4, 0.6, 0.64], SL_Xifoide_All_Speed_Mean_list, yerr=SL_Xifoide_All_Speed_CI_list, fmt='X', color='darkmagenta', markersize = ms, linewidth=lw,  label = 'Xiphoid')

ax.plot(X_2_SL_Joelho, Y_2_SL_Joelho, '--', color = 'darkcyan',linewidth =lw)
ax.plot(X_2_SL_Quadril, Y_2_SL_Quadril, '--', color = 'firebrick',linewidth =lw)
ax.plot(X_2_SL_Umbigo, Y_2_SL_Umbigo, '--', color = 'c',linewidth =lw)
ax.plot(X_2_SL_Xifoide, Y_2_SL_Xifoide, '--', color = 'darkmagenta',linewidth =lw)

ax.set_xlabel('Speed (m/s)', fontsize=22)
ax.set_ylabel('Stride Length (m)', fontsize=22)
ax.tick_params(labelsize=20)
ax.set_ylim([0, 1.6])
ax.xaxis.set_ticks(np.arange(0.2,1.0,0.2))
ax.yaxis.set_ticks(np.arange(0,1.8,0.4))
ax.legend(loc='best', frameon=False, fontsize=18)

plt.show()