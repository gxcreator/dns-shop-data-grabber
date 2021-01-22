def PriceParser(price: str) -> (int, str):
    print(price)
    priceCond = price.replace(" ", "")
    for i in range(len(priceCond)):
        if not priceCond[i].isnumeric():
            return (int(priceCond[:i]), priceCond[i:])
    #raise ValueError(f'wrong price : {price}')
    return (0," ")



