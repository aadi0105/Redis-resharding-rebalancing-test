# Rebalance the cluster
import subprocess
def rebalance_cluster(new_host, port):
    result = subprocess.run(['redis-cli', '--cluster', 'rebalance', f'{new_host}:{port}', '--cluster-use-empty-masters'], capture_output=True, text=True)
    return result.stdout
