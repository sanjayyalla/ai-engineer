from enum import Enum

class ModelProvider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "gemini"


modelname = ModelProvider.ANTHROPIC
print(modelname.value)
