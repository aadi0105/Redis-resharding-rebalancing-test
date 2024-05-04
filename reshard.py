 import subprocess

# Function to perform resharding
def reshard():
    result = subprocess.run(['redis-cli', '--cluster', 'reshard', '127.0.0.1:6382',
                             '--cluster-from', '6ac62aa8dbb80f982ab1b0fa0623fc54d2bbd77b',
                             '--cluster-to', '9026f2af5a683123abfdd7494da2c73a61803dd3',
                             '--cluster-slots', '3276', '--cluster-yes'],
                            capture_output=True, text=True)
    print(result.stdout)

# Run the resharding function
reshard()
# cluster from is the node id of the instance from where data is being migrated
#cluster to is the node id of the instance to which data is migrated