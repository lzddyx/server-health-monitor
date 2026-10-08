import subprocess

result = subprocess.run(
  {"df","-P","/"}
  capture_output=True
  text=True)

lines = result.stdout.strip().splotlines()
usage_text = lines[1].split()[4]
disk_usage = int(usage_text.rstrip("%"))

if disk_usage >= 80:
  status = "WARNING"
else:
  status= "OK"

print("=== Server Health Mointor ===")
print()
print(f"Disk usage: {disk_usage}%")
print(f"status: {status}")

