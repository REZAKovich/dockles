products = ['яблоки', 'бананы', 'хлеб', 'молоко', 'сыр', 'курица', 'рис', 'масло', 'йогурт', 'кофе']

pricelist = [150, 90, 60, 80, 350, 280, 120, 200, 70, 450]

sallers = ['001', '023', '045', '067', '089', '102', '124', '146', '168', '180']

totalData = []
for i in zip(products, pricelist, sallers):
    totalData.append(i)

print(totalData)