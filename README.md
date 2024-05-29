# Algorithms and Data Structures (Cheat Sheet)

> [!NOTE]  
> This is a cheat sheet on algorithms and data structures (mostly notes-to-self). They are
> incomplete by default.

## Data structures

### Associative arrays (or dictionaries, maps, hash tables)

Source: ChatGPT

An associative array is a data structure that represents a collection of key-value pairs, where each
unique key is associated with a value. It allows for efficient retrieval, insertion, and deletion of
values based on their associated keys. This concept is fundamental in computer science and is
implemented in various programming languages under different names.

“Associative array” is often used interchangeably with “dictionary” (or “dict” in some languages
like Python), “map” (in Java, C++), or “hash table” (in several contexts). In essence, associative
arrays and dictionaries are conceptually the same. The difference is mostly semantic and contextual,
depending on the programming language or community.

Characteristics of an associative array:

1.  Keys and Values: Each element in an associative array consists of a unique key and a
    corresponding value.
1.  Key Lookup: The primary operation is the ability to quickly retrieve a value based on its key.
1.  Dynamic Size: Associative arrays can grow or shrink dynamically as key-value pairs are added or
    removed.
1.  Efficient Access: Optimized for average-case constant time complexity $O(1)$ for lookups,
    insertions, and deletions, assuming a good hash function.

For example:

1.  "Associative Array" (JavaScript Object)

    ```javascript
    let associativeArray = {
      name: "Alic",
      age: 30,
      job: "Software Engineer",
    };

    console.log(associativeArray["name"]); // Output: Alice
    ```

1.  "Dictionary" (Python)

        ```python
        dictionary = {
            "name": "Alice",
            "age": 30,
            "job": "Software Engineer"
        }

        print(dictionary["name"])  # Output: Alice
        ```

