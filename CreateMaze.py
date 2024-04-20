import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

#Classe Criar Maze Atravez do Arquivo
class CreateMazeAndGenetatorUI:
    #Construtor
    def __init__(self) -> None:
        pass

    #Gerando labirinto atravez da Numpy
    def parse_maze(self,maze_str):
        maze = maze_str.split('\n')
        maze = np.array([[tile for tile in row] for row in maze if len(row) > 0])
        return maze

    #Mostrar Labirinto Colorido com MatPlot
    def show_maze(self, mazeOringe,solution ,fontsize = 10):
        cmap = colors.ListedColormap(['white', 'black', 'blue', 'green', 'red', 'gray', 'orange']) 
        fig, ax = plt.subplots()
        fig.set_size_inches(12, 8)
        count =0

        for ss in solution:
            y,x = ss.pos
            if(self.look(mazeOringe,ss.pos) == "G"):
                break
            
            mazeOringe[y,x] = "S"
            maze = np.copy(mazeOringe)
            goal = self.find_pos(maze, 'G')

            maze[maze == ' '] = 0
            maze[maze == 'X'] = 1 # parede
            maze[maze == 'S'] = 2 # estrela
            maze[maze == 'G'] = 3 # meta
            maze[maze == 'P'] = 4 # posicao final
            maze[maze == '.'] = 5 # pontos explorados
            maze[maze == 'F'] = 6 # limite
            maze = maze.astype(int)

            ax.clear()
            ax.imshow(maze, cmap = cmap, norm = colors.BoundaryNorm(list(range(cmap.N + 1)), cmap.N))

           
            plt.text(solution[0].pos[1], solution[0].pos[0], "S", fontsize = fontsize, color = "white",
                            horizontalalignment = 'center',
                            verticalalignment = 'center')
                
            plt.text(goal[1], goal[0], "G", fontsize = fontsize, color = "white",
                            horizontalalignment = 'center',
                            verticalalignment = 'center')

            for last in range(1,count):
                y,x = solution[last].pos
                plt.text(x, y, solution[last].valueCost, fontsize = fontsize, color = "white",
                                    horizontalalignment = 'center',
                                    verticalalignment = 'center')

                
            ax.set_title(f"Interação: {count}")
            count+=1
            plt.pause(0.05)

    #Buscar Posição no Labirinto
    def find_pos(self, maze, what = "S"):
        pos = np.where(maze == what)
        return(tuple([pos[0][0], pos[1][0]]))

    #Olhar no Labirinto
    def look(self, maze, pos):
        x, y = pos
        return(maze[x, y])
