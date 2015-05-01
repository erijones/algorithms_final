#!/usr/bin/python

import sys
import random as rand
import time

def main(argv):
    inputs = get_inputs(argv)

    processes, times = greedy_method(inputs)
    print("greedy min distance:")
    print_results(processes, times)
    print("")
    if inputs[0] > inputs[1]:
        print("top swapper min distance:")
        processes, times = top_swapper(processes, times, inputs)
        print_results(processes, times)
    else:
        print("Number of machines is greater than number of tasks; greedy algorithm will suffice")

def top_swapper(processes, times, inputs):
    # run the top swapper a bunch of times
    tic = time.time()
    num_swaps = 1000000
    for i in range(num_swaps):
        processes, times = top_swapper_once(processes, times, inputs)
    toc = time.time()
    print("time run: ", toc-tic, "s; # swaps: ", num_swaps)
    return processes, times

def top_swapper_once(processes, times, inputs):
    num_tasks, num_machs, proc_times, speeds = inputs
    # highest is mach with largest time; high_elem is the random element
    # selected from that mach
    highest = times.index(max(times))
    high_elem = rand.randint(0, len(processes[highest])-1)

    # swappee is randomly selected mach; swappee_elem is same as above
    swappee = rand.randint(0, len(times)-1)
    swap_elem = rand.randint(0, len(processes[swappee])-1)

    # check relative distances
    before_diff = times[highest] - times[swappee]
    after_high_time = times[highest] \
        - (proc_times[processes[highest][high_elem]] / speeds[highest]) \
        + (proc_times[processes[swappee][swap_elem]] / speeds[highest])
    after_swap_time = times[swappee] \
        + (proc_times[processes[highest][high_elem]] / speeds[swappee]) \
        - (proc_times[processes[swappee][swap_elem]] / speeds[swappee])
    after_diff = abs(after_high_time - after_swap_time)

    #print(before_diff, after_diff)

    # swap if beneficial
    if before_diff <= after_diff:
        return processes, times
    else:
        temp_high = processes[highest].pop(high_elem)
        temp_swap = processes[swappee].pop(swap_elem)
        processes[highest].append(temp_swap)
        processes[swappee].append(temp_high)
        times[highest] = after_high_time
        times[swappee] = after_swap_time
        return processes, times

    return processes, times

def greedy_method(inputs):
    # solves problem based on the greedy method

    num_tasks, num_machs, proc_times, speeds = inputs

    processes = [[] for i in range(num_machs)] # array to hold the processes assigned to each machine
    times = [0 for i in range(num_machs)] # array to hold the process time for each machine

    for proc, proc_time in enumerate(proc_times):
        # proc is the process number, proc_time is the process time

        # make a greedy choice for every process
        processes, times = greedy_choice(proc, proc_time, times, processes, speeds)

    #print_results(processes, times)
    return processes, times

def greedy_choice(proc, proc_time, times, processes, speeds):
    # makes single choice for greedy method

    for mach, speed in enumerate(speeds):
        # i is machine no., speed is i's speed

        times[mach] += proc_time / speed
        diff = max(times) - min(times)

        # check if the current machine choice is the best choice so far
        if mach == 0: # first machine, must be the best choice so far
            min_diff = diff
            best_choice = mach
        else:
            if diff < min_diff:
                min_diff = diff
                best_choice = mach

        # go back to the original process times so that we can test the next
        # machine
        times[mach] -= proc_time / speed

    # get the speed of the machine we've chosen
    speed = speeds[best_choice]

    # update the machine we've chosen with the process
    processes[best_choice] += [proc]
    # add the time that this process adds to the chosen machine's total time
    times[best_choice] += proc_time / speed

    return processes, times

def get_inputs(argv):
    infile = argv[0]

    with open(infile) as f:
        inputs = [line.strip() for line in f]

    inputs = [int(param) if i < 2 else param.split(' ')
              for i, param in enumerate(inputs)]

    for i, param in enumerate(inputs):
        if i > 1:
            inputs[i] = [int(x) for x in param]

    return inputs

def print_results(processes, times):
    f = open('out_file.txt', 'w')
    for mach in processes:
        print(' '.join(str(proc) for proc in mach))
        f.write(' '.join(str(proc) for proc in mach))
        f.write('\n')

    print(max(times))
    f.write(str(max(times))) 


if __name__ == "__main__":
    main(sys.argv[1:])
