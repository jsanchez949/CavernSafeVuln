import csv
from collections import defaultdict


def generar_csv():
    # Abrir el archivo csv
    with open('resultados/cve_criticidad_sa.csv', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        # Crear un diccionario para contar las repeticiones
        count = defaultdict(int)
        for row in reader:
            count[row[1]] += 1

    # Crear un diccionario para asignar valores numericos a cada valor de la primera columna
    order = {'None': 1, 'Low': 2, 'Medium': 3, 'High': 4, 'Critical': 5}
    # Crear una lista con los resultados ordenados
    result = sorted(count.items(), key=lambda x: order.get(x[0], 6))

    # Crear un archivo csv con los resultados ordenados
    with open('resultados/csv_vuln_sa.csv', mode='w') as archivo_csv:
        fieldnames = ['Riesgos', 'N veces']
        writer = csv.DictWriter(archivo_csv, fieldnames=fieldnames)
        writer.writeheader()
        print("")
        print("Tipo de riesgo	N veces")
        for key, value in result:
            writer.writerow({'Riesgos': key, 'N veces': value})
            print(key, value)
