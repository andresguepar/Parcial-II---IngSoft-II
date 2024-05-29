
class HistorialService:

    def __init__(self):
        self.historial = []

    def crear_historial(self, paciente, detalles, notas):
        nuevo_historial = {
            'id': len(self.historial) + 1,
            'paciente': paciente,
            'detalles': detalles,
            'notas': notas
        }
        self.historial.append(nuevo_historial)
        print(f'Historial creado: {nuevo_historial}')

    def obtener_historial(self, paciente):
        historial = next((h for h in self.historial if h['paciente'] == paciente), None)
        if not historial:
            print('Historial no encontrado')
            return None

        print(f'Historial obtenido: {historial}')
        return historial