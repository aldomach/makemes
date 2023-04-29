import PySimpleGUI as sg
import os
import datetime

# obtener el año actual
current_year = datetime.datetime.now().year

# crear el diseño de la interfaz gráfica
layout = [
    [sg.Text("Selecciona una carpeta:")],
    [sg.Input(key="-FOLDER-", default_text="."), sg.FolderBrowse()],
    [sg.Text("Escribe el año inicial:")],
    [sg.Input(key="-START-", default_text=current_year)],
    [sg.Text("Escribe el año final:")],
    [sg.Input(key="-END-", default_text=current_year)],
    [sg.Text("Elige el separador:")],
    [sg.Combo(["_", "-", ",", " ", "."], key="-SEPARATOR-", default_value="-")],
    [sg.Text("Elige el formato:")],
    [sg.Combo(["Mayúsculas", "Minúsculas", "Primera mayúscula"], key="-FORMAT-", default_value="Primera mayúscula")],
    [sg.Checkbox("Incluir año al nombre de la carpeta", key="-INCLUDE-YEAR-", default=True)],
    [sg.Button("Crear"), sg.Button("Salir")]
]

# crear la ventana
window = sg.Window("Creador de carpetas", layout)

# crear el bucle de eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Salir":
        # salir del programa
        break
    elif event == "Crear":
        # obtener los valores de la interfaz
        folder = values["-FOLDER-"]
        start = values["-START-"]
        end = values["-END-"]
        separator = values["-SEPARATOR-"]
        format = values["-FORMAT-"]
        include_year = values["-INCLUDE-YEAR-"]
        if folder and start and end:
            # validar que los años sean enteros y que el inicial sea menor o igual que el final
            try:
                start = int(start)
                end = int(end)
                if start <= end:
                    # crear las carpetas según los años y los meses
                    meses = ["01 enero", "02 febrero", "03 marzo", "04 abril", "05 mayo", "06 junio", "07 julio", "08 agosto", "09 septiembre", "10 octubre", "11 noviembre", "12 diciembre"]
                    for año in range(start, end + 1):
                        for mes in meses:
                            if separator:
                                # reemplazar los espacios por el separador
                                mes = mes.replace(" ", separator)
                            if format == "Mayúsculas":
                                # convertir el mes a mayúsculas
                                mes = mes.upper()
                            elif format == "Minúsculas":
                                # convertir el mes a minúsculas
                                mes = mes.lower()
                            elif format == "Primera mayúscula":
                                # convertir la primera letra del mes a mayúscula
                                mes = mes.capitalize()
                            if include_year:
                                # agregar el año al nombre del mes con el separador
                                mes = f"{año}{separator}{mes}"
                            os.makedirs(os.path.join(folder, str(año), mes), exist_ok=True)
                    # mostrar un mensaje de éxito
                    sg.popup("Se han creado las carpetas correctamente.")
                else:
                    # mostrar un mensaje de error
                    sg.popup("El año inicial debe ser menor o igual que el año final.")
            except ValueError:
                # mostrar un mensaje de error
                sg.popup("Los años deben ser números enteros.")
        else:
            # mostrar un mensaje de error
            sg.popup("Por favor, rellena todos los campos.")

# cerrar la ventana
window.close()

