def order(sentence):
    words = sentence.split(" ")
    k_v = {}
    for word in words:
        for letter in word:
            if not letter.isalpha():
                k_v[int(letter)] = word
    
    k_v = dict(sorted(k_v.items()))
    values = k_v.values()
    return " ".join(values)
print(order("is2 Thi1s T4est 3a"))
