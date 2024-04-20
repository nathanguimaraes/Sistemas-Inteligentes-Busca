import CreateMaze as mh
import Node as nd
import MemoryController as mc

#Controlador de Uma Simulação de Um Arquivo
class Simulation():
    #Construtor
    def __init__(self,mazeRefStart,mhGlobal) -> None:
        self.mhGlobal = mhGlobal
        self.maze = self.mhGlobal.parse_maze(mazeRefStart)
        self.numberNodesExpanded = 0
        pass

    #Verificar Posição no Labirinto
    def freePosition(self,pos):
        if self.mhGlobal.look(self.maze,pos) == ' ' or self.mhGlobal.look(self.maze,pos) == 'G':
            return True
        return False
   
    #Recuperar Nós do no Fornecido
    def get_children(self,pos):
        

        def addNewChildren(pos,action,cost):
            child_pos = (pos[0],pos[1])
            if  self.freePosition(child_pos):
                child = (child_pos,action,cost)
                children.append(child) 
                self.numberNodesExpanded+=1
          
     
        y,x = pos
        cost = 1
        children = []
        actions = ["N","S","E","W"]
      
        for action in actions:
            if action == "N":
                addNewChildren((y-1,x),action,cost)
            elif action =="S":
                addNewChildren((y+1,x),action,cost)
            elif action == "W":
                addNewChildren((y,x-1),action,cost)
            elif action == "E":
                addNewChildren((y,x+1),action,cost)
            

        return children

    #Verificar Objetivo
    def is_goal(self,pos):
        return (self.mhGlobal.find_pos(self.maze,what = "G") == pos)

    #Algoritimo de Busca BFS
    def bfs(self,incial_state):
        root = nd.Node(incial_state,None,None,0)

        visited = []
        queue = [root]
        allSteps= [root]

        while queue:
            node = queue.pop(0)
            visited.append(node.pos)

            if self.is_goal(node.pos):
                return node.get_path_from_root(), allSteps, node.cost,self.numberNodesExpanded,len(queue)
        
            for child_pos, action, cost in self.get_children(node.pos):
                child = nd.Node(child_pos,node,action,node.cost +cost) 
                if(child.pos not in visited):
                    queue.append(child)
                    allSteps.append(child)
                    


        return queue, allSteps, node.cost,self.numberNodesExpanded,len(queue)

    #Algoritimo de Busca DFS
    def dfs(self,incial_state):        
        root = nd.Node(incial_state,None,None,0)
        
        visited = []
        stack = [root]
        allSteps= [root]

        while stack:
            node = stack.pop()
            visited.append(node.pos)

            if self.is_goal(node.pos):              
                return node.get_path_from_root(),allSteps,node.cost,self.numberNodesExpanded,len(stack)
        
            children = self.get_children(node.pos)
            children.reverse()
            for child_pos, action, cost in children:
                child = nd.Node(child_pos,node,action,node.cost +cost)
                if(child.pos not in visited):
                    stack.append(child)
                    allSteps.append(child)

        return stack,allSteps,node.cost,self.numberNodesExpanded,len(stack)

    #Algoritimo de Busca GBS
    def gbs(self,inicial_state):
        root = nd.Node(inicial_state,None,None,0)     

        stack = [root]
        allSteps= [root]
        visited = []
        fogot = []

        posTarget = self.mhGlobal.find_pos(self.maze,what = "G")  

        def setCostNode(posNode,posTarget):
            value = abs(posTarget[0] - posNode[0]) + abs(posTarget[1] - posNode[1]) 
            return value

        while stack:
            node = stack.pop()
            visited.append(node.pos)
            
            if self.is_goal(node.pos):
                return node.get_path_from_root(), allSteps, node.cost,self.numberNodesExpanded,len(stack)

            bestNote = None

            for child_pos, action, cost in self.get_children(node.pos):
                valueCost = setCostNode(child_pos,posTarget)
                if (bestNote == None and child_pos not in visited):
                    bestNote = nd.Node(child_pos,node,action,node.cost + cost,valueCost=valueCost)
                elif (bestNote != None):
                    newNode = nd.Node(child_pos,node,action,node.cost + cost,valueCost=valueCost)
                    if((valueCost < bestNote.valueCost) and child_pos not in visited):
                        bestNote = newNode
                    else:
                        fogot.append(newNode)

            if (bestNote != None):
                if(bestNote.pos not in visited):
                    stack.append(bestNote)
                    allSteps.append(bestNote)

            if(len(stack) == 0):
                if(len(fogot) >0):
                    allSteps.append(fogot[0])
                    stack = [fogot[0]]
                    fogot.pop(0)

        return stack,allSteps, node.valueCost,self.numberNodesExpanded,len(stack)

    #Algoritimo de Busca A*
    def ASearch(self,inicial_state):
        root = nd.Node(inicial_state,None,None,0)     

        stack = [root]
        allSteps= [root]
        visited = []
        fogot = []

        posTarget = self.mhGlobal.find_pos(self.maze,what = "G")  

        def setCostNode(posNode,posTarget):
            value = abs(posTarget[0] - posNode[0]) + abs(posTarget[1] - posNode[1]) 
            return value

        while stack:
            node = stack.pop()
            visited.append(node.pos)
            
            if self.is_goal(node.pos):
                return node.get_path_from_root(), allSteps, node.valueCost,self.numberNodesExpanded,len(stack)

            bestNote = None

            for child_pos, action, cost in self.get_children(node.pos):
                valueCost = setCostNode(child_pos,posTarget)
                if (bestNote == None and child_pos not in visited):
                    bestNote = nd.Node(child_pos,node,action,node.cost + cost,valueCost= node.cost + valueCost)
                elif (bestNote != None):
                    newNode = nd.Node(child_pos,node,action,node.cost + cost,valueCost= node.cost + valueCost)
                    if((node.cost + valueCost < bestNote.valueCost) and child_pos not in visited):
                        bestNote = newNode
                    else:
                        fogot.append(newNode)

            if (bestNote != None):
                if(bestNote.pos not in visited):
                    stack.append(bestNote)
                    allSteps.append(bestNote)

            if(len(stack) == 0):
                if(len(fogot) >0):
                        allSteps.append(fogot[0])
                        stack = [fogot[0]]
                        fogot.pop(0)

        return stack,allSteps, node.valueCost,self.numberNodesExpanded,len(stack)

#Controlador do Labirinto Atual
class ControllerOfMazeSelected():
    #Construtor
    def __init__(self,localFile,nameFile) -> None:
        self.nameFile = nameFile
        self.localFile = localFile
        self.mazeRefStart = None
        self.openFile()
        pass

    #Abrir Arquivo
    def openFile(self):
        with open(self.localFile, "r") as f:
            self.mazeRefStart = f.read()
    
    #Execultar as 4 Busca no Arquivo Atual
    def executeAllSimulations(self):
        memorySimule = mc.MemorySimule(self.nameFile)
     
        newSimualtionClass = Simulation(self.mazeRefStart,mhGlobal)
        initPos = mhGlobal.find_pos(newSimualtionClass.maze,what = "S")
        solution,allSteps,cost,numberNodesExpanded,maxNodesInMemory = newSimualtionClass.bfs(initPos)
        memorySimule.bfs = mc.MemoryAux("BFS",newSimualtionClass.maze,allSteps,solution,cost,numberNodesExpanded,maxNodesInMemory)

        newSimualtionClass = Simulation(self.mazeRefStart,mhGlobal)
        initPos = mhGlobal.find_pos(newSimualtionClass.maze,what = "S")
        solution,allSteps,cost,numberNodesExpanded,maxNodesInMemory  = newSimualtionClass.dfs(initPos)
        memorySimule.dfs = mc.MemoryAux("DFS",newSimualtionClass.maze,allSteps,solution,cost,numberNodesExpanded,maxNodesInMemory)

        newSimualtionClass = Simulation(self.mazeRefStart,mhGlobal)
        initPos = mhGlobal.find_pos(newSimualtionClass.maze,what = "S")
        solution,allSteps,cost,numberNodesExpanded,maxNodesInMemory  = newSimualtionClass.gbs(initPos)
        memorySimule.gbs = mc.MemoryAux("GBS",newSimualtionClass.maze,allSteps,solution,cost,numberNodesExpanded,maxNodesInMemory)

        newSimualtionClass = Simulation(self.mazeRefStart,mhGlobal)
        initPos = mhGlobal.find_pos(newSimualtionClass.maze,what = "S")
        solution,allSteps,cost,numberNodesExpanded,maxNodesInMemory  = newSimualtionClass.ASearch(initPos)
        memorySimule.A = mc.MemoryAux("A*",newSimualtionClass.maze,allSteps,solution,cost,numberNodesExpanded,maxNodesInMemory)

        Memory.addNewSimule(memorySimule)

#Controlador Geral da Simulação     
class ControllerAllSimulation():
    #Construtor
    def __init__(self,listWhitLocalFiles,localDir) -> None:
        self.Memory = listWhitLocalFiles
        self.listWhitLocalFiles = listWhitLocalFiles
        self.localDir = localDir
        pass

    #Iniciar Simulação em Cada Um dos Arquivos
    def StartSimule(self):
        for nameFiles in self.listWhitLocalFiles:
            Controller = ControllerOfMazeSelected(self.localDir + nameFiles,nameFiles)
            Controller.executeAllSimulations()

#Classe Usadas por Todas as Simulações
mhGlobal = mh.CreateMazeAndGenetatorUI()
Memory = mc.MemoryController()

#Função que Inicia a Simulção
def StartSimulation(dir,files):  
    SimulationController = ControllerAllSimulation(files,dir)
    SimulationController.StartSimule()
    return True



