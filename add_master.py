import subprocess

# Add 127.0.0.1:6382 to the cluste
def add_master(master, master_port, host_to_add, host_to_add_port):
    result = subprocess.run(['redis-cli', '--cluster', 'add-node', f'{host_to_add}:{str(host_to_add_port)}', f'{master}:{str(master_port)}'], capture_output=True, text=True)
    return result.stdout
