import subprocess

# Add 127.0.0.1:6382 to the cluste
def add_master(node1, port1, node2, port2):
    result = subprocess.getoutput(f"redis-cli --cluster add-node {node2}:{str(port2)} {node1}:{str(port1)}")
    # result = subprocess.run(['redis-cli', '--cluster', 'add-node', f'{node2}:{str(port2)}', f'{node1}:{str(port1)}'], capture_output=True, text=True)
    for line in result.split("\n"):
        if "added" in line:
            return line
        
    return f"ERROR >>> {result}"
