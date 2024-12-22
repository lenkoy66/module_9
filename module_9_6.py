def all_variants(text):
    n = len(text)

    for a in range(n):
        for b in range(n - a):
            yield text[b:b+a+1]

a = all_variants("abc")
for i in a:
    print(i)

