# Rebalance the cluster
import subprocess
result = subprocess.run(['redis-cli', '--cluster', 'rebalance', '127.0.0.1:6379'], capture_output=True, text=True)

print(result.stdout)
