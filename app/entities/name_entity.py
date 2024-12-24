from typing import Any
from dataclasses import dataclass


@dataclass
class nameEntity:
    nombre        : str
    paterno : str
    materno: str
       
    @staticmethod
    def init_entity()->'nameEntity':
        return nameEntity(None,None,None)