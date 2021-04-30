def max_independent_set(arr):
    memo = []
    three_back = []
    two_back = []
    one_back = []
    if len(arr) < 3:
        if len(arr) == 0:
            return memo
        if len(arr) == 1:
            if arr[0] >= 0:
                memo.append(arr[0])
            return memo
        if len(arr) == 2:
            if arr[0] and arr[1] < 0:
                return memo
            else:
                memo.append(max(arr[0], arr[1]))
                return memo
        
    else:
        if arr[2] < 0 or arr[0] < 0:
            if arr[2] < 0:
                three_back.append(arr[0])
                two_back.append(arr[1])
                one_back.append(arr[0])
                memo.append(arr[0])
                memo.append(arr[1])
                memo.append(arr[0])
            else:
                three_back.append(arr[0])
                two_back.append(arr[1])
                one_back.append(arr[2])
                memo.append(arr[0])
                memo.append(arr[1])
                memo.append(arr[2])
        else:
            three_back.append(arr[0])
            two_back.append(arr[1])
            one_back.append(arr[0])
            one_back.append(arr[2])
            memo.append(arr[0])
            memo.append(arr[1])
            memo.append(arr[0] + arr[2])
                
    for i in range(3,len(arr)):
        if arr[i] <= 0:
            memo.append(max(memo[i-3],memo[i-2]))
            if memo[i-3] > memo[i-2]:
                temp = three_back[:]
                three_back = two_back[:]
                two_back = one_back[:]
                one_back = temp[:]
            else:
                temp = two_back[:]
                three_back = two_back[:]
                two_back = one_back[:]
                one_back = temp[:]
        else:
            memo.append(arr[i] + max(memo[i-3],memo[i-2]))
            if memo[i-3] > memo[i-2]:
                temp = three_back[:]
                temp.append(arr[i])
                three_back = two_back[:]
                two_back = one_back[:]
                one_back = temp[:]
            else:
                temp = two_back[:]
                temp.append(arr[i])
                three_back = two_back[:]
                two_back = one_back[:]
                one_back = temp[:]
                
    if memo[len(memo)-1] > memo[len(memo)-2]:
        return one_back
    else:
        return two_back
