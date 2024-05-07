from subprocess import getoutput
def count_slot_key(node, port):
    result = getoutput(f"redis-cli --cluster check {node}:{str(port)} | grep slaves")
    return result
