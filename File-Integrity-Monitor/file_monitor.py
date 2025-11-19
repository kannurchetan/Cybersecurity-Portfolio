import hashlib
import os
import time
import json

DB_FILE = "hashes.db"
WATCH_FOLDER = "test_files"
LOG_FILE = "integrity_log.txt"

# Generate SHA-256 hash
def hash_file(path):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            sha.update(chunk)
    return sha.hexdigest()

# Load old hashes
def load_hashes():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

# Save new hashes
def save_hashes(hashes):
    with open(DB_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

# Log events
def log_event(msg):
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")
    print(msg)

def monitor():
    old_hashes = load_hashes()
    new_hashes = {}

    for file in os.listdir(WATCH_FOLDER):
        path = os.path.join(WATCH_FOLDER, file)
        
        if os.path.isfile(path):
            h = hash_file(path)
            new_hashes[file] = h

            # Detect new files
            if file not in old_hashes:
                log_event(f"[NEW FILE] {file} added.")
            
            # Detect modified files
            elif old_hashes[file] != h:
                log_event(f"[MODIFIED] {file} changed!")

    # Detect deleted files
    for f in old_hashes:
        if f not in new_hashes:
            log_event(f"[DELETED] {f} removed.")

    save_hashes(new_hashes)


if __name__ == "__main__":
    print("Monitoring folder for integrity changes...")
    monitor()
