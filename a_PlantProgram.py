import a_PlantClass as pc

primrose = pc.Plant("Green")

# sunflower = pc.Flower("Yellow") #this will be an error because you are missing
# petals argument

sunflower = pc.Flower("Yellow", 12)

print(primrose.get_color())  # (Green)

# (Yellow) b/c of inheritance subclass can use this method
print(sunflower.get_color())
print(sunflower.get_petals())


# print(primrose.get_petals()) #this will cause an error because superclass
# doesn't have attribute petals
