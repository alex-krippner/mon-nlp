from abc import ABC, abstractmethod
from typing import List, Dict


class NlpProcessor(ABC):
    @abstractmethod
    def tokenize(self, text) -> List[Dict[str, List[str]]]:
        pass
