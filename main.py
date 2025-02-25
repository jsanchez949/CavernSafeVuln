import subprocess
import log_phpmalwarefinder
import csv_phpmalwarefinder
import log_security_advisories
import scriptCVEs
import csv_vul_sa


def main():
    print("\n--------------------------------------------------------")
    print("| Script Ciberseguridad - CavernSafe |")
    print("--------------------------------------------------------")

    print("\n---------Detalles a tener en cuenta para el script----------\n")
    print("* Tener las herramientas instaladas correctamente (en el script se comprobaran si existen actualizaciones)")
    print("* Agregar al path las direcciones de las herramientas para poder ejecutarlas desde cualquier directorio")
    print("* Controlar variables para obtener rutas, ficheros, etc")

    menuprincipal = int(input(
        "\n Menu Principal "
        "\n -------------- "
        "\n 1 - Ver actualizaciones equipo "
        "\n 2 - Actualizar equipo "
        "\n 3 - Ejecutar herramienta PHP Malware Finder "
        "\n 4 - Generar CSV PHP Malware Finder "
        "\n 5 - Ejecutar herramienta Security Advisories "
        "\n 6 - Generar CSV Security Advisories "
        "\n 7 - Ejecutar todas las herramientas "
        "\n 8 - Generar todos los CSV "
        "\n 9 - Ejecutar las herramientas y los CSV "
        "\n 0 - Salir \n"))

    while menuprincipal != 0:
        if menuprincipal == 1:
            subprocess.run(["sudo", "apt-get", "update"])
            print("\n Actualizaciones mostradas \n")
        elif menuprincipal == 2:
            subprocess.run(["sudo", "apt-get", "upgrade"])
            print("\n Equipo actualizado \n")
        elif menuprincipal == 3:
            log_phpmalwarefinder.ejecutar_log()
        elif menuprincipal == 4:
            csv_phpmalwarefinder.generar_csv()
        elif menuprincipal == 5:
            log_security_advisories.ejecutar_log()
            scriptCVEs.conversionCVE()
        elif menuprincipal == 6:
            csv_vul_sa.generar_csv()
        elif menuprincipal == 7:
            log_phpmalwarefinder.ejecutar_log()
            log_security_advisories.ejecutar_log()
            log_security_advisories.ejecutar_log()
            scriptCVEs.conversionCVE()
        elif menuprincipal == 8:
            csv_phpmalwarefinder.generar_csv()
            csv_vul_sa.generar_csv()
        elif menuprincipal == 9:
            log_phpmalwarefinder.ejecutar_log()
            csv_phpmalwarefinder.generar_csv()
            log_security_advisories.ejecutar_log()
            scriptCVEs.conversionCVE()
            csv_vul_sa.generar_csv()
        else:
            print("\nElija una opcion correcta para el menu")

        menuprincipal = int(input(
            "\n Menu Principal "
            "\n -------------- "
            "\n 1 - Ver actualizaciones equipo "
            "\n 2 - Actualizar equipo "
            "\n 3 - Ejecutar herramienta PHP Malware Finder "
            "\n 4 - Generar CSV PHP Malware Finder "
            "\n 5 - Ejecutar herramienta Security Advisories "
            "\n 6 - Generar CSV Security Advisories "
            "\n 7 - Ejecutar todas las herramientas "
            "\n 8 - Generar todos los CSV "
            "\n 9 - Ejecutar las herramientas y los CSV "
            "\n 0 - Salir \n"))


if __name__ == '__main__':
    main()
