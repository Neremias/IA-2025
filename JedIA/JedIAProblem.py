from simpleai.search import (
    SearchProblem,
    breadth_first,
    depth_first,
    limited_depth_first,
    uniform_cost,
    iterative_limited_depth_first,
    greedy,
    astar,
)

INITIAL_STATE = (
        (2,2), #Posicion del Jed.
        (5), #Puntos de Concentracion.

        #Droides
        [   #(fi,col,canRobots)
            (0, 2, 4),   # 4 droides arriba de todo 
            (1, 2, 2),   # 2 droides cerca del Jedi
            (1, 4, 1),   # 1 droide cerca del Jedi
            (3, 1, 3)    # 3 droides fuera de la habitación
        ]   
    ) 

#Defino como variable global las paredes dado que no van a cambiar entre estado y estado. 
WALLS = [(0,1),
         (1,1),
         (2,1),
         (3,3),
        (3,4),
        (3,5)] 

#Los movimientos tampoco van a modificarse, es decir van a depender de los estados. 
MOVIMIENTOS = {
    "moveLow": (-1,0),
    "moveUp": (+1,0),
}

def hayRobots(coordenadaJed,droides):
    for coordenadaDroide in droides:
        if coordenadaDroide[0:2] == coordenadaJed:
           return True
    
    return False

class JedIaProblem(SearchProblem):
    def cost(self,state1,action,state2):
        return 1
    
    def is_goal(self, state):
        return False
    
    def actions(state):
        posActualJed = state[0]
        rowJed,colJed = state[0]
        puntosConcentracion = state[1]
        droides = state[2]

        MOVIMIENTOS = {
            "move": [(rowJed-1,colJed),
                 (rowJed+1,colJed),
                 (rowJed,colJed-1),
                 (rowJed,colJed+1)],
            "jump": [(rowJed-1,colJed-1),
                 (rowJed-1,colJed+1),
                 (rowJed+1,colJed+1),
                 (rowJed+1,colJed-1)],
            "slash":[(rowJed,colJed)],
            "force":[(rowJed,colJed)],
            "rest":[(rowJed,colJed)],
}
        listaAcciones = []
        casillerosAdyacentes = MOVIMIENTOS["move"]

        for action, listaMovimientos in MOVIMIENTOS.items():

            #recorro la lista de movimientos de mi diccionario (arriba, abajo, izq o dere)
            for movimiento in listaMovimientos:

                #si mi proximo movimiento es move y no es pared entonces me muevo. 
                if action == "move" and movimiento not in WALLS:
                    listaAcciones.append((action,movimiento))

                #si mi proximo movimiento es saltar y no es pared entonces salto. 
                if action == "jump" and movimiento not in WALLS:
                    if puntosConcentracion >= 1:
                        listaAcciones.append((action,movimiento))

                #si mi proximo movimiento es atacar con laser, tengo puntos de concentracion y tengo bots en mi lugar, entonces ataco. 
                if action == "slash" and puntosConcentracion >= 1:
                    if hayRobots(movimiento,droides):
                        listaAcciones.append((action,movimiento))
            
                #si mi proximo movimiento es atacar con fuerza, tengo puntos de concentracion y tengo bots en mi lugar, entonces ataco. 
                if action == "force" and puntosConcentracion >= 5:
                    if hayRobots(movimiento,droides):
                        listaAcciones.append((action,movimiento))
                                  
                #si mi proximo movimiento es descansar y no tengo bots en mi lugar, ni tampoco adyacentemente, entonces descanso. 
                if action == "rest" and hayRobots(movimiento,droides) == False:

                    for casillero in casillerosAdyacentes:
                        #si encuentro por lo menos un casillero con robots, entonces no puedo descansar. 
                        if hayRobots(casillero,droides):
                            break
                      
                    listaAcciones.append((action,posActualJed))     

        return listaAcciones
    
    def result(self,action,state):
        new_state = () 
        return new_state
    
    def heuristic(self, state):
        return True

problem = JedIaProblem(INITIAL_STATE)
result = astar(problem, graph_search=True)