# strip the given word from a list

def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l = ['Rakesh', 'Manish', 'Hitesh', 'Kamlesh', 'Chetan', 'sh']

print(rem(l, 'sh'))
