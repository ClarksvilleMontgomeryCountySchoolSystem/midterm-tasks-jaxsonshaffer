slices = party_pizza_mini+large+medium
print(f"{slices}")

people += 1
share = slices//people
leftover = slices%people
print(f"Each person gets: {share}")
print(f"leftover slices: {leftover}")

people += 2 #Eric and Brandon are coming too.
share = slices//people
leftover = slices%people
print(f"Each person gets: {share}")
print(f"Leftover slices; {leftover}")



slices += party_pizza_mini
share = slices//people
leftover = slices%people
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")
print("...for Mr. Hollow Leg")
