import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._nodes =[]
        self._edges =[]
        self._lista_stati = []
        self._lista_connessioni = []
        self._id_map_ = {}
        self.selected_state = None

    def load_states(self, n_voli):
        self._lista_stati = DAO.get_nodes(n_voli)
        #print(f"Stati: {len(self._lista_stati)}")

    def load_connessioni(self, n_voli):
        self._lista_connessioni = DAO.get_connessioni(n_voli)
        #print(f"Connessioni: {len(self._lista_connessioni)}")

    def build_graph(self, n_voli):
        self._graph.clear()

        self._nodes = []
        self._edges = []
        self._id_map_ = {}
        #nodi
        self.load_states(n_voli)

        for stato in self._lista_stati:
            self._nodes.append(stato)
            self._id_map_[stato.id] = stato
        self._graph.add_nodes_from(self._nodes)

        #archi
        self.load_connessioni(n_voli)
        print(f"  -> [Model] Trovati {len(self._lista_connessioni)} archi totali nel DB.")

        for c in self._lista_connessioni:
            w = c.peso
            if (c.state1 in self._id_map_ and c.state2 in self._id_map_):
                a1 = self._id_map_[c.state1]
                a2 = self._id_map_[c.state2]
                self._graph.add_edge(a1, a2, weight=w)
                self._edges.append(c)

    def get_num_of_nodes(self):
        return self._graph.number_of_nodes()

    def get_num_of_edges(self):
        return self._graph.number_of_edges()

    def get_raggiungibili(self):
        pass




    #prova 1