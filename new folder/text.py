import random
import string
import json
from collections import defaultdict

# Generate large amounts of random data
data = [] 

# Create 1,000,000 random strings
for i in range(1000000):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=500))
    data.append(random_string)

# Create large nested dictionaries
large_dict = {}
for i in range(100000):
    large_dict[f"key_{i}"] = {
        "nested_key": ''.join(random.choices(string.ascii_letters, k=500)),
        "value": random.randint(0, 10000000),
        "list": [random.random() for _ in range(500)],
        "timestamp": random.randint(1000000, 9999999),
        "sub_data": {str(j): random.random() for j in range(50)}
    }

# Create a large list of tuples
large_list = [(i, random.random(), ''.join(random.choices(string.ascii_letters, k=200))) for i in range(500000)]

# Create set of unique values
unique_values = set(''.join(random.choices(string.ascii_letters, k=20)) for _ in range(100000))

# Create defaultdict with lists
grouped_data = defaultdict(list)
for i in range(200000):
    key = random.choice(string.ascii_uppercase)
    grouped_data[key].append(random.randint(1, 100000))

# Perform operations
result = sum(len(item) for item in data)
dict_size = len(large_dict)
list_size = len(large_list)
unique_count = len(unique_values)
grouped_count = len(grouped_data)
max_group_size = max(len(v) for v in grouped_data.values()) if grouped_data else 0

# Store analysis results in JSON format
json_results = {
    "data_size": result,
    "dict_size": dict_size,
    "list_size": list_size,
    "unique_values": unique_count,
    "grouped_items": grouped_count,
    "max_group_size": max_group_size
}

json_output = json.dumps(json_results, indent=2)

print(f"Data size: {result}, Dict size: {dict_size}, List size: {list_size}")
print(f"Unique values: {unique_count}, Grouped items: {grouped_count}, Max group size: {max_group_size}")
print("\nJSON Analysis Results:")
print(json_output)