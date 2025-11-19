def maximumWealth(multiarray):
    richest_array = []
    for client in multiarray:
        wealth = sum(client)
        richest_array.append(wealth)
    return max(richest_array)

entrada = [[1,5],[7,3],[3,5]]
call = maximumWealth(entrada)
print(call)
