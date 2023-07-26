import os
import shutil
import string

def abrir_explorador():
    archivo = input("Arrastre un archivo aquí y presione Enter: ")
    nombre_archivo = os.path.basename(archivo).translate(str.maketrans("", "", string.punctuation + string.whitespace))
    copia_archivo = "copia_" + nombre_archivo
    ruta_absoluta_archivo = os.path.abspath(archivo)
    copia_ruta_absoluta_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), copia_archivo)
    shutil.copy2(ruta_absoluta_archivo, copia_ruta_absoluta_archivo)
    os.startfile(ruta_absoluta_archivo)
    print("Archivo copiado y ventana del explorador abierta.\n")

def limpiar_archivo():
    archivo = input("Ingrese el nombre del archivo que desea limpiar: ")
    try:
        with open(archivo, 'r') as f:
            lines = f.readlines()
        with open(archivo, 'w') as f:
            f.writelines(lines[1:])
        print("Archivo limpiado correctamente.\n")
    except FileNotFoundError:
        print("Archivo no encontrado.\n")

def generar():
    abrir_explorador()
    limpiar_archivo()

while True:
    print("Opciones:")
    print("1. Abrir ventana del explorador y copiar archivo")
    print("2. Limpiar archivo")
    print("3. Generar (Abrir ventana del explorador y copiar archivo, luego limpiar archivo)")
    print("0. Salir")
    opcion = int(input("Ingrese el número de la opción deseada: "))
    
    if opcion == 1:
        abrir_explorador()
    elif opcion == 2:
        limpiar_archivo()
    elif opcion == 3:
        generar()
    elif opcion == 0:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.\n")
