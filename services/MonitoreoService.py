
class MonitoreoService:

    def __init__(self):
        self.dispositivos = []

    def registrar_dispositivo(self, paciente, tipo, datos):
        nuevo_dispositivo = {
            'id': len(self.dispositivos) + 1,
            'paciente': paciente,
            'tipo': tipo,
            'datos': datos
        }
        self.dispositivos.append(nuevo_dispositivo)
        print(f'Dispositivo registrado: {nuevo_dispositivo}')

    def obtener_datos_dispositivo(self, id):
        dispositivo = next((d for d in self.dispositivos if d['id'] == id), None)
        if not dispositivo:
            print('Dispositivo no encontrado')
            return None

        print(f'Dispositivo obtenido: {dispositivo}')
        return dispositivo