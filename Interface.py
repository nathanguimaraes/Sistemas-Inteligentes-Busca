from PySimpleGUI import PySimpleGUI as sg 
import os
import SimulationController as sc

nameOfWindons = "Sistemas Inteligentes - Busca"

#Class Janela Principal
class UISimulationController():

    #Contrutor
    def __init__(self) -> None:
        sg.theme('Reddit')
        self.GlobalNameEmpty = "Não Há Labirintos Selecionados" 
        self.layoutWithSimulations = [self.GlobalNameEmpty]
        pass

    #Gerar Layout da Interface Princiapl
    def GetBasicInterface(self):

        addFrameLoyout = [
              [sg.T('Diretorio Com os Labirintos que Serão Simulados')],
              [sg.In(key='KeyInputLocal',size=(550,100),enable_events=True)],
              [sg.FolderBrowse("Abrir Pasta",change_submits=True,enable_events=True,target='KeyInputLocal',key="key_OpenFile",size=(25,2)), 
               sg.Button("Iniciar Simulação",key="KeyStartSimulation",visible=False,size=(50,2))],
        ]

        dataSimulation= [
            [
            sg.Text("Labirintos :",border_width=1,background_color='#d0d0d0',size=(20,1)),sg.Text("",key="KeyTotalSimule"),
             sg.Button("Remover",key="KeyRemove",visible=False,button_color="red",size=(75,1)),
            ]
           
        ]
        
        addFrameList= [
            [sg.Frame('Dados Dessa Busca',dataSimulation,font='Any 10',border_width=2,visible=False,key="KeyFrameDataSimule")],
            [sg.Listbox(values = self.layoutWithSimulations,
                        size=(350,10),
                        key="KeyListWithSimulations",
                        background_color='#9FB8AD',
                        pad=(5,5),
                        font="italic",
                        enable_events=True,
                        tooltip="Lista com Todos os Labirintos, Que Serão Simulados"),]     
        ]

        layout = [
            [sg.Frame("Nova Simulação de Busca",addFrameLoyout,font='Any 14')],
            [sg.HorizontalSeparator(pad=None)],
            [sg.Frame('Lista de Labirintos Selecionados',addFrameList,font='Any 12',key="KeyFrameList")],
            [sg.HorizontalSeparator(pad=None)],
        ]

        return layout

    #Busca Nome dos Arquivos no Diretorio
    def CheckCanSimule(self,localDir):
        self.layoutWithSimulations = os.listdir(localDir)

    #Remover Arquivos do Labirinto
    def RemoveSimulation(self,nameRemove): 
        self.layoutWithSimulations.remove(nameRemove[0])
        if(len(self.layoutWithSimulations)==0):
            self.layoutWithSimulations.append(self.GlobalNameEmpty)

    #Atualizar Janela
    def UpdateList(self,GlobalWindons):
        GlobalWindons["KeyTotalSimule"].update(int(len(self.layoutWithSimulations)))
        GlobalWindons["KeyFrameDataSimule"].update(visible = True)

    #Iniciar Janela e Controlador de Eventos
    def StartApp(self):
        globalWindons = sg.Window(nameOfWindons,self.GetBasicInterface(),size=(550,375)) 

        while True:
            events,values = globalWindons.read()    
            globalWindons["KeyRemove"].update(visible = False)    

            if(events == sg.WINDOW_CLOSED):
                break

            if events == "KeyListWithSimulations":
                globalWindons["KeyRemove"].update(visible = True if values["KeyListWithSimulations"][0] != self.GlobalNameEmpty else False) 
            
            if events == "KeyRemove":
                self.RemoveSimulation(values["KeyListWithSimulations"])
                globalWindons["KeyListWithSimulations"].update(self.layoutWithSimulations)
                self.UpdateList(globalWindons)

            if events == "KeyInputLocal":  
                self.CheckCanSimule(values["KeyInputLocal"])
                globalWindons["KeyListWithSimulations"].update(self.layoutWithSimulations)
                self.UpdateList(globalWindons)
            
            if events == "KeyStartSimulation":  
                sc.Memory.listWithAllSimutations.clear()
                if(sc.StartSimulation(values["KeyInputLocal"]+"/",self.layoutWithSimulations)):   
                    showValuesSimule = ShowValuesSimule()
                    showValuesSimule.StartApp()
                

            globalWindons["KeyStartSimulation"].update(visible = True if self.layoutWithSimulations[0] != self.GlobalNameEmpty else False) 

#Class Janela Resultados
class ShowValuesSimule():
    #Construtor
    def __init__(self) -> None:
        sg.theme('Reddit')
        pass

    #Gerar Layout da Janela de Resultados
    def GetBasicInterface(self):
   
        dataSimulation= [
             [sg.Button("Visualizar Detalhes do Labirinto Selecionado",size=(100,2),key="keyViewFile")]
        ]

        dataResusts= [
             [sg.Button("Gerar Tabela",size=(35,2),key="keyButPlotTable"),
              sg.Button("Plotar Grafico",size=(35,2),key="keyButPlotGrafic")
            ]
        ]

        addFramWithAvarageFinal= [
            [sg.Output(size=(500,15),key="KeyOutput")],
        ]
        
        addFrameList= [
            [sg.Frame('Mas Detalhes - Passo a Passo',dataSimulation,font='Any 12',border_width=2,visible=False,key="KeyFrameDataSimule")],
            [sg.Listbox(values = sc.Memory.getListName(),
                        size=(350,6),
                        key="KeyListWithSimulations",
                        background_color='#9FB8AD',
                        pad=(5,5),
                        font="italic",
                        enable_events=True,
                        tooltip="Lista com os Resultados dos Labirintos"),]     
        ]

        #Layout Principal que será inicializado.
        layout = [
            [sg.Frame('Resultados das Buscas Nos Labirintos',addFrameList,font='Any 12',key="KeyFrameList")],
            [sg.HorizontalSeparator(pad=None)],
            [sg.Frame('Medias Finais',addFramWithAvarageFinal,font='Any 10')],
            [sg.HorizontalSeparator(pad=None)],
            [sg.Frame('Resultados',dataResusts,font='Any 10')],
            [sg.HorizontalSeparator(pad=None)],
        ]

        return layout

    #Iniciar Janela e Controlador de Eventos
    def StartApp(self):
        globalWindons = sg.Window(nameOfWindons,self.GetBasicInterface(),size=(550,600)) 

        for i in range(1):
            events,values = globalWindons.read(timeout=10)  
            sc.Memory.getGlobalAvarage()
        
        while True:
            events,values = globalWindons.read()    
    
            if(events == sg.WINDOW_CLOSED):
                break

            if(events == "keyButPlotTable"):
                sc.Memory.setPlotTableGlobal()

            if(events == "keyButPlotGrafic"):
                sc.Memory.setPlotGraficGlobal()

            if events == "keyViewFile":
                UIController = UIViewValues(sc.Memory.getWithName(values["KeyListWithSimulations"][0]))
                UIController.StartApp()

            if events == "KeyListWithSimulations":
                globalWindons["KeyFrameDataSimule"].update(visible = True)

#Class Janela de Detalhes dos Resultados
class UIViewValues():
    #Construtor
    def __init__(self,file) -> None:
        self.file = file
        pass

    #Gera Layout da Janela de Detalhes dos Resultados
    def GetBasicInterface(self):
     
        addFrameLoyout = [
             [sg.Radio('Busca BFS', "RADIO1", default=True,key="typeSearch1",background_color='#9FB8AD'),
                sg.Radio('Busca DFS', "RADIO1",key="typeSearch2",background_color='#9FB8AD'),
                sg.Radio('Busca GBS', "RADIO1",key="typeSearch3",background_color='#9FB8AD'),
                sg.Radio('Busca A*', "RADIO1",key="typeSearch4",background_color='#9FB8AD')],
            [sg.HorizontalSeparator(pad=None)],  
            [sg.Radio('Resultado Final', "RADIO2", default=True,key="isSteps1",background_color='#9FB8AD'),
                sg.Radio('Passo A Passo', "RADIO2",key="isSteps2",background_color='#9FB8AD'),
                sg.Button("Mostra Animação da Busca",key="keyShow",size=(100,1))]
    
        ]

       
        addOutput = [
            [sg.Output(size=(500,15),key="KeyOutput")],
            [sg.Button("Gerar Tabela",size=(29,2),key="keyButPlotTable"), 
             sg.VerticalSeparator(pad=None),
             sg.Button("Plotar Grafico",size=(29,2),key="keyButPlotGrafic"),]
        ]
        
      
        layout = [
            [sg.Text(f"Arquivo Selecionado : {self.file.nameFile}")],
            [sg.HorizontalSeparator(pad=None)],
            [sg.Frame("Visualizar Animação do Passo-A-Passo da Busca",addFrameLoyout,font='Any 12',background_color='#9FB8AD')],
            [sg.HorizontalSeparator(pad=None)],
            [sg.Frame('Comparação Final',addOutput,font='Any 12',key="KeyFrameList")],
            [sg.HorizontalSeparator(pad=None)],
        ]

        return layout

    #Iniciar Janela e Controlador de Eventos
    def StartApp(self):
        globalWindons = sg.Window(nameOfWindons,self.GetBasicInterface(),size=(550,500)) 
        
        for i in range(1):
            events,values = globalWindons.read(timeout=10)  
            self.file.getValueStr()
        
        while True:         
            events,values = globalWindons.read() 
            if(events == sg.WINDOW_CLOSED):
                break

            if(events == "keyButPlotTable"):
                self.file.setPlotTable()

            if(events == "keyButPlotGrafic"):
                self.file.setPlotGrafic()

            if(events =="keyShow"):
                value = True if (values["isSteps1"] == True) else False
                if(values["typeSearch1"] == True):
                    self.file.ShowSteps(0,value)
                elif (values["typeSearch2"] == True):
                    self.file.ShowSteps(1,value)
                elif (values["typeSearch3"] == True):
                    self.file.ShowSteps(2,value)
                elif (values["typeSearch4"] == True):
                    self.file.ShowSteps(3,value)
          
#Inicializar App                      
UIController = UISimulationController()
UIController.StartApp()