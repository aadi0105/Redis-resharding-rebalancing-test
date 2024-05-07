import json
from time import sleep
import create_cluster
import count_slot_key
import write_keys
import add_master
import rebalance
import reshard
import remove_master

def count(step):
    print(f"{str(step)} > COUNT NODES\n\n")
    result= count_slot_key.count_slot_key(nodes["node1"]["ip"], nodes["node1"]["port"])
    print(f"{result}\n" )

def main(nodes):
    print("1 > EMPTY CLUSTER OF THREE NODES\n\n")
    result = create_cluster.create_cluster(nodes)
    print(f"{result}\n")

    sleep(10)
    count(2)

    #we need to wait for some time before writing keys otherwise cluster down error occurs
    print(f"3 > WRITE KEYS\n\n")
    result = write_keys.write_keys(nodes)
    print(f"{result}\n")
    
    count(4)
    
    print("5 > ADD MASTER\n\n")
    result = add_master.add_master(nodes["node1"]["ip"],6379,nodes["node4"]["ip"],6379)
    print(f"{result}\n" )

    sleep(10) #this wait is necessary. it doesn't show up in count otherwise.
    count(6)

    print("7 > REBALANCE\n\n")
    result= rebalance.rebalance_cluster(nodes["node4"]["ip"], nodes["node4"]["port"])
    print(f"{result}\n" )
    
    count(8)

    sleep(15)
    print("9> RESHARD\n\n")
    result= reshard.reshard(nodes["node1"]["ip"], nodes["node1"]["port"], nodes["node4"]["ip"], nodes["node4"]["port"])
    print(f"{result}\n" )
    
    count(10)

    sleep(10)
    print("11 > REBALANCE\n\n")
    result= rebalance.rebalance_cluster(nodes["node4"]["ip"], nodes["node4"]["port"])
    print(f"{result}\n" )

    count(12)

    print("13 > REMOVE 4TH NDOE\n\n")
    result= remove_master.remove_master(nodes["node4"]["ip"], nodes["node4"]["port"])
    print(f"{result}\n" )

    count(14)


file = open("./inventory.json")
nodes = json.load(file)
main(nodes)
