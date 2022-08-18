class Name:

    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return "fn: {} ln: {}".format(self.firstname, self.lastname)

    def __lt__(self, other):
        return len(self.firstname) > len(other.firstname)


def remove_firstname_duplicates(names):
    dict_names = {}
    for i, n in enumerate(names):
        if n.firstname in dict_names:
            dict_names[n.firstname].append(i)
        else:
            dict_names[n.firstname] = [i]

    erase = []
    for dn in dict_names.items():
        if len(dn[1]) > 1:
            erase += dn[1][:-1]
    erase.sort(reverse=True)
    print(erase)
    for e in erase:
        names.remove(names[e])
    return names


def main():
    names = [
        Name('ilya', 'zlatkin'),
        Name('ilya', 'zlatkin'),
        Name('tamila', 'feldman'),
        Name('aron', 'zlatkin'),
        Name('aron', 'zlatkin'),
        Name('ilya', 'zlatkin'),
        Name('ilya', 'varlamov'),
    ]
    print(names)
    print(remove_firstname_duplicates(names))



if __name__ == '__main__':
    main()