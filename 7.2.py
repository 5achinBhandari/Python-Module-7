names_set = set()
while True:
    name = input("Enter a name (or press Enter to quit): ")


    if name == "":
        break


    if name in names_set:
        print(f"Existing name: {name}")
    else:
        print(f"New name: {name}")
        names_set.add(name)


print("\nList of input names:")
for name in names_set:
    print(name)
