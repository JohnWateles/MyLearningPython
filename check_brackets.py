def check_brackets(_str: str) -> bool:
    pairs, stack = {"[": "]", "(": ")", "{": "}"}, list()
    for bracket in _str:
        if bracket in pairs:
            stack.append(bracket)
        elif stack != list() and pairs[stack[-1]] == bracket:
            stack.pop()
        else:
            return False
    return True


assert check_brackets("[()]") is True
assert check_brackets("[(}]") is False
assert check_brackets("[]][[]") is False
assert check_brackets("") is True
