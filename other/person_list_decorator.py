import operator

def person_lister(f):
    def inner(people):
        # complete the function
        print(people)
        print("---")
        people.sort(key = lambda i: int(i[2]))
        print(people)
        print("---")
        for p in people:
            yield f(p)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    inp = [
        "Jake Jake 42 M",
        "Jake Kevin 57 M",
        "Jake Michael 91 M",
        "Kevin Jake 2 M",
        "Kevin Kevin 44 M",
        "Kevin Michael 100 M",
        "Michael Jake 4 M",
        "Michael Kevin 36 M",
        "Michael Michael 15 M",
        "Micheal Micheal 6 M"
    ]

    people = [i.split() for i in inp]
    print(*name_format(people), sep='\n')
