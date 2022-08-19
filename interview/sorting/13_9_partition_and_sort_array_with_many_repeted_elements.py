import collections
import heapq


class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return "{} : {} \n".format(self.name, self.age)

    def __lt__(self, other):
        return self.age > other.age


def partition_sort(students: list[Student]):
    #events.sort(reverse=True) # 0(n*log(n)) # wost-case O(n**2)
    print(students)
    st_count = collections.Counter((s.age for s in students))
    print(st_count)
    ofsets = {}
    original_offset = {}
    current = 0
    for c in st_count.items():
        ofsets[c[0]] = current
        original_offset[c[0]] = current
        current += c[1]
    print(ofsets)
    for ind_from in range(len(students)):
        s = students[ind_from]
        tmp = s.age
        ind_to = ofsets[tmp]
        if ind_from >= original_offset[tmp] and ind_from <= ind_to:
            continue
        ofsets[tmp] += 1
        students[ind_from], students[ind_to] = students[ind_to], students[ind_from]
    return students


def group_by_age(students: list[Student]):
    age_count = collections.Counter((s.age for s in students))
    age_to_offset = {}
    offset = 0
    for age, count in age_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:
        from_age = next(iter(age_to_offset))
        from_ind = age_to_offset[from_age]
        to_age = students[from_ind].age
        to_ind = age_to_offset[students[from_ind].age]
        students[from_ind], students[to_ind] = students[to_ind], students[from_ind]
        age_count[to_age] -= 1
        if age_count[to_age]:
            age_to_offset[to_age] += 1
        else:
            del age_to_offset[to_age]

    return students


def main():
    students = [
        Student("David", 5),
        Student("Anna", 9),
        Student("David", 5),
        Student("David", 5),
        Student("Annafd", 9),
        Student("David", 5),
        Student("Anna", 9),
        Student("Stas", 18),
        Student("Stas", 18),
        Student("Davidvfd", 5),
        Student("Davidvfd", 5),
        Student("Davidvf", 5)
    ]
    print("merged invervals {}".format(partition_sort(students)))
    #print("merged invervals {}".format(group_by_age(students)))



if __name__ == '__main__':
    main()