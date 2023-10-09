#!/usr/bin/env python3

from pyzabbix import ZabbixAPI
import datetime

def connect_to_zabbix():
    try:
        z = ZabbixAPI("http://10.75.20.28/zabbix/")
        z.login(api_token='bcf7a642e2dc19f13c502b1447588b570ff47d67b2d301d98377e7d983aaf193')
        return z
    except Exception as e:
        return None

def jei_none():
    now = datetime.datetime.now()
    nhour = now.hour
    nminute = now.minute
    return now.hour * now.minute

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

            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x + 1
                count += 1

            print(count)

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