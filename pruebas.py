
INITIAL_STATE = (
        (2,3), #Posicion del Jed.
        (5), #Puntos de Concentracion.

        #Droides
        [   #(fi,col,canRobots)
            (0, 2, 4),   # 4 droides arriba de todo 
            (1, 2, 2),   # 2 droides cerca del Jedi
            (1, 4, 1),   # 1 droide cerca del Jedi
            (3, 1, 3)    # 3 droides fuera de la habitación
        ]   
    ) 
WALLS = [(0,1),
         (1,1),
         (2,1),
         (3,3),
        (3,4),
        (3,5)
        ] 

def actions(state):
    posActualJed = state[0]
    rowJed, colJed = state[0]
    listaAcciones = []

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

    for action, moves in MOVIMIENTOS.items():
        for move in moves:
            if action == "move" and move not in WALLS:
                listaAcciones.append((action,move))
            
            if action == "slash":
                 listaAcciones.append((action,move))
            
            if action == "force":
                listaAcciones.append((action,move))

            if action == "rest":
                listaAcciones.append((action,move))

    return listaAcciones

            
print(actions(INITIAL_STATE))



    #MOVIMIENTOS = {
   # "move": (rowJed-1,),
   # "move": (rowJed+1,0),
   # "move": (0,colJed-1),
   # "move": (0,colJed+1),
   # "jump": (rowJed-1,colJed-1),
   # "jump": (rowJed-1,colJed+1),
   # "jump": (rowJed+1,colJed+1),
   # "jump": (rowJed+1,colJed-1),
#}