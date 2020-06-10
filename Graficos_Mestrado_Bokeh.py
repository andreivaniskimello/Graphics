import numpy as np
import os
import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter


File_Path = os.path.join("C:/Users/andre/Documents/Mestrado/Projetos Pesquisa/Projeto Marcha Água/Coletas/Data/Planilha_Custo_Geral.txt")
Data = pd.read_csv(File_Path,delimiter="\t",header = 0)
Rows = Data.shape[0]
Data_Array = array(Data)

x = Data_Array[:,0]
y = Data_Array[:,1]
z = Data_Array[:,2]
z = np.expand_dims(z,axis=1)

fig = plt.figure()
ax = fig.gca(projection='3d')


#X axis
xticks = [1, 2, 3, 4]
xlabels = ["Joelho", "Quadril", "Umbigo","Xifoide"]
plt.xticks(xticks, xlabels)

#Y axis
yticks = [2, 3, 4, 5]
ylabels = ["0.2 m/s", "0.4 m/s", "0.6 m/s","0.8 m/s"]
plt.yticks(yticks, ylabels)
plt.yticks(np.arange(min(y), max(y)+1, 1.0))

#Z axis
ax.set_zlim(0, 15)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.i'))

ax.set_xlabel('Depth',fontsize=16)
ax.set_ylabel('Speed',fontsize=16)
ax.set_zlabel('Cost of Transport',fontsize=16)
fig.suptitle('Cost of Transport', fontsize=20)

#Scatter Plot Specifications
c = (z)
s = 450
ax.scatter(x,y,z,s=s, c = c, cmap = 'rainbow')

plt.show()