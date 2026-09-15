import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_creaGrafo(self, e):
        try:
            n_voli =int(self._view.txtNumVoliMinimo.value)

        except(ValueError, TypeError):
            self._view.show_alert("Inserire un valore valido")
            return

        if n_voli < 0:
            self._view.show_alert("Inserire un valore positivo")
            return


        self._model.build_graph(n_voli)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(
            f"Grafo creato: Nodi: {self._model.get_num_nodes()} - Archi: {self._model.get_num_edges()}"))
        self._view.txt_result.update()
        self._view.update_page()

    def populate_dropdown(self):
        for node in self._model.get_nodes():
            self._view._ddStatoPartenza.options.append(ft.dropdown.Option(text =node.name, key = node.state))

    def handler_read_stati(self,e):
        stato_iniziale = self._view.txtStato.value




    def handle_statiRaggiungibili(self, e):
       pass

