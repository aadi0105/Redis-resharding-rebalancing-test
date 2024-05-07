import redis
import hashlib

# Function to calculate the slot for a given key
def calculate_slot(key):
    return hashlib.sha1(key.encode('utf-8')).hexdigest()

def write_keys(cluster):
    # Connect to the Redis cluster
    rc = redis.Redis(host=cluster["node1"]["ip"], port=int(cluster["node1"]["port"]), decode_responses=True)

    # Write 1000 keys evenly distributed among all masters
    for i in range(10):
        key = f'key{i}'
        slot = int(calculate_slot(key), 16) % 16384  # 16384 is the total number of slots in Redis
        try:
            if slot < 5461:  # Each master will handle roughly 1/3rd of the keys
                rc.set(key, f'value{i}')
            elif slot < 10922:
                rc = redis.Redis(host=cluster["node2"]["ip"], port=int(cluster["node2"]["port"]), decode_responses=True)
                rc.set(key, f'value{i}')
            else:
                rc = redis.Redis(host=cluster["node3"]["ip"], port=int(cluster["node3"]["port"]), decode_responses=True)
                rc.set(key, f'value{i}')
        except redis.exceptions.ResponseError as e:
            try:
                # If MOVED response received, reconnect to the correct Redis instance
                new_host, new_port = str(e).split()[2].split(':')
                rc = redis.Redis(host=new_host, port=int(new_port), decode_responses=True)
                rc.set(key, f'value{i}')
            except:
                return e
    return "Keys written successfully."

    

