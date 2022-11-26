from grongier.pex import Message
from dataclasses import dataclass

@dataclass
class SaveFileRequest(Message):
    filename: str = None
    content: str = None