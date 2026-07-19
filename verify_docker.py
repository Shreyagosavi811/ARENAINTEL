import subprocess
import time
import urllib.request
import json

print("Building docker image...")
subprocess.run(["docker", "build", "-t", "arenaintel-backend", "."], cwd="backend", check=True)

print("Starting container...")
container = subprocess.Popen([
    "docker", "run", "--rm", "-p", "8001:8000",
    "-e", "PORT=8000",
    "-e", "CORS_ORIGINS=http://test-origin.com",
    "arenaintel-backend"
])

time.sleep(3) # Wait for container to start

try:
    print("Testing /health endpoint...")
    req = urllib.request.Request("http://localhost:8001/health")
    with urllib.request.urlopen(req) as response:
        print(f"Health Response: {response.read().decode()}")

    print("Testing /copilot/analyze endpoint...")
    data = json.dumps({"text": "Test emergency"}).encode("utf-8")
    req = urllib.request.Request("http://localhost:8001/api/v1/copilot/analyze", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as response:
        print(f"Copilot Response Code: {response.getcode()}")
        print("Copilot Response Success.")
        
    print("Testing CORS response header...")
    req = urllib.request.Request("http://localhost:8001/health", headers={"Origin": "http://test-origin.com"})
    with urllib.request.urlopen(req) as response:
        cors_header = response.getheader("Access-Control-Allow-Origin")
        print(f"CORS Header (expected http://test-origin.com): {cors_header}")
        assert cors_header == "http://test-origin.com", "CORS misconfigured"
        
except Exception as e:
    print(f"Error during verification: {e}")
finally:
    print("Killing container...")
    container.terminate()
