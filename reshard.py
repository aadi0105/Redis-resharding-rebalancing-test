# Reshard 127.0.0.1:6379
import subprocess
result = subprocess.run(['redis-cli', '--cluster', 'reshard', '127.0.0.1:6382'], capture_output=True, text=True)

print(result.stdout)