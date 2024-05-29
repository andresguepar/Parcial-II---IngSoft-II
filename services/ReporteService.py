
import random


class ReporteService:

    def generar_reporte_salud(paciente):
        paciente = "Ben Martins"
        reporte = {
            'paciente': paciente,
            'presion_arterial': f'{random.randint(100, 150)}/{random.randint(60, 90)} mmHg',
            'frecuencia_cardiaca': f'{random.randint(60, 100)} bpm',
            'nivel_glucosa': f'{random.randint(70, 140)} mg/dL',
            'colesterol': f'{random.randint(120, 200)} mg/dL',
            'trigliceridos': f'{random.randint(50, 150)} mg/dL',
            'otros_datos': '...'
        }
        print(f'Reporte de salud generado para paciente {paciente}: {reporte}')
        return reporte