from abc import ABC, abstractmethod
from typing import List, Dict, Union


class NlpProcessor(ABC):
    @abstractmethod
    def tokenize(self, text) -> List[Dict[str, Union[int, float, str, bool, None]]]:
        pass
