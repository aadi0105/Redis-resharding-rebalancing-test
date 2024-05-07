from subprocess import getoutput 

def create_cluster(nodes):
    result = getoutput(f"redis-cli --cluster create {nodes['node1']['ip']}:{nodes['node1']['port']} {nodes['node2']['ip']}:{nodes['node2']['port']} {nodes['node3']['ip']}:{nodes['node3']['port']} --cluster-replicas 0 --cluster-yes| grep OK")
    return result

