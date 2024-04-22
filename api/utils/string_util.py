from typing import List

from errors.utils import TypeError1, SizeError


class StringUtil(object):

    @staticmethod
    def replace_(string: str, old: str | List[str], new: str | List[str]) -> str:
        if type(old) is not type(new):
            raise TypeError1
        if isinstance(old, str):
            return string.replace(old, new)
        if len(old) != len(new):
            raise SizeError
        for old_, new_ in zip(old, new):
            string = string.replace(old_, new_)
        return string
