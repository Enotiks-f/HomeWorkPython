import re
from collections import Counter


def filter_transaction(transaction, search):
    pattern = re.compile(search, re.IGNORECASE)
    return [t for t in transaction if "description" in t and pattern.search(t["description"])]


def filter_description(transaction, categories):
    pattern = re.compile("|".join(categories), re.IGNORECASE)
    tt = []
    for i in transaction:
        try:
            if re.search(pattern, i["description"]):
                tt.append(i["description"])
        except (KeyError, TypeError, ValueError):
            continue

    compbined = " ".join(tt)
    matches = re.findall(pattern, compbined)
    counter = Counter(matches)

    return dict(counter)


def filter_state(transaction, state):
    pattern = re.compile(state, re.IGNORECASE)
    result = []
    for i in transaction:
        try:
            if re.search(pattern, i["state"]):
                result.append(i)
        except (KeyError, TypeError, ValueError):
            continue

    return result
