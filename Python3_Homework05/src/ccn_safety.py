import re

def ccn_safety(text):
    lst_to_replace = re.findall(r"[^\d-]\d{4}-\d{4}-\d{4}-\d{4}[^-\d]", text)
    count = 0
    for value in lst_to_replace:
        text = re.sub(r"[^\d-]\d{4}-\d{4}-\d{4}-\d{4}[^-\d]", " XXXX-XXXX-XXXX-{0}".format(value[16:21]), text,1)
        count += 1  
    return text, count
