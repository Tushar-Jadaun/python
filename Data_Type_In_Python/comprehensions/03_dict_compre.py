tea_price = {
    "Masala chai": 40,
    "green tea" : 30,
    "lemon tea" : 200
}
tea_price_usd = {tea:price/80  for tea,price in tea_price.items()}

print(tea_price_usd)










