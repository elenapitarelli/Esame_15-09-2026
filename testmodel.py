from model.model import Model

model = Model()
n_voli = 10
model.load_states(n_voli)
model.build_graph(n_voli)
