# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):

        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        # Fill this in.

        index - self.hash_mod(key)
        linked_pair = LinkedPair(key, value)

        if self.storage[index]:
            if self.retrieve(key):
                linked_list = self.storage[index]
                current = linked_list.head
                while current:
                    if current.key == key:
                        current.value = value
                    current = current.next
            else:
                linked_list = self.storage[index]
                linked_list.tail.next = linked_pair
                linked_list.tail = linked_pair

        else:
            self.storage[index] LinkedList(linked_pair)
        return self

        pass

    def remove(self, key):
        # '''
        # Remove the value stored with the given key.

        # Print a warning if the key is not found.
        # '''
        # Fill this in.

        linked_pair_value self.retrieve(key)
        index = self._hash.mod(key)
        linked_list = self.storage[index]

        if linked_pair_value:
            current = linked_list.head
            prev = current

            # if there's only one linked_pair in the list
            if current == linked_list.head and current == linked_list.tail:
                self.storage[index] = None
                return True
            # else if the head has the key we want to remove:
        elif current.key == key:
            linked_list.head = current.next
            current.next = None
            return True
        else:
            print('current value', current.value)
            print('prev value', prev.value)
            while current:
                if current.key == key:
                    if linked_list.tail == current:
                        linked_list.tail = prev
                    prev.next = current.next
                    current.next = None
                    return True
                prev = current

                current = current.next
        return "bleep"
        pass

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        pass

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
