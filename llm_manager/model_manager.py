from abc import ABC, abstractmethod

class LlmModelManager(ABC):
    @abstractmethod
    def get_model(self, model_name: str = None):
        pass

    @abstractmethod
    def generate(self, prompt: str, model_name: str = None, **kwargs) -> str:
        pass