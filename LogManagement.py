import os
import sys
import json
from datetime import datetime

def check_write_permissions(path):
    try:
        test_file = os.path.join(path, 'permission_test.tmp')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        return True
    except (OSError, IOError):
        return False

def log_system_event(message):
    log_path = "logs/system_security_log.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def load_settings():
    settings_path = "config/settings.json"
    try:
        with open(settings_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
def setup_project_environment():
    project_name = "Kira_Management_System"
    folders = ["logs", "data", "config"]
    files = {
        "logs/system_security_log.txt": "LOG FILE INITIALIZED\n",
        "config/settings.json": '{"version": "1.0", "status": "active"}'
    }

    base_path = os.getcwd()

    if not check_write_permissions(base_path):
        return f"ERRORE: Permessi negati in {base_path}"

    if not os.path.exists(project_name):
        os.makedirs(project_name)

    os.chdir(project_name)

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    for file_path, initial_content in files.items():
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(initial_content)

    return os.getcwd()

if __name__ == "__main__":
    path = setup_project_environment()

    if "ERRORE" in path:
        print(path)
        sys.exit(1)

    print(f"Setup Complete. Project Path: {path}")

    config = load_settings()
    if config:
        print(f"Sistema {config['status']} - Versione {config['version']}")

    log_system_event("Sessione avviata correttamente dal Guru.")
    print("Evento registrato nel file di log.")