import json

# Open the log file
with open('security_logs.json', 'r') as log_file:
    # Load the JSON data
    logs = json.load(log_file)

# Loop through the logs and print each one
for log in logs:
    print(f'Timestamp: {log["timestamp"]}')
    print(f'Source IP: {log["source_ip"]}')
    print(f'Destination IP: {log["destination_ip"]}')
    print(f'Action: {log["action"]}')
    print(f'Details: {log["details"]}')
    print('-' * 20)
