# calculate mean and std deviation
from pathlib import Path
import cv2
import numpy as np
from scipy import stats
from itertools import pairwise
from execitiontime import timer
from graphplot import GraphPlot
from thread import  NewThread, CustomThread
import time
import matplotlib.pyplot as plt
import timeit

@timer
def get_mean(files):
    mean = np.array([0.,0.,0.])
    numSamples = len(files)
    for i in range(numSamples):
        im = cv2.imread(str(files[i]))
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        im = im.astype(float) / 255.
        
        for j in range(3):
            mean[j] += np.mean(im[:,:,j])

    mean = (mean/numSamples)
    return mean

@timer
def get_median(files, mean):
    stdTemp = np.array([0.,0.,0.])
    std = np.array([0.,0.,0.])
    numSamples = len(files)
    for i in range(numSamples):
        im = cv2.imread(str(files[i]))
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        im = im.astype(float) / 255.
        
        for j in range(3):
            stdTemp[j] += ((im[:,:,j] - mean[j])**2).sum()/(im.shape[0]*im.shape[1])

    std = np.sqrt(stdTemp/numSamples)
    return std

@timer
def get_mode(files):
    mod = np.array([0.,0.,0.])
    numSamples = len(files)
    for i in range(numSamples):
        im = cv2.imread(str(files[i]))
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        im = im.astype(float) / 255.
        unq,count = np.unique(im.reshape(-1,im.shape[-1]), axis=0, return_counts=True)

        for j in range(3):
            mod[j] += unq[count.argmax()][j]

    return mod

def find_min(A):
    mini = float('inf')  # Initialize mini as positive infinity
    for num in A:
        if num < mini:
            mini = num
    return mini

def find_max(A):
    maxi = float('-inf')  # Initialize maxi as negative infinity
    for num in A:
        if num > maxi:
            maxi = num
    return maxi

# Brute Force
# @timer
def bruteforce(arr):
    start_time = time.time()  # Start time
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Calculate execution time
    return arr, execution_time

# Divide and Conquer
@timer
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Pairwise
# @timer
def pairwisefu(arr):
    start_time = time.time()  # Start time
    end_time = time.time()  # End time
    execution_time = end_time - start_time  # Calculate execution time
    return list(pairwise(arr)), execution_time

def main():

    imageFilesDir = Path(r'traindata')
    files = list(imageFilesDir.rglob('*.jpg'))

    mean_thread = CustomThread(target=get_mean, args=(files,)) # This is where you get your return value.p
    mean_thread.start()
    mean = mean_thread.join()

    median_thread = CustomThread(target=get_median, args=(files,mean,))
    median_thread.start()
    median = median_thread.join()

    mod_thread = CustomThread(target=get_mode, args=(files,))
    mod_thread.start()
    mod = mod_thread.join()

    print("mean: ")
    print(mean)
    print("median: ")
    print(median)
    print("modus: ")
    print(mod)

    arr = np.concatenate((mean, median, mod))
    print(arr)
    min = find_min(arr)
    print("Min: ")
    print(min)
    max = find_max(arr)
    print("Max: ")
    print(max)
    arr.sort()
    print("Sorted:", arr)

    bforce, br_esclaped = bruteforce(arr)
    print("Brute Force: ", bforce)
    print("Time Execution: ", br_esclaped)

    quick = quick_sort(arr)
    print("Divide and Conquer: ", quick)
    print("Time Execution: ", br_esclaped)

    pair, pw_esclaped = pairwisefu(arr)
    print("Pairwise: ", pair)
    print("Time Execution: ", br_esclaped)

    # Calculate and print the elapsed time
    elapsed_time = [br_esclaped,br_esclaped*2, br_esclaped]
    p1 = GraphPlot(elapsed_time) 
    p1.plotshow()


if __name__ == "__main__":
    main()
