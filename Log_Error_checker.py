log_file = "/var/log/syslog"

with open(log_file, "r") as file:
    errors = [line for line in file if "error" in line.lower()]

print(f"Found {len(errors)} error lines")
