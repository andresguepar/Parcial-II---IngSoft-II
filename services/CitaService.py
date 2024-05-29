

class CitaService:
    
    def __init__(self):
        self.citas = []

    def crear_cita(self, paciente, medico, fecha_hora):
        nueva_cita = {
            'id': len(self.citas) + 1,
            'paciente': paciente,
            'medico': medico,
            'fecha_hora': fecha_hora,
            'estado': 'reservada'
        }
        self.citas.append(nueva_cita)
        print(f'Cita creada: {nueva_cita}')

    def actualizar_cita(self,id, fecha_hora, estado):
        cita = next((c for c in self.citas if c['id'] == id), None)
        if not cita:
            print('Cita no encontrada')
            return

        cita['fecha_hora'] = fecha_hora
        cita['estado'] = estado
        print(f'Cita actualizada: {cita}')

    def obtener_citas(self, id_cita):
        citas = [c for c in self.citas if c['id_cita'] == id_cita]
        print(f'Mensajes obtenidos para paciente {id_cita}: {citas}')
        return citas

    def cancelar_cita(self, id):
        global citas
        cita = next((c for c in self.citas if c['id'] == id), None)
        if not cita:
            print('Cita no encontrada')
            return

        citas = [c for c in citas if c['id'] != id]
        print(f'Cita cancelada: {cita}')