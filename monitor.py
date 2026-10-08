import subprocess

result = subprocess.run(
    ["df", "-P", "/"],
    capture_output=True,
    text=True
)

lines = result.stdout.strip().splitlines()
usage_text = lines[1].split()[4]
disk_usage = int(usage_text.rstrip("%"))

if disk_usage >= 80:
    status = "WARNING"
else:
    status = "OK"

service_result = subprocess.run(
    ["systemctl", "is-active", "ai-demo.service"],
    capture_output=True,
    text=True
)

service_status = service_result.stdout.strip()

if service_status == "active":
    service_display = "RUNNING"
else:
    service_display = "NOT RUNNING"

print("=== Server Health Monitor ===")
print()
print("Disk")
print(f"Usage: {disk_usage}%")
print(f"Status: {status}")
print()
print("Service")
print(f"ai-demo: {service_display}")
