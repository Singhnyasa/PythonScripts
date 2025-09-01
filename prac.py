import requests
import time
import json

# List of services and their health check endpoints
services = {
    "auth-service": "http://auth.example.com/health",
    "user-service": "http://user.example.com/health",
    "payment-service": "http://payment.example.com/health"
}

# Timeout for each request (in seconds)
TIMEOUT = 5

# Function to check the health of a service
def check_service_health(name, url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code == 200:
            print(f"[OK] {name}")
            return {"service": name, "status": "healthy", "code": response.status_code}
        else:
            print(f"[DOWN] {name} - HTTP {response.status_code}")
            return {"service": name, "status": "unhealthy", "code": response.status_code}
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {name} - Exception: {str(e)}")
        return {"service": name, "status": "unreachable", "error": str(e)}

# Run health checks
def run_health_checks():
    results = []
    for name, url in services.items():
        result = check_service_health(name, url)
        results.append(result)
    return results

# Save results to a JSON log file
def save_log(results):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"health_check_log_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
    print(f"\nHealth check results saved to {filename}")

if __name__ == "__main__":
    results = run_health_checks()
    save_log(results)

