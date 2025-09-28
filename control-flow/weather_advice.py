weather = input("What's the wweather like today? (sunny/rainy/cold)").lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear warm coat and scarf.")
else :
    print("Sorry, I don't have recommendations for this weather.")
