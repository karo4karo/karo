import logging
from pyzabbix import ZabbixAPI
import datetime

# Configure logging to write errors to a log file
logging.basicConfig(filename='zabbix_validation_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a function to connect to the Zabbix API
def connect_to_zabbix():
    try:
        z = ZabbixAPI("http://10.75.20.153/zabbix/")  # Replace with your Zabbix server URL
        z.login(user='Admin', password='zabbix')  # or replace with your API token
        print("Connected to Zabbix API Version %s" % z.api_version())
        return z
    except Exception as e:
        logging.error(f"Failed to connect to Zabbix API: {str(e)}")
        return None

# Create a function to perform validation
def validate_input(x):
    try:
        # Your validation logic here
        if x < 0:
            raise ValueError("Input must be non-negative.")
        return True
    except Exception as e:
        logging.error(f"Validation error: {str(e)}")
        return False

# Get user input or calculate default value
user_input = input("Enter a number: ")
if user_input.strip() == "":
    now = datetime.datetime.now()
    x = now.hour * now.minute
else:
    try:
        x = int(user_input)
    except ValueError:
        x = None

# Check if the input is valid
if x is not None and validate_input(x):
    # Collatz conjecture loop
    count = 1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        count += 1
    # Print the result
    print("Count of iterations:", count)
else:
    print("Input is not valid.")

# Logout from the Zabbix API
try:
    z = connect_to_zabbix()
    if z:
        z.user.logout()
except Exception as e:
    logging.error(f"Failed to log out from Zabbix API: {str(e)}")

# Close the log file when done
logging.shutdown()