import math
restaurants = ["Tatsunoya Ramen", "Borneo Kalimantan Cuisine", "El Cholo Spanish Eatery", "President Thai", "Domenico's Pizza", "Wingstop", "Kaiba Sushi", "Mintleaf Indian Cuisine", "Noodle World", "Dog Haus"]
backup = restaurants
new_list = restaurants
final_ranking = []

mid_value = (math.ceil(len(restaurants) / 2))
new_restaurant = input("What restaurant would you like to add to ranking? ")

while len(new_list) > 1:
    move = input("Which restaurant is better: A) " + new_restaurant + ", or B) " + new_list[mid_value - 1] + "? ")

    if move == "A" or move == "a":
        new_list = backup[0:mid_value]

    if move == "B" or move == "b":
        new_list = backup[mid_value:len(restaurants)]

    backup = new_list
    mid_value = (math.ceil(len(new_list) / 2))

print(new_list[0])

for restaurant in restaurants:
    if restaurant != new_list[0]:
        final_ranking.append(restaurant)

    else:
        if move == "A" or move == "a":
            final_ranking.append(new_restaurant)
            final_ranking.append(restaurant)
        if move == "B" or move == "b":
            final_ranking.append(restaurant)
            final_ranking.append(new_restaurant)

print("Your new ranking is:")
print(final_ranking)
