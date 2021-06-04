def patternmatch(string,pattern):
    s_len = len(string)
    p_len = len(pattern)
    memo = [[0 for p in range(p_len+1)] for s in range(s_len+1)]
    #for the memo table 0 will mean that its false, 1 will be true.
    #since memo[0][0] will be two empty strings, its true.
    for i in range(0,s_len+1):
        for j in range(0,p_len+1):
            if i == 0 or j == 0:
                #solve for empty string or pattern
                if i == 0 and j == 0:
                    memo[i][j] = True
                elif j == 0 and i > 0:
                    memo[i][j] = False
                    #no pattern
                elif i == 0 and pattern[j-1] == "*":
                    memo[i][j] = memo[i][j-1]
                    #no string, but first item of pattern is "*"
                else: 
                    memo[i][j] = False
                    #false if none of the above occue and i or j is = 0
            elif string[i-1]==pattern[j-1] or pattern[j-1] == "?":
                memo[i][j] = memo[i-1][j-1]
                #if character match or pattern character is able to match any single character
            elif pattern[j-1] == "*":
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
                #if not a match, but pattern character is * to match any sequence
            else:
                memo[i][j] = False
                #otherwise, matrix cell is false
    return memo[s_len][p_len]

            
# print(patternmatch("abcdefg", "a*d?fg"))
# print(patternmatch("abcdefg", "a*d?e"))
# print(patternmatch("abcdefg", "a?d"))
# print(patternmatch("abcdefg", "*?d*?e*"))
# print(patternmatch("abcdefg", "a*d?f*g"))
# print(patternmatch("abcdefg", "a*?g"))
# print(patternmatch("abcdefg", "a*d?e"))
