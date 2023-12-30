from Grafo import Graph

def fill_graph(g):
    
    g.add_edge("Central", "Avenida Doutor Leonardo Coimbra", 3)
    g.add_edge("Central", "Avenida da Liberdade", 5)
    g.add_edge("Central", "Rua Rei Ricardo II", 4)
    g.add_edge("Central", "Rua de Barros", 7)
    g.add_edge("Central", "Rua da Serrinha", 12)
    g.add_edge("Central", "Rua da Amizade", 10)
    g.add_edge("Rua de Barros", "Rua da Amizade", 9)
    g.add_edge("Rua de Barros", "Rua da Torre", 19)
    g.add_edge("Avenida da Liberdade", "Rua do Montejoia", 14)
    g.add_edge("Avenida da Liberdade", "Rua do Cabo", 19)
    g.add_edge("Avenida da Liberdade", "Avenida Doutor Leonardo Coimbra", 5)
    g.add_edge("Avenida Doutor Leonardo Coimbra", "Rua da Espadilha", 7)
    g.add_edge("Rua Rei Ricardo II", "Rua do Monte", 11)
    g.add_edge("Rua Rei Ricardo II", "Rua da Espadilha", 24)
    g.add_edge("Rua da Serrinha", "Rua da Fonte", 29)
    g.add_edge("Rua da Serrinha", "Rua do Monte", 7)
    g.add_edge("Rua da Espadilha", "Rua da Seara", 14)
    g.add_edge("Rua da Espadilha", "Rua do Monte", 20)
    g.add_edge("Rua do Monte", "Rua dos Canhoes", 8)
    g.add_edge("Rua do Cabo", "Rua dos Canhões", 10)
    
    
#colocar heuristicas em condiçoes
def heuristicaDistanciaLinhaReta(g):
    g.add_heuristica("Central", 0)
    g.add_heuristica("Avenida da Liberdade", 3)
    g.add_heuristica("Avenida Doutor Leonardo Coimbra", 2)
    g.add_heuristica("Rua de Barros", 5)
    g.add_heuristica("Rua Rei Ricardo II", 3)
    g.add_heuristica("Rua da Serrinha", 10)
    g.add_heuristica("Rua do Cabo", 17)
    g.add_heuristica("Rua da Amizade", 8)
    g.add_heuristica("Rua do Montejoia", 12)
    g.add_heuristica("Rua da Torre", 24)
    g.add_heuristica("Rua da Fonte", 32)
    g.add_heuristica("Rua da Seara", 13)
    g.add_heuristica("Rua dos Canhões", 13)
    g.add_heuristica("Rua do Monte", 16)
    g.add_heuristica("Rua da Espadilha", 23)
    
#colocar heuristicas em condiçoes (meter em minuts)
def heuristicaTemporais(g):
    g.add_heuristica("elvas", 270)
    g.add_heuristica("borba", 250)
    g.add_heuristica("estremoz", 145)
    g.add_heuristica("evora", 95)
    g.add_heuristica("montemor", 70)
    g.add_heuristica("vendasnovas", 45)
    g.add_heuristica("arraiolos", 220)
    g.add_heuristica("alcacer", 140)
    g.add_heuristica("palmela", 85)
    g.add_heuristica("almada", 25)
    g.add_heuristica("alandroal", 180)
    g.add_heuristica("redondo", 170)
    g.add_heuristica("monsaraz", 120)
    g.add_heuristica("barreiro", 30)
    g.add_heuristica("baixadabanheira", 33)
    g.add_heuristica("moita", 35)
    g.add_heuristica("alcochete", 26)
    g.add_heuristica("lisboa", 0)

#colocar heuristicas em condiçoes
def heuristicaTransito(g):
    g.add_heuristica("elvas", 270)
    g.add_heuristica("borba", 250)
    g.add_heuristica("estremoz", 145)
    g.add_heuristica("evora", 95)
    g.add_heuristica("montemor", 70)
    g.add_heuristica("vendasnovas", 45)
    g.add_heuristica("arraiolos", 220)
    g.add_heuristica("alcacer", 140)
    g.add_heuristica("palmela", 85)
    g.add_heuristica("almada", 25)
    g.add_heuristica("alandroal", 180)
    g.add_heuristica("redondo", 170)
    g.add_heuristica("monsaraz", 120)
    g.add_heuristica("barreiro", 30)
    g.add_heuristica("baixadabanheira", 33)
    g.add_heuristica("moita", 35)
    g.add_heuristica("alcochete", 26)
    g.add_heuristica("lisboa", 0)