def schedule_to_minize_waiting_time(service_times: list[int]):
    service_times.sort()
    total_time = 0
    n = len(service_times)
    for i, service_time in enumerate(service_times):
        total_time += service_time * (n - i - 1)
    return total_time



def main():
    print(schedule_to_minize_waiting_time([2, 5, 1, 3]))


if __name__ == '__main__':
    main()