import psutil
import getpass
import logging
from datetime import datetime

# --- Logging Setup ---
logging.basicConfig(
    filename="script.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def safe_call(func, description):
    """Runs a function safely and logs errors."""
    try:
        value = func()
        logging.info(f"{description}: SUCCESS")
        return value
    except Exception as e:
        logging.error(f"{description}: ERROR - {e}")
        return "N/A"

# --- Collecting System Info ---

def get_cpu_info():
    return {
        "cores": psutil.cpu_count(),
        "usage": psutil.cpu_percent(interval=1)
          }

def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        "total": mem.total,
        "used": mem.used,
        "free": mem.available
    }

def get_disk_info():
    disk = psutil.disk_usage('/')
    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free
    }

def get_user():
    return getpass.getuser()

# --- Main Execution ---

def generate_report():
    cpu = safe_call(get_cpu_info, "CPU INFO")
    memory = safe_call(get_memory_info, "MEMORY INFO")
    disk = safe_call(get_disk_info, "DISK INFO")
    user = safe_call(get_user, "USER INFO")

    report = f"""
System Report - {datetime.now()}

CPU Cores: {cpu['cores']}
CPU Usage: {cpu['usage']}%

Total Memory: {memory['total']}
Used Memory: {memory['used']}
Free Memory: {memory['free']}

Total Disk: {disk['total']}
Used Disk: {disk['used']}
Free Disk: {disk['free']}

Logged-in User: {user}
"""

    with open("system_report.txt", "w") as f:
        f.write(report)

    logging.info("System report generated successfully")


if __name__ == "__main__":
    generate_report()
