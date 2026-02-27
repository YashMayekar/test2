import random
import string
from abc import ABC, abstractmethod
from typing import Dict, Any
from dataclasses import dataclass
from enum import Enum


class DataType(Enum):
    """Enum for different data types"""
    STRINGS = "strings"
    NESTED_DICT = "nested_dict"
    TUPLES = "tuples"
    SETS = "sets"
    GROUPED = "grouped"
def read_data(path):
    """Read and return all lines from the data file."""
    with open(path, "r") as f:
        return f.readlines()
def read_data(path):
    """Read and return all lines from the data file."""
    with open(path, "r") as f:
        return f.readlines()
def read_data(path):
    """Read and return all lines from the data file."""
    with open(path, "r") as f:
        return f.readlines()
def read_data(path):
    """Read and return all lines from the data file."""
    with open(path, "r") as f:
        return f.readlines()



@dataclass
class AnalysisResult:
    """Data class for storing analysis results"""
    data_size: int
    dict_size: int
    list_size: int


class DataGenerator(ABC):
    """Abstract base class for data generators"""
    
    @abstractmethod
    def generate(self) -> Any:
        pass


class DictDataGenerator(DataGenerator):
    def __init__(self, count: int = 100000, nested_size: int = 50):
        self.count = count
        self.nested_size = nested_size
        self.data = {}
    
    def generate(self) -> Dict:
        self.data = {f"key_{i}": {"nested_key": ''.join(random.choices(string.ascii_letters, k=500)), "value": random.randint(0, 10000000)} for i in range(self.count)}
        return self.data


class DataAnalyzer:
    def __init__(self):
        self.generators: Dict[str, DataGenerator] = {}
    
    def register_generator(self, name: str, generator: DataGenerator) -> None:
        self.generators[name] = generator
    
    def generate_all(self) -> None:
        for generator in self.generators.values():
            generator.generate()


if __name__ == "__main__":
    analyzer = DataAnalyzer()
    analyzer.register_generator("dicts", DictDataGenerator(count=100000, nested_size=50))
    analyzer.generate_all()
