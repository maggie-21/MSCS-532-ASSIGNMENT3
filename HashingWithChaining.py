class HashTable:
    def __init__(self, size=10):
        self.size = size  # Size of the hash table
        self.table = [[] for _ in range(self.size)]  # Initialize table with empty lists
    
    def hash_function(self, key):
        """Hash function that maps keys to table indices."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)
        # Check if the key already exists and update the value if it does
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Update existing value
                return
        # If the key is not found, append it to the chain
        self.table[index].append([key, value])

    def search(self, key):
        """Search for a value associated with the given key."""
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]  # Return the associated value
        return None  # Key not found

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]  # Remove the item from the chain
                return True
        return False  # Key not found
