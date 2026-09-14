import subprocess

service = "jenkins"

result = subprocess.run(
    ["systemctl", "is-active", service],
    capture_output=True,
    text=True
)

if result.stdout.strip() == "active":
    print(f"{service} is RUNNING")
else:
    print(f"{service} is NOT RUNNING")