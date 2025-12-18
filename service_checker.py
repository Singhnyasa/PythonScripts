import subprocess

service = 'nginx'
result = subprocess.run(["systemctl","is-active",service],
                        capture_output=True,text=True)

if result.stdout.strip() == 'active':
     print(f"{service} is running")
else:
     print(f"{service} is NOT running")     