import subprocess
# Remove the 4th master
def remove_master(node, port):
    result = subprocess.run(['redis-cli', '--cluster', 'del-node', f'{node}:{str(port)}'], capture_output=True, text=True)
    return result.stdout
