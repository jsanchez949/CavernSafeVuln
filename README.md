# ✨ Cybersecurity Script - CavernSafeVuln ✨

## 🔒 What is CavernSafeVuln?

CavernSafeVuln is a set of **cybersecurity tools** designed to **detect vulnerabilities and malware in PHP files** within a Linux system.

The user can select different menu options to execute security tools and generate detailed reports in **CSV** format.

---

## ⚙️ Main Features

- **Automated security analysis** for Linux systems.
- **Malware detection** in PHP files.
- **Detailed report generation** in CSV files.
- **Easy installation** and use with an interactive menu.

---

## 🛠️ Included Tools

| # | Tool                         | Description                                             |
| - | ---------------------------- | ------------------------------------------------------- |
| 1 | Check for updates            | Displays available system updates.                      |
| 2 | Update system                | Applies system updates.                                |
| 3 | PHP Malware Finder           | Scans PHP files for malware.                           |
| 4 | Generate CSV PHP Malware Finder | Saves scan results in a CSV file.                      |
| 5 | Security Advisories          | Checks for security vulnerabilities in the system.     |
| 6 | Generate CSV Security Advisories | Saves detected vulnerabilities in a CSV file.          |
| 7 | Run all tools                | Executes all analysis tools.                           |
| 8 | Generate all CSVs            | Saves all results in CSV format.                       |
| 9 | Run tools + CSV              | Combines analysis and report generation.               |

---

## 📝 Requirements

- **Operating System:** Kali Linux (or similar distribution)
- **Language:** Python 3.9+
- **Required Tools:**
  - `php-malware-finder`
  - `security-advisories`
  - `yara`
- **Python Libraries:**
  - `os`, `re`, `csv`, `pandas`

---

## 🖥️ Installation

1. Ensure you have **Python 3.9+** installed.
2. Install **Yara** with:
   ```bash
   sudo apt-get update
   sudo apt-get install yara
   ```
3. Clone this repository:
   ```bash
   git clone https://github.com/your_username/CavernSafeVuln.git
   cd CavernSafeVuln
   ```
4. Create a folder to store results:
   ```bash
   mkdir results
   ```
5. Run the main script:
   ```bash
   python3 main.py
   ```

---

## 🔮 Example Results

Results are stored in the `results` folder and include:

**Example CSV from PHP Malware Finder:**

| Vulnerability Type  | Occurrences |
| ------------------- | ----------- |
| nonPrintableChars   | 9           |
| obfuscatedPhp      | 46          |
| dodgyPhp          | 20          |
| dangerousPhp      | 7           |
| dodgyStrings      | 12          |

**Example CSV of Vulnerabilities:**

| CVE            | Risk Level |
| -------------- | ---------- |
| CVE-2022-25275 | Critical   |
| CVE-2022-25277 | Critical   |
| CVE-2022-29248 | High       |

---

## 🚀 Contributions & Contact

If you want to improve this project or report issues:

- ✨ **Fork** and **pull request** on GitHub
- 💎 **Email:** [jesus.s.s949@gmail.com](mailto:jesus.s.s949@gmail.com)

---

## © Licence

This project is under the **MIT Licence** – you are free to use, modify, and share it.

---

💡 **Protecting your system has never been easier!** 🔒🌐

