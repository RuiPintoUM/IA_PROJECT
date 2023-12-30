class Cliente:
    def __init__(self, name, id=-1):     #  construtor do nodo....."
        self.m_id = id
        self.m_name = str(name)

    def __str__(self):
        return "node " + self.m_name
