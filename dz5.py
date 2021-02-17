productPrice = [57.8, 46.51, 97, 22, 31.8, 21.4, 111.7, 42, 8.4, 7]
priceSentenceA = 'A:'

for priceR in productPrice:
    priceKK = int((priceR * 100) % 100)
    priceR = int(priceR)
    priceSentenceA += f' {priceR}r {priceKK:02d}kk,'

print(priceSentenceA)

productPrice = sorted(productPrice)

print(f'B: {productPrice}')

productPriceReverset = [57.8, 46.51, 97, 22, 31.8, 21.4, 111.7, 42, 8.4, 7]

productPriceReverset = sorted(productPrice)
productPriceReverset = productPriceReverset[::-1]

print(f'C: {productPriceReverset}')

productPrice = productPrice[-5:]

print(f'D: {productPrice}')
