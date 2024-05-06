import redis
import hashlib

def write_keys(hosts, ports):
    # Connect to the Redis cluster
    rc = redis.Redis(host=hosts[0], port=6379, decode_responses=True)

    # Function to calculate the slot for a given key
    def calculate_slot(key):
        return hashlib.sha1(key.encode('utf-8')).hexdigest()

    # Write 1000 keys evenly distributed among all masters
    for i in range(1000):
        key = f'key{i}'
        slot = int(calculate_slot(key), 16) % 16384  # 16384 is the total number of slots in Redis
        try:
            if slot < 5461:  # Each master will handle roughly 1/3rd of the keys
                rc.set(key, f'value{i}')
            elif slot < 10922:
                rc = redis.Redis(host=hosts[1], port=6379, decode_responses=True)
                rc.set(key, f'value{i}')
            else:
                rc = redis.Redis(host=hosts[2], port=6379, decode_responses=True)
                rc.set(key, f'value{i}')
            print(key, f'value{i}')
        except redis.exceptions.ResponseError as e:
            # If MOVED response received, reconnect to the correct Redis instance
            new_host, new_port = str(e).split()[2].split(':')
            rc = redis.Redis(host=new_host, port=int(new_port), decode_responses=True)
            rc.set(key, f'value{i}')
    print("Keys written successfully.")

    

