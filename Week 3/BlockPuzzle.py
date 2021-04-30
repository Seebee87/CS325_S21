def blockpuzzle_dp(n):
    unit_count_table = [n+1]*(n+1)

    unit_count_table[0] = 1 
    unit_count_table[1] = 1

    for i in range(2,len(unit_count_table)):
        unit_count_table[i] = unit_count_table[i-1] + unit_count_table[i-2]
    
    return unit_count_table[len(unit_count_table)-1]

print(blockpuzzle_dp(6))