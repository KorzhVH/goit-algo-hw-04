import timsort, insertion, merge
import timeit, random
import pandas as pd

arr10 = [random.randint(1, 100) for _ in range(10)]
arr1000 = [random.randint(1, 100) for _ in range(1000)]
arr10000 = [random.randint(1, 100) for _ in range(10000)]


ins10 = timeit.timeit('insertion.insertion_sort(arr10)', globals=globals(), number=100)
ins1000 = timeit.timeit('insertion.insertion_sort(arr1000)', globals=globals(), number=100)
ins10000 = timeit.timeit('insertion.insertion_sort(arr10000)', globals=globals(), number=100)

merge10 = timeit.timeit('merge.mergeSort(arr10)', globals=globals(), number=100)
merge1000 = timeit.timeit('merge.mergeSort(arr1000)', globals=globals(), number=100)
merge10000 = timeit.timeit('merge.mergeSort(arr10000)', globals=globals(), number=100)

tims10 = timeit.timeit('timsort.tim_sort(arr10)', globals=globals(), number=100)
tims1000 = timeit.timeit('timsort.tim_sort(arr1000)', globals=globals(), number=100)
tims10000 = timeit.timeit('timsort.tim_sort(arr10000)', globals=globals(), number=100)

results = {
    "Array length": [10, 1000, 10000],
    'insertion_sort': [ins10, ins1000, ins10000],
    'merge_sort': [merge10, merge1000, merge10000],
    'timsort': [tims10, tims1000, tims10000]

}

df = pd.DataFrame(results)

print(df)