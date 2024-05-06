import subprocess
import count_slot_key
import write_keys
import add_master
import rebalance
import rebalance_resharded
import reshard
import remove_master

# List of IP addresses
hosts = ["65.1.86.97", "3.110.148.234", "13.233.109.186", "13.234.231.230"]
ports = [6379, 6379, 6379, 6379]

def call_python_file(file_path, hosts):
    subprocess.run(["python", file_path, *hosts])

def main():
    #result= count_slot_key.count_slot_key(hosts[0], 6379)
    #print(result)
    #result = write_keys.write_keys(hosts, ports)
    #print(result)
    #result= count_slot_key.count_slot_key(hosts[0], 6379)
    #print(result)
    #result = add_master.add_master(hosts[0],6379,hosts[3],6379)
    #print(result)
    #result= count_slot_key.count_slot_key(hosts[0], 6379)
    #print(result)
    result= rebalance.rebalance_cluster(hosts[3], 6379)
    print(result)
    result= count_slot_key.count_slot_key(hosts[0], 6379)
    print(result)
    #result= reshard.reshard(hosts[0], 6379)
    #print(result)


if __name__ == "__main__":
    main()

