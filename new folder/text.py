import random
import string

# Generate large amounts of random data
data = []

# Create 100,000 random strings
for i in range(100000):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    data.append(random_string)

# Create large nested dictionaries
large_dict = {}
for i in range(10000):
    large_dict[f"key_{i}"] = {
        "nested_key": ''.join(random.choices(string.ascii_letters, k=200)),
        "value": random.randint(0, 1000000),
        "list": [random.random() for _ in range(100)]
    }

# Create a large list of tuples
large_list = [(i, random.random(), ''.join(random.choices(string.ascii_letters, k=50))) for i in range(50000)]

# Perform some operations
result = sum(len(item) for item in data)
dict_size = len(large_dict)
list_size = len(large_list)

print(f"Data size: {result}, Dict size: {dict_size}, List size: {list_size}")