#!/usr/bin/env python3

from pyzabbix import ZabbixAPI
from pyzabbix import ZabbixSender
import datetime

def connect_to_zabbix():
    try:
        z = ZabbixAPI("http://10.75.20.153/zabbix/")
        z.login(user='Admin', password='zabbix')
        return z
    except Exception as e:
        return None

def jei_none():
    now = datetime.datetime.now()
    nhour = now.hour
    nminute = now.minute
    return now.hour * now.minute

def send_highest_number():
    try:
        max_value = (max(highest_number))
        zbx = ZabbixSender(zabbix_server='10.75.20.153',zabbix_port=10051)
        zbx.send(host='oracle_agent_1', key='highest.number', value=max_value)
        return int(zbx)
    except Exception as e:
        return None

def main():
    zabbix_api = connect_to_zabbix()
    if zabbix_api:
        try:
            x_input = input("Enter a number: ")
            if not x_input:
                x = jei_none()
            else:
                x = int(x_input)

            count = 1
            global highest_number
            highest_number = []
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x + 1
                    highest_number.append(x)
                count += 1

            print(count)

            send_highest_number()
            
        except ValueError:
            print("Invalid input.")
        except EOFError:
            x = jei_none()
            count = 1
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x + 1
                count += 1
                
            print(count)
            
        # Logout from the Zabbix API
        try:
            zabbix_api.user.logout()
        except Exception:
            pass  # Ignore logout errors


if __name__ == "__main__":
    main()
