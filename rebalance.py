# Rebalance the cluster
from subprocess import getoutput
def rebalance_cluster(node, port):
    result = getoutput(f"redis-cli --cluster rebalance {node}:{str(port)} --cluster-use-empty-masters")
    for line in result.split("\n"):
        if "Rebalancing" in line:
            return line   
    return f"ERROR >>> {result}"


