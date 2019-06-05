import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.last = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, timestamp, data):

        if self.head is None:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
            return
        else:
            current = self.last
            self.last = Block(timestamp, data, current)
            self.last.previous_hash = current
            return

def get_utc():
    utc = datetime.datetime.utcnow()
    return utc.strftime("%d/%m/%Y %H:%M:%S")

block0 = Block(get_utc(), "Some Information", 0)
block1 = Block(get_utc(), "Another Information", block0)
block2 = Block(get_utc(), "Some more Information", block1)

print(block0.data)
print(block0.hash)
print(block0.timestamp)
print(block1.previous_hash.data)

temp = BlockChain()
temp.append(get_utc(), "Some Information")
temp.append(get_utc(), "Another Information")
print(temp.last.data)
print(temp.last.previous_hash.data)