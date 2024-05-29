from services.CitaService import CitaService
from services.HistorialService import HistorialService 
from services.MonitoreoService import MonitoreoService 
from services.ComunicacionService import ComunicacionService 
from services.RecordatorioService import RecordatorioService 
from services.ReporteService import ReporteService 

def main():
    while True:
            print("======Clinica======")
            print("\nOptions:")
            print("1. Citas ")
            print("2. Historial Medico ")
            print("3. Monitoreo de Salud Remoto ")
            print("4. Recordatorios de Medicacion ")
            print("5. Comunicacion")
            print("6. Reportes ")
            print("7. Exit")

            
            choice = input("Select an option: ")

        
            if choice == '1':  
                gc = CitaService()

                cita = gc.crear_cita(
                    paciente ="Juan Perez",
                    medico ="Dra. Maria Lopez",
                    fecha_hora ="2024-05-27 10:00 AM"
                )
                
                while True:
                    
                        print("\nOptions:")
                        print("1. Agendar ")
                        print("2. Actualizar ")
                        print("3. Cancelar ")
                        print("4. Mostrar ")
                        print("5. Exit")

                        if choice == '1':  
                            cita = gc.crear_cita(
                            paciente = input("Nombre Paciente"),
                            medico = input("Nombre Medico"),
                            fecha_hora =  input("Fecha y Hora")
                            )
                            print("Cita agendada.")
                            
                        elif choice == '2':  
                            id_cita = input("Id Cita: ") 
                            fecha_hora = input("Fecha y Hora: ")
                            estado = input("Estado: ")

                            cita = gc.actualizar_cita(
                                id=id_cita,
                                fecha_hora=fecha_hora,
                                estado=estado
                            )

                            if cita:
                                print("Cita Actualizada.")
                            else:
                                print("No se pudo actualizar la cita. Por favor, verifica el ID.")

                        elif choice == '3':  
                            id = input("Id Cita: ")
                            gc.cancelar_cita(id)
                        
                        elif choice == '4':  
                            print("Citas:")
                            gc.obtener_citas()  
                        
                        elif choice == '5':  # Exit the program
                            print("Exiting...")
                            break
                
            elif choice == '2':  
                gh = HistorialService()

                historial = gh.crear_historial(
                paciente = "Edwin",
                detalles = "Consulta general",
                notas = "Notas del médico..."
                )

            elif choice == '3':  
                ms = MonitoreoService()

                dispositivo = ms.registrar_dispositivo(
                paciente = "Pepito Limon",
                tipo = "Monitor de presión arterial",
                datos={"presion_sistolica": 120, "presion_diastolica": 80}
                )

            elif choice == '4': 
                rec = RecordatorioService()

                recordatorio = rec.crear_recordatorio(
                paciente = "Yennefer",
                medicamento = "Ibuprofeno",
                dosis = "200mg",
                frecuencia = "Cada 8 horas"
                )

            elif choice == '5':
                com = ComunicacionService()

                mensaje = com.enviar_mensaje(
                paciente = "Dolores Abernathy",
                medico= "Maeve Millay",
                mensaje="Hola, necesito ayuda con mi medicamento.",
                tipo='chat'
                )

            elif choice == '6':
                rs = ReporteService()
                
                rs.generar_reporte_salud()

            elif choice == '7':  
                print("Exiting...")
                break
            else:
                print("Option not valid.")



    gh.obtener_historial(cita)

    com.obtener_mensajes(cita)
    
    rec.obtener_recordatorios(cita)

    rs.generar_reporte_salud(cita)
    
if __name__ == "__main__":
    main()
