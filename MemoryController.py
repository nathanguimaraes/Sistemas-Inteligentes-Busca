import SimulationController as sc
import numpy as np
import PlotMaze as pt

#Memoria Principal - Controlador
class MemoryController():
    #Construtor
    def __init__(self) -> None:
        self.listWithAllSimutations = []
        self.cost = 0
        self.numberNodesExpanded =0
        self.maxNodesInMemory=0
        self.allSteps = 0

        self.Listcost = []
        self.ListnumberNodesExpanded = []
        self.ListmaxNodesInMemory = []
        self.ListallSteps = []
        pass

    #Adcionar Nova Simulação de Um Arquivo
    def addNewSimule(self,newSimule):
        self.listWithAllSimutations.append(newSimule)
    
    #Recupera Nome das Memorias das Simulações Salvas
    def getListName(self):
        nameTemp = []
        for ss in self.listWithAllSimutations:
            nameTemp.append(ss.nameFile)
        return nameTemp
    
    #Recuperar um Memoria de um Arquivo Pelo Nome
    def getWithName(self,name):
        for ss in self.listWithAllSimutations:
            if(ss.nameFile == name):
                return ss

    #Plotar Grafico com Resultados Finais
    def setPlotGraficGlobal(self):
        plotMazeHelper = pt.PlotMaze()

        algorithms = ["BFS","DFS","GBS","A*"]
    
        plotMazeHelper.setPlotGrafic("Comparação de Desempenho das Buscas no Labirinto",algorithms,self.Listcost,self.ListnumberNodesExpanded, self.ListmaxNodesInMemory, self.ListallSteps)

    #Plotar Tabale dos Resultados Finais
    def setPlotTableGlobal(self):
        plotMazeHelper = pt.PlotMaze()
        valueFinal = {}

        valueFinal["Quantificadores de Desempenho dos Algarismos de Busca"] = [
            f"Custo: {self.Listcost[0]:,.2f} | Nós Expandidos: {self.ListnumberNodesExpanded[0]:,.2f} | Max Nós Mémoria: {self.ListmaxNodesInMemory[0]:,.2f} | Interações: {self.ListallSteps[0]:,.2f}",
            f"Custo: {self.Listcost[1]:,.2f} | Nós Expandidos: {self.ListnumberNodesExpanded[1]:,.2f} | Max Nós Mémoria: {self.ListmaxNodesInMemory[1]:,.2f} | Interações: {self.ListallSteps[1]:,.2f}",
            f"Custo: {self.Listcost[2]:,.2f} | Nós Expandidos: {self.ListnumberNodesExpanded[2]:,.2f} | Max Nós Mémoria: {self.ListmaxNodesInMemory[2]:,.2f} | Interações: {self.ListallSteps[2]:,.2f}",
            f"Custo: {self.Listcost[3]:,.2f} | Nós Expandidos: {self.ListnumberNodesExpanded[3]:,.2f} | Max Nós Mémoria: {self.ListmaxNodesInMemory[3]:,.2f} | Interações: {self.ListallSteps[3]:,.2f}"]
        
        plotMazeHelper.setPlotTable(f"Comparação de Desempenho das Buscas nos Labirintos",valueFinal,["BFS","DFS","GBS","A*"])

    #Exibir Medias Finais 
    def getGlobalAvarage(self):
        self.Listcost.clear()
        self.ListnumberNodesExpanded.clear()
        self.ListmaxNodesInMemory.clear()
        self.ListallSteps.clear()

        def printValue(name,cost,numberNodesExpanded,maxNodesInMemory,allSteps,lengh):
            self.Listcost.append(cost/lengh)
            self.ListnumberNodesExpanded.append(numberNodesExpanded/lengh)
            self.ListmaxNodesInMemory.append(maxNodesInMemory/lengh)
            self.ListallSteps.append(allSteps/lengh)
            print("------------------------------------------------------")
            print(f"Algoritimo: {name}")
            print(f"Custo: {cost/lengh:,.2f} | Nós Expandidos: {numberNodesExpanded/lengh:,.2f} | Max Nós Mémoria: {maxNodesInMemory/lengh:,.2f} | Interações: {allSteps/lengh:,.2f}")
            print("------------------------------------------------------")

        def clearValue():
            self.cost = 0
            self.numberNodesExpanded =0
            self.maxNodesInMemory=0
            self.allSteps = 0

        clearValue()

        lengh = len(self.listWithAllSimutations)
        for ss in self.listWithAllSimutations:
            self.cost += ss.bfs.cost
            self.numberNodesExpanded += ss.bfs.numberNodesExpanded
            self.maxNodesInMemory += ss.bfs.maxNodesInMemory
            self.allSteps += len(ss.bfs.allSteps)
        
       
        printValue("BFS",self.cost,self.numberNodesExpanded,self.maxNodesInMemory,self.allSteps,lengh)

        clearValue()

        for ss in self.listWithAllSimutations:
            self.cost += ss.dfs.cost
            self.numberNodesExpanded += ss.dfs.numberNodesExpanded
            self.maxNodesInMemory += ss.dfs.maxNodesInMemory
            self.allSteps += len(ss.dfs.allSteps)
        
        printValue("DFS",self.cost,self.numberNodesExpanded,self.maxNodesInMemory,self.allSteps,lengh)

        clearValue()

        for ss in self.listWithAllSimutations:
            self.cost += ss.gbs.cost
            self.numberNodesExpanded += ss.gbs.numberNodesExpanded
            self.maxNodesInMemory += ss.gbs.maxNodesInMemory
            self.allSteps  += len(ss.gbs.allSteps)
        
        printValue("GBS",self.cost,self.numberNodesExpanded,self.maxNodesInMemory,self.allSteps,lengh)

        clearValue()
        for ss in self.listWithAllSimutations:
            self.cost += ss.A.cost
            self.numberNodesExpanded += ss.A.numberNodesExpanded
            self.maxNodesInMemory += ss.A.maxNodesInMemory
            self.allSteps  += len(ss.A.allSteps)
        
        printValue("A*",self.cost,self.numberNodesExpanded,self.maxNodesInMemory,self.allSteps,lengh)

#Memoria de Cada Arquivo
class MemorySimule():
    #Construtor
    def __init__(self,nameFile) -> None:
        self.nameFile = nameFile
        self.bfs = None
        self.dfs = None
        self.gbs = None
        self.A = None
        pass

    #Plotar Grafico do Arquivo
    def setPlotGrafic(self):
        plotMazeHelper = pt.PlotMaze()

        algorithms = ["BFS","DFS","GBS","A*"]
        cost = [float(self.bfs.cost),float(self.dfs.cost),float(self.gbs.cost),float(self.A.cost)]
        maxNode = [float(self.bfs.numberNodesExpanded),float(self.dfs.numberNodesExpanded),float(self.gbs.numberNodesExpanded),float(self.A.numberNodesExpanded)]
        maxNodeInMemory = [float(self.bfs.maxNodesInMemory),float(self.dfs.maxNodesInMemory),float(self.gbs.maxNodesInMemory),float(self.A.maxNodesInMemory)]
        interations = [float(len(self.bfs.allSteps)),float(len(self.dfs.allSteps)),float(len(self.gbs.allSteps)),float(len(self.A.allSteps))]

        plotMazeHelper.setPlotGrafic("Comparação de Desempenho das Buscas no Labirinto",algorithms,cost,maxNode,maxNodeInMemory,interations)
    
    #Plotar Table do Arquivo
    def setPlotTable(self):
        plotMazeHelper = pt.PlotMaze()
        valueFinal = {}

        valueFinal["Quantificadores de Desempenho dos Algarismos de Busca"] = [self.bfs.getReturnValue(),
                                                                               self.dfs.getReturnValue(),
                                                                               self.gbs.getReturnValue(),
                                                                               self.A.getReturnValue()]
        
        plotMazeHelper.setPlotTable(f"Comparação de Desempenho das Buscas no Labirinto {self.nameFile}",valueFinal,["BFS","DFS","GBS","A*"])
    
    #Exibir Resultados na Tela de Detalhes
    def getValueStr(self):
        self.bfs.getValueStr()
        self.dfs.getValueStr()
        self.gbs.getValueStr()
        self.A.getValueStr()

    #Mostrar Animaçao do Algoritimo de Busca Selecionado
    def ShowSteps(self,which,isSteps):
        if which == 0:
            self.bfs.ShowSteps(isSteps)
        elif which == 1:
            self.dfs.ShowSteps(isSteps)
        elif which == 2:
            self.gbs.ShowSteps(isSteps)
        elif which == 3:
            self.A.ShowSteps(isSteps)
  
#Momoria Indivual de Cada Algarismo
class MemoryAux():
    #Construtor
    def __init__(self,nameAlgorithm,maze,allSteps,Solution,cost,numberNodesExpanded,maxNodesInMemory) -> None:
        self.nameAlgorithm = nameAlgorithm
        self.maze = maze
        self.allSteps = allSteps
        self.Solution = Solution
        self.cost = cost
        self.numberNodesExpanded = numberNodesExpanded
        self.maxNodesInMemory = maxNodesInMemory
        pass

    #Retorna Resultados  
    def getReturnValue(self):
        return f"Custo: {self.cost:,.2f} | Nós Expandidos: {self.numberNodesExpanded:,.2f} | Max Nós Mémoria: {self.maxNodesInMemory:,.2f} | Interações: {len(self.allSteps)}  "

    #Printar Resultados na Tela
    def getValueStr(self):
        print("------------------------------------------------------")
        print(f"Algoritimo: {self.nameAlgorithm}")
        print(f"Custo: {self.cost:,.2f} | Nós Expandidos: {self.numberNodesExpanded:,.2f} | Max Nós Mémoria: {self.maxNodesInMemory:,.2f} | Interações: {len(self.allSteps)}  ")
        print("------------------------------------------------------")

    #Mostra Animação do Labirinto
    def ShowSteps(self,isSteps):
        maze = np.copy(self.maze)
        solution = list.copy(self.Solution)
        allSteps = list.copy(self.allSteps)
 
        if(isSteps == False):
            sc.mhGlobal.show_maze(maze,allSteps)
            return
        
        sc.mhGlobal.show_maze(maze,solution)