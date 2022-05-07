import math

"""
Data types

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

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

#sorting
first = [11.25, 18.0, 20.0]
sorted_first = sorted(first, reverse=True)
print((sorted_first))

#string methods
place = "poolhouse"
place_up = place.upper()
print(place.count("o"))
print(first.index(20.0))
print(first.count(20.0))
first.append(24.5)
first.append(15.45)
first.reverse()
print(first)
