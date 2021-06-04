def checkPalindrome_1(string, k):
    if string == "":
        return True
    lower_string = string.lower()
    reversed_string = lower_string[::-1]
    string_len = len(string)
    no_match = pal_helper_1(lower_string, reversed_string, string_len, 0)
    if no_match > k:
        print(str(no_match) + " is greater than " + str(k))
        print("this is not a k-palindrome")
        return False
    else: 
        print(str(no_match) + " characters did not match, whis is less than or equal to " + str(k))
        print("this is k-palindrome")
        return True

def pal_helper_1(string1, string2, length, incorrect):
    if length == 0:
        return incorrect
    if string1[0] == string2[0]:
        return pal_helper_1(string1[1:], string2[1:], length-1, incorrect)
    else:
        return pal_helper_1(string1[1:], string2[1:], length-1, incorrect+1)



def checkPalindrome_2(string, k):
    rev_string = string[::-1]
    strlen = len(string)
    removed = pal_helper_2(string, rev_string, strlen, strlen)
    print(str(removed) + " characters removed")
    if removed > k*2:
        return False
    else: 
        return True

def pal_helper_2(string1, string2, len1, len2):
    if len1 == 0:
        print("len 1 at 0, return value len2 = " + str(len2))
        return len2
    if len2 == 0:
        print("len 2 at 0, return value len1 = " + str(len1))
        return len1
    if string1[len1-1] == string2[len2-1]:
        return pal_helper_2(string1, string2, len1-1, len2-1)
    cuts = 1 + min(pal_helper_2(string1, string2, len1-1, len2),
                       pal_helper_2(string1, string2, len1, len2-1))
    print(cuts)
    return cuts
    
print(checkPalindrome_1("abcdnondba", 3))


