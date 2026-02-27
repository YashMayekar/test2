from abc import ABC, abstractmethod
from typing import Any, List
from dataclasses import dataclass
from enum import Enum


class DataType(Enum):
    """Enum for different data types"""
    STRINGS = "strings"
    NESTED_DICT = "nested_dict"
    TUPLES = "tuples"
    SETS = "sets"
    GROUPED = "grouped"


def read_data(path: str) -> List[str]:
    """Read and return all lines from the data file."""
    with open(path, "r", encoding="utf-8") as f:
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
        """Generate and return data of some type."""
        ...
