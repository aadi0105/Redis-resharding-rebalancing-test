# Add 127.0.0.1:6382 to the cluster
import subprocess
result = subprocess.run(['redis-cli', '--cluster', 'add-node', '127.0.0.1:6382', '127.0.0.1:6379'], capture_output=True, text=True)

print(result.stdout)
