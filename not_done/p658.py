
def J(alphabet_length, word_length):
    if word_length < alphabet_length:
        return alphabet_length**word_length
    if word_length >= alphabet_length:
        return alphabet_length**word_length - alphabet_length*(alphabet_length-1)**word_length

def I(a, n):
    summ = 0
    for i in range(n+1):
        summ += J(a,i)
    return summ

def S(k,n):
    summ = 0
    for a in range(1,k+1):
        summ += I(a, n)
    return summ

print(I(3,0)) # 1
print(I(3,2)) # 13
print(I(3,4)) # 79

