import subprocess
def count_slots_key(master_host, port):
    result = subprocess.run(['redis-cli', '--cluster', 'check', f'{master_host}:{str(port)}'], capture_output=True, text=True)
    return result.stdout
