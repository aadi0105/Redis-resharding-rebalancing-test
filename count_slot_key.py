from subprocess import getoutput
def count_slot_key(node, port):
    result = getoutput(f"redis-cli --cluster check {node}:{str(port)} | grep slaves")
    # result = subprocess.run(['redis-cli', '--cluster', 'check', f'{node}:{str(port)}'], capture_output=True, text=True)
    return result
