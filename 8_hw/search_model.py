def search_contact(base, name):
    #base = base.split('\n')
    flag = True
    results = []
    for i in base:
        if name in i:
            flag = False
            results.append(i)
    return results