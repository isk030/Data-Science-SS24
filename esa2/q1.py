import numpy as np
import time


def sorted_indices_without_numpy(lst):
    if not lst:
        raise ValueError("list is empty")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("list has non-numeric elements")

    return sorted((k[0] for k in enumerate(lst)), key=lambda x: lst[x])


def sorted_indices_with_numpy(lst):
    if not lst:
        raise ValueError("list is empty")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("list has non-numeric elements")

    return np.argsort(lst)


# Test Code
list1 = [23, 104, 5, 190, 8, 7, -3]
list2 = []
rng = np.random.default_rng(3)
list3 = np.random.randint(0, 10, 1000000).tolist()

print("list1 test")
start_time = time.time()
indices1 = sorted_indices_without_numpy(list1)
print("indices of sorted elements without numpy:", indices1)
print("time taken without numpy:", time.time() - start_time)

start_time = time.time()
indices2 = sorted_indices_with_numpy(list1)
print("indices of sorted elements with numpy:", indices2)
print("time taken with numpy:", time.time() - start_time)

print("#" * 40)
print("list3 test")
start_time = time.time()
indices5 = sorted_indices_without_numpy(list3)
print("indices of sorted elements without numpy:", np.array(indices5))
print("time taken without numpy:", time.time() - start_time)

start_time = time.time()
indices6 = sorted_indices_with_numpy(list3)
print("indices of sorted elements with numpy:", indices6)
print("time taken with numpy:", time.time() - start_time)

print("#" * 40)
print("list2 test")
start_time = time.time()
indices3 = sorted_indices_without_numpy(list2)
print("indices of sorted elements without numpy:", indices3)
print("time taken without numpy:", time.time() - start_time)

start_time = time.time()
indices4 = sorted_indices_with_numpy(list2)
print("indices of sorted elements with numpy:", indices4)
print("time taken with numpy:", time.time() - start_time)
