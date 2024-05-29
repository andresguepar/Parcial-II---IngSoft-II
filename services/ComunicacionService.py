
class ComunicacionService:

    def __init__(self):
        self.mensajes = []

    def enviar_mensaje(self,paciente, medico, mensaje, tipo):
        nuevo_mensaje = {
            'id': len(self.mensajes) + 1,
            'paciente': paciente,
            'medico': medico,
            'mensaje': mensaje,
            'tipo': tipo  # chat, videoconferencia, notificación
        }
        self.mensajes.append(nuevo_mensaje)
        print(f'Mensaje enviado: {nuevo_mensaje}')

    def obtener_mensajes(self,paciente):
        mensajes = [m for m in self.mensajes if m['paciente'] == paciente]
        print(f'Mensajes obtenidos para paciente {paciente}: {mensajes}')
        return mensajes