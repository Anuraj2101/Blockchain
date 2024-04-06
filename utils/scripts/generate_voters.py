import hashlib

def hash_data(data):
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    return hashed_data

names = {"Sam":"2234", "Bob":"2412", "Alice":"5213", "Mike":"7867", "Alex":"2102", "Roger":"9035"}

with open("utils/verified_voters.txt", "w+") as f:
    for name in names:
        hashed_uuid = hash_data(names[name]) 
        f.write(name + ":" + hashed_uuid + "\n")