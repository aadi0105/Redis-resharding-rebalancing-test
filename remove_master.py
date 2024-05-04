# Remove the 4th master
result = subprocess.run(['redis-cli', '--cluster', 'del-node', '127.0.0.1:6382'], capture_output=True, text=True)

print(result.stdout)
