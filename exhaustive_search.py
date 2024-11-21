def knapSack(max_weight, weights, value, n):
    # base case
    if n == 0 or max_weight == 0:
        return 0
    
    # mulai dari elemen paling akhir
    # jika elemen weights ke n-1 lebih besar 
    # dari maksimal beban yang bisa dibawa,
    # lakukan rekursi dengan menggeser indeks weights dan values
    if (weights[n-1] > max_weight):
        return knapSack(max_weight, weights, value, n-1)
    
    # mengembalikan nilai maksimum dari dua kasus jika:
    # memuat elemen value/weights ke-n
    # tidak memuat value/weights ke-n
    else:
        return max(value[n-1] + knapSack(max_weight - weights[n-1], weights, value, n-1), knapSack(max_weight, weights, value, n-1))

values = [60, 100]
weights = [10, 20]
max_weight = 40
n = len(values)
result = knapSack(max_weight, weights, values, n)
print(result)