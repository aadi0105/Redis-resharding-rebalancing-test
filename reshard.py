from subprocess import getoutput

# Function to perform resharding
def reshard(node_to, port_to, node_from, port_from):
    cluster_to_id = getoutput(f'redis-cli -h {node_to} -p {(port_to)} CLUSTER NODES | grep myself | cut -d" " -f1')
    cluster_from_id = getoutput(f'redis-cli -h {node_from} -p {port_from} CLUSTER NODES | grep myself | cut -d" " -f1')
    result = getoutput(f"redis-cli --cluster reshard {node_to}:{str(port_to)} --cluster-from {cluster_from_id} --cluster-to {cluster_to_id} --cluster-slots 4096 --cluster-yes | grep Ready")
    return result

# Run the resharding function
# cluster from is the node id of the instance from where data is being migrated
#cluster to is the node id of the instance to which data is migrated


