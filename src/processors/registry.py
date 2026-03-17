from .demat import DematProcessor
from .citizenship import CitizenshipProcessor

PROCESSOR_MAP = {
    "demat": DematProcessor(),
    "citizenship": CitizenshipProcessor()
}


def get_processor(doc_type):
    return PROCESSOR_MAP.get(doc_type)