beer = 99

while beer > 0:
   print(str(beer) + " bottles of beer on the wall, " + str(beer) + " bottles of beer.")
   print("Take one down, pass it around, " + str(beer - 1) + " bottles of beer on the wall.")
   beer -= 1
else:
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall...")