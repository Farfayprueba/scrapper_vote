from typing import Any
from dataclasses import dataclass


@dataclass
class PoolEntity:
    link        : list
    placeholder : list
    ingresarBttn: list
    captcha     : list
    fullName    : list
    nextBttn    : list
    voteBttn    : list
    voteBttnMain: list
    delete : list
       
    @staticmethod
    def init_entity(entity:Any)->'PoolEntity':
        link         = [int(x) for x in entity.link.split(',')]
        placeholder  = [int(x) for x in entity.placeholdermail.split(',')]
        ingresarBttn = [int(x) for x in entity.ingresarbttn.split(',')]
        captcha      = [int(x) for x in entity.captcha.split(',')]
        fullName     = [int(x) for x in entity.fullname.split(',')]
        nextBttn     = [int(x) for x in entity.nextbttn.split(',')]
        voteBttn     = [int(x) for x in entity.votebttn.split(',')]
        voteBttnMain = [int(x) for x in entity.votebttnmain.split(',')]
        delete = [int(x) for x in entity.eliminar.split(',')]
        return PoolEntity(link, placeholder, ingresarBttn, captcha, fullName, nextBttn, voteBttn, voteBttnMain, delete)