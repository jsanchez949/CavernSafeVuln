import csv
import os
import re
import scriptCVEs


# Clonar repositorio https://github.com/FriendsOfPHP/security-advisories.git
# Comprobacion de si existe el fichero necesario para ejecutar la herramienta en local

def ejecutar_log():
    print ("-------- Inicio de la herramienta Security-Advisories ----------")

    # Si no existe, clonar el repositorio dentro de la carpeta Herramientas en el escritorio
    if not os.path.exists('/home/kali/Desktop/Herramientas/security-advisories/'):
        os.system(
            'git clone https://github.com/nbs-system/php-malware-finder.git /home/kali/Desktop/Herramientas/security-advisories/')
        os.system('chmod 755 -R /home/kali/Desktop/Herramientas/security-advisories/')
        if not os.path.exists('/home/kali/Desktop/Herramientas/security-advisories'):
            print("No se pudo clonar el repositorio.")
            exit()

    # Comprueba si existe el fichero local-php-security. Si existe se ejecuta la herramienta,
    # por el contrario, si no existe se descarga dicho fichero se renombra y se le dan permisos al archivo para que
    # pueda ejecutarse la herramienta

    if os.path.exists('local-php-security-checker.bin'):
        ejecucion_herramienta()
        print("\n //Proyecto escaneado correctamente...\\")
    else:
        print("No se encontro el archivo $advisories")
        print("Descargando fichero...")

        os.system(
            "wget https://github.com/fabpot/local-php-security-checker/releases/download/v2.0.5/local-php-security"
            "-checker_2.0.5_linux_386")
        os.system("mv local-php-security-checker_2.0.5_linux_386 local-php-security-checker.bin")
        os.system("chmod 755 local-php-security-checker.bin")

        ejecucion_herramienta()


def ejecucion_herramienta():
    advisories = './local-php-security-checker.bin'
    # Ejecuta el comando del sistema y obtiene la salida como un flujo de datos
    output = os.popen(advisories).read()
    # Crea un patron para buscar lineas que contengan el texto "resultado"
    pattern = re.compile('\*|package|---|==|Symfony')
    # Probar con * para filtrar solamente una vez las CVE
    # Abre el archivo en modo escritura
    with open('resultados/log_sec_advisories.csv', 'w') as csvfile:
        # Crea un objeto escritor
        writer = csv.writer(csvfile)

        # Itera sobre las lineas de la salida del comando
        for line in output.splitlines():
            # Si la linea coincide con el patron, escribela en el archivo CSV
            if pattern.search(line):
                cleaned = re.sub("\[\w+m", "", line)
                cleaned_row = cleaned.replace("", "")
                writer.writerow([cleaned_row])
                print(cleaned_row)
