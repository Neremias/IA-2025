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

class JedIaProblem(SearchProblem):

    def cost(self,state1,action,state2):
        return 1
    
    def is_goal(self, state):
        return False
    
    def actions(self,state):
        available_actions = []

        return availableActions
    
    def result(self,action,state):
        new_state = () 
        return new_state
    
    def heuristic(self, state):
        return True

problem = JedIaProblem(INITIAL_STATE)
result = astar(problem, graph_search=True)