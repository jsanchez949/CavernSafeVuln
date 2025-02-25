import csv
import re


def get_cve_column(cve):
    with open('/home/kali/Desktop/scripts-herramientas-ciberseguridad/cve_tabla.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0].find(cve) != -1:
                return row[1]
    return None


def conversionCVE():
    cve_list = []
    criticidad = []
    with open('resultados/log_sec_advisories.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            start = row[0].find("[")
            end = row[0].find("]")
            cve = row[0][start + 1:end]
            if cve.startswith("CVE"):
                cve_list.append(cve)
                cve_column = get_cve_column(cve)
                if cve_column:
                    criticidad.append(cve_column)
                else:
                    criticidad.append("No se encuentra el CVE")

    with open('resultados/cve_criticidad_sa.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([])
        csvwriter.writerow(['CVE', 'Criticidad'])
        for i in range(len(cve_list)):
            csvwriter.writerow([cve_list[i], criticidad[i]])
            print([cve_list[i], criticidad[i]])
