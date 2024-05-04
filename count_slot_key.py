import subprocess

# Run the command to count keys in the cluster
result = subprocess.run(['redis-cli', '--cluster', 'check', '127.0.0.1:6379'], capture_output=True, text=True)

# Display the results
print(result.stdout)
