import random
import string
import json
from collections import defaultdict

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
        "list": [random.random() for _ in range(100)],
        "timestamp": random.randint(1000000, 9999999)
    }

# Create a large list of tuples
large_list = [(i, random.random(), ''.join(random.choices(string.ascii_letters, k=50))) for i in range(50000)]

# Additional: Create set of unique values
unique_values = set(''.join(random.choices(string.ascii_letters, k=10)) for _ in range(5000))

# Additional: Create defaultdict with lists
grouped_data = defaultdict(list)
for i in range(20000):
    key = random.choice(string.ascii_uppercase)
    grouped_data[key].append(random.randint(1, 100))

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

# Convert to JSON string
json_output = json.dumps(json_results, indent=2)

print(f"Data size: {result}, Dict size: {dict_size}, List size: {list_size}")
print(f"Unique values: {unique_count}, Grouped items: {grouped_count}, Max group size: {max_group_size}")
print("\nJSON Analysis Results:")
print(json_output)