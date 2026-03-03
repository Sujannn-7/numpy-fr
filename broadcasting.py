# Using Loop: 

prices = [100, 200, 300, 270, 500, 670, 888, 127]
# discout = 13

# prices_after_discount = []

# for price in prices:
#     final_prices = price - (price*discout/100)
#     prices_after_discount.append(final_prices)

# print(prices_after_discount)

#Using Numpy

import numpy

prices1 = numpy.array(prices)

discount = 13
prices2 = prices1 - (prices1*discount/100)
 
print(prices2)