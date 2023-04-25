import PySimpleGUI as sg
import os

# crear el diseño de la interfaz gráfica
layout = [
    [sg.Text("Selecciona una carpeta:")],
    [sg.Input(key="-FOLDER-"), sg.FolderBrowse()],
    [sg.Text("Escribe el año inicial:")],
    [sg.Input(key="-START-")],
    [sg.Text("Escribe el año final:")],
    [sg.Input(key="-END-")],
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

