from collections import defaultdict

def dict_key_access():
    inventory = {1:3, 2:4, 4:0, 5:10}
    print(inventory[1])
    print(inventory[5])
    try:
        print(inventory[3])
    except KeyError as e:
        print("Error:", e)
    
    print(inventory.get(3))

    if 4 in inventory:
        print("Zero is true (in)")
    if inventory.get(4):
        print("Zero is true (get)")
    
    inv2 = defaultdict(list, inventory)
    inv2[3].append(10)
    inv2[6].append(10)

    print(*enumerate(inv2))

if __name__ == "__main__":
    dict_key_access()