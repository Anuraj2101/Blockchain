
names = ["Sam", "Bob", "Alice", "Mike", "Alex", "Roger"]

with open("utils/verified_voters.txt", "w") as f:
    for name in names:
        f.write(name+"\n")