size = 10
hash_array = [None] * size

def hash_code(keys):
    return keys % size

def insert(keys):
    hash_index = hash_code(keys)
    while hash_array[hash_index] is not None:
        hash_index += 1
        hash_index %= size   # wrap around if needed
    hash_array[hash_index] = keys

insert(11)
insert(22)
insert(33)

for i in range(size):
    print(f"Index {i}: {hash_array[i]}")
