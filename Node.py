
#Classe dos Nós
class Node:
    #Construtor
    def __init__(self, pos, parent, action, cost,valueCost = 1):
        self.pos = tuple(pos)    
        self.parent = parent     
        self.action = action     
        self.cost = cost    
        self.valueCost = valueCost     

    #Exibir Resultado - NÃO É USADA
    def __str__(self):
        return f"Node - pos = {self.pos}; action = {self.action}; cost = {self.cost}"
    
    #Recuperar Nó
    def get_path_from_root(self):
        node = self
        path = [node]
    
        while not node.parent is None:
            node = node.parent
            path.append(node)
        
        path.reverse()
        
        return(path)

