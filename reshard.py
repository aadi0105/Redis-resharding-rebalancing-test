import subprocess

# Function to perform resharding
def reshard(node_to, port_to, node_from, port_from):
    cluster_to_id = subprocess.getoutput(f'redis-cli -h {node_to} -p {(port_to)} CLUSTER NODES | grep myself | cut -d" " -f1')
    cluster_from_id = subprocess.getoutput(f'redis-cli -h {node_from} -p {port_from} CLUSTER NODES | grep myself | cut -d" " -f1')
    result = subprocess.run(['redis-cli', '--cluster', 'reshard', f'{node_to}:{str(port_to)}',
                             '--cluster-from', f'{cluster_from_id}',
                             '--cluster-to', f'{cluster_to_id}',
                             '--cluster-slots', '4096', '--cluster-yes'],
                            capture_output=True, text=True)
    return result.stdout

# Run the resharding function
# cluster from is the node id of the instance from where data is being migrated
#cluster to is the node id of the instance to which data is migrated


