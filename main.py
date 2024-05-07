import json
import create_cluster
import count_slot_key
import write_keys
import add_master
import rebalance
import reshard
import remove_master

def count(step):
    result= count_slot_key.count_slot_key(nodes["node1"]["ip"], nodes["node1"]["port"])
    print(f"{str(step)} > COUNT NODES\n\n{result}\n" )

def main(nodes):

    result = create_cluster.create_cluster(nodes)
    print(f"1 > EMPTY CLUSTER OF THREE NODES\n\n{result}\n")

    count(2)

    #we need to wait for some time before writing keys otherwise cluster down error occurs

    result = write_keys.write_keys(nodes)
    print(f"3 > WRITE KEYS\n\n{result}\n")
    
    count(4)
    
    result = add_master.add_master(nodes["node1"]["ip"],6379,nodes["node4"]["ip"],6379)
    print(f"5 > ADD MASTER\n\n{result}\n" )

    count(6)

    result= rebalance.rebalance_cluster(nodes["node4"]["ip"], nodes["node4"]["port"])
    print(f"7 > REBALANCE\n\n{result}\n" )
    
    count(8)

    result= reshard.reshard(nodes["node1"]["ip"], nodes["node1"]["port"], nodes["node4"]["ip"], nodes["node4"]["port"])
    print(f"9> RESHARD\n\n{result}\n" )
    
    count(10)

    result= rebalance.rebalance_cluster(nodes["node4"]["ip"], nodes["node4"]["port"])
    print(f"11 > REBALANCE\n\n{result}\n" )

    count(12)

    result= remove_master.remove_master(nodes["node4"]["ip"], nodes["node4"]["port"])
    print(f"13 > REMOVE 4TH NDOE\n\n{result}\n" )

    count(14)


file = open("./inventory.json")
nodes = json.load(file)
main(nodes)
