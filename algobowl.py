#!/usr/bin/python

import sys

def main(argv):
    # num_tasks, num_machs, proc_times, speeds = get_inputs(argv)
    inputs = get_inputs(argv)
    greedy_method(inputs)

def greedy_method(inputs):
    # solves problem based on the greedy method

    num_tasks, num_machs, proc_times, speeds = inputs

    processes = [[] for i in range(num_machs)] # array to hold the processes assigned to each machine
    times = [0 for i in range(num_machs)] # array to hold the process time for each machine

    for proc, proc_time in enumerate(proc_times):
        processes, times = greedy_choice(proc, proc_time, times, processes, speeds)

    print_results(processes, times)

def greedy_choice(proc, proc_time, times, processes, speeds):
    # makes single choice for greedy method

    for mach, speed in enumerate(speeds):
        # i is machine no., speed is i's speed

        times[mach] += speed * proc_time
        diff = max(times) - min(times)

        if mach == 0:
            min_diff = diff
            best_choice = mach
        else:
            if diff < min_diff:
                min_diff = diff
                best_choice = mach

        times[mach] -= speed * proc_time

    speed = speeds[best_choice]

    processes[best_choice] += [proc]
    times[best_choice] += speed * proc_time

    return processes, times

def get_inputs(argv):
    infile = argv[0]
    with open(infile) as f:
        inputs = [line.strip() for line in f]

    inputs = [int(param) if i < 2 else param.split(' ') for i, param in
            enumerate(inputs)]

    for i, param in enumerate(inputs):
        if i > 1:
            inputs[i] = [int(x) for x in param]

    return inputs

def print_results(processes, times):
    for mach in processes:
        print(' '.join(str(proc) for proc in mach))

    print(min(times))


if __name__ == "__main__":
    main(sys.argv[1:])
