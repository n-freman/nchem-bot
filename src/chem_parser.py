import json
from typing import Dict, List, Literal

with open('data.json') as file:
    elements = json.load(file)


class ChemParser:
    '''
    Parses text in search of chemical elements
    '''
    elements = elements
    titles = elements.keys()

    @classmethod
    def dispatch(cls, text: str) -> List[str]:
        if len(text) == 0:
            raise EmptyTextError(
                'Can not find elements in empty text'
            )
        return cls._find_full_sequences(cls._search(cls._clean(text)))

    @classmethod
    def _find_full_sequences(cls, results: Dict[str, Dict] | Literal[True]) -> List[str]:
    # Iterate over results
        if results is True:
            return ['']
        if results == {}:
            return False # type: ignore
        combinations = []
        for key in results.keys():
            result = cls._find_full_sequences(results[key])
            if not result:
                continue
            combinations.extend(
                cls.merge_results(
                    key,
                    cls._find_full_sequences(results[key])
                )
            )
        return combinations

    @classmethod
    def _search(cls, text: str) -> Dict[str, Dict] | Literal[True]:
        if len(text) == 0:
            return True
        result = {}
        for el in cls.titles:
            if text.startswith(el):
                result[el] = cls._search(text[len(el):])
        return result


    @classmethod
    def _clean(cls, text: str) -> str:
        clean_text = ''
        for ch in text:
            if ch.isalpha(): clean_text += ch.lower()
        return clean_text

    @staticmethod
    def merge_results(element, combinations):
        result = []
        for i in combinations:
            result.append(element + i)
        return result


class EmptyTextError(Exception):
    pass

