def cap_payroll(salaries: list[int], target: int):
    salaries.sort(reverse=True)
    summa = sum(salaries)
    if sum(salaries) < target:
        print("Nothing to cat")
    if target / len(salaries) < salaries[-1]:
        print("Everybody cat")
        return target / len(salaries)
    print(salaries)
    for i, p in enumerate(salaries):
        summa -= p
        if salaries[i + 1] < (target - summa) / (i + 1) < p:
            result = (target - summa) / (i + 1)
            print([result] * (i + 1) + salaries[i+1:])
            return result


def main():
    salaries = [90, 30, 100, 40, 20]
    target = 210
    print(cap_payroll(salaries, target))
    print(cap_payroll(salaries, 50))



if __name__ == '__main__':
    main()