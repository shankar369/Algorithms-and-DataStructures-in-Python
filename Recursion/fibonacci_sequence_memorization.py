# calculate nth fibonacci number and comparing both iterative and recursive approach
import time


def iterative_approach(n):
    if(n <= 1):
        return n
    i = 2
    f1, f2, f = 0, 1, 0
    while(i <= n):
        f = f1+f2
        f1, f2 = f2, f
        i += 1
    return f


def recursive_memorization_approach(n):
    if(n <= 1):
        return n
    if(n in memory):
        return memory[n]

    memory[n] = recursive_memorization_approach(
        n-1)+recursive_memorization_approach(n-2)

    return memory[n]


if __name__ == "__main__":
    memory = {}
    n = int(input("Enter the value of n : "))
    start_time = time.time()
    nv = iterative_approach(n)
    end_time = time.time()
    print("iterative approach took ", end_time-start_time,
          " seconds", "\nnth fibonacci number is : ", nv)
    start_time = time.time()
    nv = recursive_memorization_approach(n)
    end_time = time.time()
    print("recursive approach took ", end_time-start_time,
          " seconds", "\nnth fibonacci number is : ", nv)
