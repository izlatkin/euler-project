def balanced_brace_combinations(k):
    in_progress = [(k, "", 0)]
    while in_progress:
        n = len(in_progress)
        for _ in range(n):
            tmp = in_progress[0]
            if tmp[0] == 0 and tmp[2] == 0:
                print(tmp[1])
            else:
                if tmp[0] > tmp[2]:
                    in_progress.append((tmp[0] - 1, tmp[1] + '(', tmp[2] + 1))
                if tmp[2] > 0:
                    in_progress.append((tmp[0] - 1, tmp[1] + ')', tmp[2] - 1))
            in_progress.remove(tmp)



# Driver code
if __name__ == '__main__':
    balanced_brace_combinations(6)