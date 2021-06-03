def game_bottomup(N):
    if N == 1 or N == 3 or N < 1:
        return False
    if N == 2:
        return True
    else:
        count_array = [0]*(N)
        count_array[1] = 1
        for i in range(4, len(count_array)+1):
            for j in range(2, int(i)):
                if count_array[i-1] == 0:
                    if (i) % j == 0:
                        if count_array[j-1] == 1:
                            count_array[i-1] = 1
        return bool(count_array[N-1])
                    

def game_topdown(N, memo=None):
    if memo == None:
        memo= [N+1]*(N)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 0
    if N == 3 or N == 1:
        return False
    if N == 2: 
        return True
    for j in range(1,(int(N)//2)):
        if N%j == 0:
            if memo[N-j]+1 == 1:
                return True
            if memo[N-j]+1 == 0:
                return False
            move = game_topdown_valid(N)
            if move > 0:
                memo[N-1] = 1
                game_topdown(N-1, memo)
            else:
                memo[N-1] = 0
                game_topdown(N-1, memo)
    return bool(memo[N-1])
        
        
def game_topdown_valid(N):
    if N == 1 and N%2 == 0:
        return 1
    factors = [1]
    good_move = 0
    for i in range(2,(int(N)//2)+1):
        if N % i == 0:
            factors.append(i)
    for j in range(len(factors)):
        if (N - factors[j]) % 2 == 1:
            if (N - factors[j]) == 3:
                good_move = 1
            if (N - factors[j]) > 3:
                good_move = 1
    return good_move

print(game_topdown(8))
