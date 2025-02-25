# ✨ Script Ciberseguridad - CavernSafeVuln ✨

&#x20;&#x20;

## 🔒 ¿Qué es CavernSafeVuln?

CavernSafeVuln es un conjunto de herramientas de **ciberseguridad** diseñado para **detectar vulnerabilidades y malware en archivos PHP** dentro de un sistema Linux.

El usuario puede seleccionar distintas opciones del menú para ejecutar herramientas de seguridad y generar reportes detallados en formato **CSV**.

---

## ⚙️ Características principales

- **Análisis de seguridad automático** en sistemas Linux.
- **Detección de malware** en archivos PHP.
- **Generación de reportes** detallados en archivos CSV.
- **Fácil instalación** y uso con menú interactivo.

---

## 🛠️ Herramientas incluidas

| # | Herramienta                     | Descripción                                           |
| - | ------------------------------- | ----------------------------------------------------- |
| 1 | Ver actualizaciones             | Muestra las actualizaciones disponibles del sistema.  |
| 2 | Actualizar sistema              | Aplica las actualizaciones del sistema.               |
| 3 | PHP Malware Finder              | Busca malware en archivos PHP.                        |
| 4 | Generar CSV PHP Malware Finder  | Guarda los resultados del análisis en un archivo CSV. |
| 5 | Security Advisories             | Busca vulnerabilidades de seguridad en el sistema.    |
| 6 | Generar CSV Security Advisories | Guarda las vulnerabilidades detectadas en CSV.        |
| 7 | Ejecutar todas las herramientas | Corre todas las herramientas de análisis.             |
| 8 | Generar todos los CSV           | Guarda todos los resultados en CSV.                   |
| 9 | Ejecutar herramientas + CSV     | Combina análisis y generación de reportes.            |

---

## 📝 Requisitos

- **Sistema operativo:** Kali Linux (o distribución similar)
- **Lenguaje:** Python 3.9+
- **Herramientas necesarias:**
  - `php-malware-finder`
  - `security-advisories`
  - `yara`
- **Librerías de Python:**
  - `os`, `re`, `csv`, `pandas`

---

## 🖥️ Instalación

1. Asegúrate de tener **Python 3.9+** instalado.
2. Instala **Yara** con:
   ```bash
   sudo apt-get update
   sudo apt-get install yara
   ```
3. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/CavernSafeVuln.git
   cd CavernSafeVuln
   ```
4. Crea una carpeta para almacenar los resultados:
   ```bash
   mkdir resultados
   ```
5. Ejecuta el script principal:
   ```bash
   python3 main.py
   ```

---

## 🔮 Ejemplo de Resultados

Los resultados se almacenan en la carpeta `resultados` y contienen:

**Ejemplo CSV de PHP Malware Finder:**

| Tipo de Vulnerabilidad | Ocurrencias |
| ---------------------- | ----------- |
| nonPrintableChars      | 9           |
| obfuscatedPhp          | 46          |
| dodgyPhp               | 20          |
| dangerousPhp           | 7           |
| dodgyStrings           | 12          |

**Ejemplo CSV de Vulnerabilidades:**

| CVE            | Nivel de Riesgo |
| -------------- | --------------- |
| CVE-2022-25275 | Critical        |
| CVE-2022-25277 | Critical        |
| CVE-2022-29248 | High            |

---

## 🚀 Contribuciones y Contacto

Si quieres mejorar este proyecto o reportar errores:

- ✨ **Fork** y **pull request** en GitHub
- 📧 **Email:** [jesus\.s\.s949@gmail.com](mailto\:jesus.s.s949@gmail.com)

---

## © Licencia

Este proyecto está bajo la **Licencia MIT** - eres libre de usarlo, modificarlo y compartirlo.

---

💡 **¡Proteger tu sistema nunca fue tan fácil!** 🔒🌐

