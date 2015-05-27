"""
Find the start and end position of a phrase
"""
import re

def find(text):
    m = re.search("[\w \"\.\,\n]+", text)
    return m.start(), m.end()