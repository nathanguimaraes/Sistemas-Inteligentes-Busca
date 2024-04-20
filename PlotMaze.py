import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Class Plotadora de Tabelas e Gráficos
class PlotMaze():
    #Construtor
    def __init__(self) -> None:
        pass

    #Plotar Tabela 
    def setPlotTable(self,nameTable,collums, rows):
        genericDateFrame = pd.DataFrame(collums,index=rows)
        fig, tableS = plt.subplots()
        fig.patch.set_visible(False)
        tableS.axis('off')
        tableS.axis('tight')
        tableOpened = tableS.table(cellText=genericDateFrame.values,colLabels=genericDateFrame.columns,rowLabels=rows,loc='center')
        tableOpened.auto_set_font_size(False)
        tableOpened.set_fontsize(14)
        fig.set_size_inches(14, 8)
        plt.title(nameTable)
        plt.show()

    #Plotar Gráfico
    def setPlotGrafic(self,title,Algorithms,cost,maxNodes,maxNodeInMemory,interations):     
        penguin_means = {
            'Custo': cost,
            'Nós Expandidos': maxNodes,
            'Max Nós Mémoria': maxNodeInMemory,
            'Interações': interations,
        }

        x = np.arange(len(Algorithms))
        width = 0.15  
        multiplier = 0

        fig, ax = plt.subplots(layout='constrained')
        fig.set_size_inches(12, 8)

        for attribute, measurement in penguin_means.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1
   
        theBigger = 0
        for ss in maxNodes:
            if ss > theBigger:
                theBigger =ss

        ax.set_ylabel('Váriaveis de Desempenho')
        ax.set_title(title)
        ax.set_xticks(x + width, Algorithms)
        ax.legend(loc='upper left', ncols=3)
        ax.set_ylim(0, float(theBigger) + theBigger*0.15)

        plt.show()
