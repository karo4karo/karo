#!/usr/bin/env python3
import subprocess

# Replace these with your Zabbix server IP, port, hostname, item key, and new severity
zabbix_server = '10.75.20.153'
zabbix_port = '10051'
host_name = '	snmp_trap_catcher'
item_key = 'snmptrap[]'
new_severity = '4'  # 0 - Not classified, 1 - Information, 2 - Warning, 3 - Average, 4 - High, 5 - Disaster

# Construct the zabbix_sender command
command = [
    'zabbix_sender',
    '-z', zabbix_server,
    '-p', zabbix_port,
    '-s', host_name,
    '-k', item_key,
    '-o', new_severity
]

try:
    # Execute the zabbix_sender command
    subprocess.run(command, check=True)
    print("Trigger severity updated to " + new_severity + ".")
except subprocess.CalledProcessError as e:
    print("Error: " + str(e))
