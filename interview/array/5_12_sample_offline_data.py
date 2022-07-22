import random

def sample_offline_data(A:list[int], k:int) -> list[int]: # O(k)
    n = len(A)
    for i in reversed(range(n - k - 1, n - 1)):
        r = random.randint(0, i)
        A[r], A[i] = A[i], A[r]
    return A[n - k:]




def main():
    A = [39, 47, 96, 59, 81, 71, 15, 11, 9, 32] # random.sample(range(1, 100), 10))
    print(sample_offline_data(A, 5))

if __name__ == '__main__':
    main()