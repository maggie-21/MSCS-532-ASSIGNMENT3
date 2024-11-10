from HashingWithChaining import HashTable
# Create a hash table
hash_table = HashTable(size=5)  # Small size to force collisions

# Insert items
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("cherry", 3)
hash_table.insert("banana", 4)  # Update value for "banana"
hash_table.insert("grape", 5)
hash_table.insert("mango", 6)  # Collision likely with small table size

# Search for items
print("Search 'banana':", hash_table.search("banana"))  # Should print updated value 4
print("Search 'cherry':", hash_table.search("cherry"))  # Should print 3
print("Search 'grape':", hash_table.search("grape"))    # Should print 5
print("Search 'nonexistent':", hash_table.search("nonexistent"))  # Should print None

# Delete items
print("Delete 'apple':", hash_table.delete("apple"))     # Should return True
print("Delete 'nonexistent':", hash_table.delete("nonexistent"))  # Should return False
print("Search 'apple' after deletion:", hash_table.search("apple"))  # Should print None
