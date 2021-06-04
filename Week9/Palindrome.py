def checkPalindrome_1(string, k):
    rev_string = string[::-1]
    strlen = len(string)
    removed = pal_helper_1(string, rev_string, strlen, strlen)
    if removed > k*2:
        return False
    else: 
        return True

def pal_helper_1(string1, string2, len1, len2):
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1
    if string1[len1-1] == string2[len2-1]:
        return pal_helper_1(string1, string2, len1-1, len2-1)
    cuts = 1 + min(pal_helper_1(string1, string2, len1-1, len2),
                       pal_helper_1(string1, string2, len1, len2-1))
    return cuts
    

#checkPalindrome_2 approach will use a bottom up approach
def checkPalindrome_2(string,k):
    reversed = string[::-1]
    string_len = len(string)
    memo = [[0 for x in range(string_len+1)] for y in range(string_len+1)]
    
    for i in range(string_len+1):
        for j in range(string_len+1):
            if i == 0 or j == 0:
                memo[i][j] = i+j
                #if either string is empty, value is length of other string to remove
            elif string[i-1] == reversed[j-1]:
                memo[i][j] = memo[i-1][j-1]
                #if both letters match, copy memo[i-1][j-1] to that location
            else:
                memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1])
                #if they dont match, take 1 + the minimum of the cell in the table to the top or left
            
    least = memo[string_len][string_len]
    if least <= k*2:
        return True
    else:
        return False
            
print(checkPalindrome_1("abhyjba",2))

