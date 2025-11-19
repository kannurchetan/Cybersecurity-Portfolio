# Snort Setup Steps

1. Install Snort on Ubuntu  
   sudo apt update  
   sudo apt install snort -y

2. Verify installation  
   snort -V

3. Add custom rules by placing custom-rules.rules in /etc/snort/rules/.

4. Update snort.conf to include the custom rule file.

5. Run Snort in IDS mode  
   sudo snort -A fast -c /etc/snort/snort.conf -i eth0

6. Test using Kali:  
   - nmap -sS <target-ip>  
   - ping -c 10 <target-ip>  
   - hydra -l admin -P passwords.txt ftp://<target-ip>

7. Alerts will appear in snort_alerts.txt
