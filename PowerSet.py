def powerset(input):
    result = []
    helper(len(input)-1, [], input, result)
    return result
    
def helper(pointer, choices_made, input, result):
    if pointer < 0:
        result.append(choices_made[:])
        return
    choices_made.append(input[pointer])
    helper(pointer-1, choices_made, input, result)
    choices_made.pop()
    helper(pointer-1, choices_made, input, result)