def make_query(**kwarg):

    data = sorted(kwarg.items())
    query = ''

    for i in data:
        if query == '':
            query = query + i[0] + '=' + i[1]
        
        query = query + '&' + i[0] + '=' + i[1]

    return query

print(make_query(category='books', genre='thriller', author='Stephen_King'))