import re

def ccn_safety(text):
    regex = re.compile(r"""
        (?<!-)    # look for an expression without hyphen before of the expression     
        \d{4}-    # first 4 digits from the credit card with the respective hyphen
        \d{4}-    # second 4 digits from the credit card with the respective hyphen
        \d{4}-    # third 4 digits from the credit card with the respective hyphen
        \d{4}     # last 4 digits from the credit card
        (?!-)     # loof for an expression without hyphen after of the expression
        """, re.VERBOSE)
    text, count = regex.subn("CCN REMOVED FOR YOUR SAFETY", text)
    return text, count