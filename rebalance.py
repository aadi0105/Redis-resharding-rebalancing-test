# Rebalance the cluster
import subprocess
def rebalance_cluster(node, port):
    result = subprocess.run(['redis-cli', '--cluster', 'rebalance', f'{node}:{str(port)}', '--cluster-use-empty-masters'], capture_output=True, text=True)
    return result.stdout


