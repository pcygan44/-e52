stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston"from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop

# 1
a = stops.append("Edinburgh Waverley")
print(stops)

# 2
b = stops.insert(0,"Glasgow Queen St" )
print(stops)

# 3
c = stops.insert(4,"Polmont"  )
print(stops)

# 4
d = print(stops.index("Linlithgow"))

# 5
e = stops.remove("Livingston")
print(stops)

# 6
del stops[2]
print(stops)

# 7
g = print(len(stops))

# 8
i = stops.sort()
print(stops)

# 9
j = stops.reverse()
print(stops)

# 10
for stop in stops:
    print(stop)