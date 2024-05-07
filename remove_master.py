from subprocess import getoutput
# Remove the 4th master
def remove_master(node, port):
    node_id = getoutput(f'redis-cli -h {node} -p {port} CLUSTER NODES | grep myself | cut -d" " -f1')
    result = getoutput(f"redis-cli --cluster forget {node_id}" )
    return result
