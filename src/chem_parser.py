import json

import regex

with open('data.json') as file:
    elements = json.load(file)


class ChemParser:
    '''
    Parses text in search of chemical elements
    '''
    elements = elements
    titles = elements.keys()
    regex = f'^({"|".join(map(lambda x: x.lower(), titles))})+$'

    @classmethod
    def dispatch(cls, text: str) -> bool:
        return cls.search(cls.clean(text))

    @classmethod
    def search(cls, text: str) -> bool:
        match = regex.match(cls.regex, text)
        print(match.groups())
        return bool(match)

    @classmethod
    def clean(cls, text: str) -> str:
        clean_text = ''
        for ch in text:
            if ch.isalpha(): clean_text += ch.lower()
        return clean_text

