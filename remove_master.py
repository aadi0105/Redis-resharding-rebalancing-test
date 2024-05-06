import subprocess
# Remove the 4th master
def remove_master(host_to_remove, port):
    result = subprocess.run(['redis-cli', '--cluster', 'del-node', f'{host_to_remove}:{port}'], capture_output=True, text=True)
    return result.stdout
