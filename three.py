# Iteration

def reverse_string(s):
    reverse_strings = ""
    for char in s:
        reverse_strings = char + reverse_strings
    return reverse_strings


# Recursion
# s="hello" ello h  llo eh lo leh o lleh olleh
def recursive_string(s):
    # base case
    if len(s) <= 1:
        return s
    
    return recursive_string(s[1:] + s[0])

