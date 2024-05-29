
class RecordatorioService:

    def __init__(self):
        self.recordatorios = []

    def crear_recordatorio(self,paciente, medicamento, dosis, frecuencia):
        nuevo_recordatorio = {
            'id': len(self.recordatorios) + 1,
            'paciente': paciente,
            'medicamento': medicamento,
            'dosis': dosis,
            'frecuencia': frecuencia
        }
        self.recordatorios.append(nuevo_recordatorio)
        print(f'Recordatorio creado: {nuevo_recordatorio}')

    def obtener_recordatorios(self, paciente):
        recordatorios = [r for r in self.recordatorios if r['paciente'] == paciente]
        print(f'Recordatorios obtenidos para paciente {paciente}: {recordatorios}')
        return recordatorios    