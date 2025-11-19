# File Integrity Monitoring Tool

This tool monitors files inside the `test_files/` directory and detects:

- New files added  
- Files modified  
- Files deleted  

It uses SHA-256 hashing and logs all events in `integrity_log.txt`.

## How to use:

1. Place the files you want to monitor inside the **test_files** folder.
2. Run the script:

