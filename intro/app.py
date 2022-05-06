# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# list areas
areas = [
    hall, kit, liv, bed, bath
]

# list with various types
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# list of lists
# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# type of
print((type(house)))

#subsetting of list
print(areas[0])
print(areas[-1])
print(house[2])
house_sub = house[0][1]
print("house sub is", house_sub)

#slicing and dicing
downstairs = areas[:6]
upstairs = areas[-4:]
upstairs_2 = areas[-4:]

#replacing list element
areas[-1] = 10.50
areas[4] = 'chill zone'

#extend list
areas_1 = areas + ['poolhouse', 24.5, 'a']
areas_2 = areas_1 + ['garage', 15.45]

# deleting item from list
print(areas)
del(areas[0])
print(areas)

#copying list
areas_copy = areas[:]
areas_copy_2 = list(areas)
