import hashlib
import os
import binascii
import time


def generate_secure_hash(password):
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return binascii.hexlify(salt + dk).decode()


def get_security_config():
    return {
        "max_attempts": 3,
        "lockout_time": 10,
        "authorized_users": {
            "Kira": "L2204!"
        }
    }


failed_attempts = {}


def secure_login(username, password_input):
    config = get_security_config()
    current_time = time.time()

    if username in failed_attempts:
        attempts, last_time = failed_attempts[username]
        if attempts >= config["max_attempts"]:
            if current_time - last_time < config["lockout_time"]:
                wait_time = int(config["lockout_time"] - (current_time - last_time))
                return f"Security Lock: Try again in {wait_time}s."
            else:
                failed_attempts[username] = [0, 0]

    users = config["authorized_users"]

    if username in users and users[username] == password_input:
        failed_attempts[username] = [0, 0]
        secure_hash = generate_secure_hash(password_input)
        return f"Access Granted: Welcome {username}. Session Hash: {secure_hash[:16]}..."
    else:
        attempts = failed_attempts.get(username, [0, 0])[0] + 1
        failed_attempts[username] = [attempts, current_time]
        return f"Access Denied: Attempt {attempts} of {config['max_attempts']}."


if __name__ == "__main__":
    print("--- LOGIN SYSTEM (Active Memory Mode) ---")
    while True:
        user_in = input("\nUsername: ")
        pass_in = input("Password: ")

        result = secure_login(user_in, pass_in)
        print(result)

        if "Welcome" in result:
            break