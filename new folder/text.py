import random
import string
import json
from collections import defaultdict
from abc import ABC, abstractmethod
from typing import Dict, List, Set, Tuple, Any
from dataclasses import dataclass
from enum import Enum


class DataType(Enum):
    """Enum for different data types"""
    STRINGS = "strings"
    NESTED_DICT = "nested_dict"
    TUPLES = "tuples"
    SETS = "sets"
    GROUPED = "grouped"


@dataclass
class AnalysisResult:
    """Data class for storing analysis results"""
    data_size: int
    dict_size: int
    list_size: int
    unique_values: int
    grouped_items: int
    max_group_size: int


class DataGenerator(ABC):
    """Abstract base class for data generators"""
    
    @abstractmethod
    def generate(self) -> Any:
        pass
    
    @abstractmethod
    def analyze(self) -> Dict[str, int]:
        pass


class StringDataGenerator(DataGenerator):
    def __init__(self, count: int = 1000000, length: int = 500):
        self.count = count
        self.length = length
        self.data = []
    
    def generate(self) -> List[str]:
        self.data = [''.join(random.choices(string.ascii_letters + string.digits, k=self.length)) for _ in range(self.count)]
        return self.data
    
    def analyze(self) -> Dict[str, int]:
        return {"total_chars": sum(len(item) for item in self.data)}


class DictDataGenerator(DataGenerator):
    def __init__(self, count: int = 100000, nested_size: int = 50):
        self.count = count
        self.nested_size = nested_size
        self.data = {}
    
    def generate(self) -> Dict:
        self.data = {f"key_{i}": {"nested_key": ''.join(random.choices(string.ascii_letters, k=500)), "value": random.randint(0, 10000000), "list": [random.random() for _ in range(500)], "timestamp": random.randint(1000000, 9999999), "sub_data": {str(j): random.random() for j in range(self.nested_size)}} for i in range(self.count)}
        return self.data
    
    def analyze(self) -> Dict[str, int]:
        return {"dict_size": len(self.data)}


class TupleDataGenerator(DataGenerator):
    def __init__(self, count: int = 500000, string_length: int = 200):
        self.count = count
        self.string_length = string_length
        self.data = []
    
    def generate(self) -> List[Tuple]:
        self.data = [(i, random.random(), ''.join(random.choices(string.ascii_letters, k=self.string_length))) for i in range(self.count)]
        return self.data
    
    def analyze(self) -> Dict[str, int]:
        return {"tuple_count": len(self.data)}


class SetDataGenerator(DataGenerator):
    def __init__(self, count: int = 100000, length: int = 20):
        self.count = count
        self.length = length
        self.data = set()
    
    def generate(self) -> Set[str]:
        self.data = {''.join(random.choices(string.ascii_letters, k=self.length)) for _ in range(self.count)}
        return self.data
    
    def analyze(self) -> Dict[str, int]:
        return {"unique_count": len(self.data)}


class GroupedDataGenerator(DataGenerator):
    def __init__(self, count: int = 200000):
        self.count = count
        self.data = defaultdict(list)
    
    def generate(self) -> defaultdict:
        for _ in range(self.count):
            self.data[random.choice(string.ascii_uppercase)].append(random.randint(1, 100000))
        return self.data
    
    def analyze(self) -> Dict[str, int]:
        max_size = max((len(v) for v in self.data.values()), default=0)
        return {"grouped_items": len(self.data), "max_group_size": max_size}


class DataAnalyzer:
    def __init__(self):
        self.generators: Dict[str, DataGenerator] = {}
    
    def register_generator(self, name: str, generator: DataGenerator) -> None:
        self.generators[name] = generator
    
    def generate_all(self) -> None:
        for generator in self.generators.values():
            generator.generate()
    
    def analyze_all(self) -> AnalysisResult:
        combined = {}
        for generator in self.generators.values():
            combined.update(generator.analyze())
        
        return AnalysisResult(
            combined.get("total_chars", 0),
            combined.get("dict_size", 0),
            combined.get("tuple_count", 0),
            combined.get("unique_count", 0),
            combined.get("grouped_items", 0),
            combined.get("max_group_size", 0)
        )
    
    def print_summary(self, result: AnalysisResult) -> None:
        print(f"Data: {result.data_size}, Dict: {result.dict_size}, List: {result.list_size}")
        print(f"Unique: {result.unique_values}, Grouped: {result.grouped_items}, Max: {result.max_group_size}")
        print(json.dumps(result.__dict__, indent=2))


if __name__ == "__main__":
    analyzer = DataAnalyzer()
    analyzer.register_generator("dicts", DictDataGenerator(count=100000, nested_size=50))
    analyzer.register_generator("tuples", TupleDataGenerator(count=500000, string_length=200))
    analyzer.register_generator("sets", SetDataGenerator(count=100000, length=20))
    analyzer.register_generator("grouped", GroupedDataGenerator(count=200000))
    
    print("Analyzing data...")
    results = analyzer.analyze_all()
    analyzer.print_summary(results)
