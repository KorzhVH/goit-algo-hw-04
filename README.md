Here is the results I received.
   Array length  insertion_sort  merge_sort   timsort
0            10        0.000103    0.000775  0.000145
1          1000        0.028794    0.136583  0.075446
2         10000        2.154436    1.649208  1.268324

As can be seen insertion_sort is effective on arrays of 10 and 1000 length. But on 10000 it gets exponentially higher.
The reason for that is because insertion sort, having less steps to do, is always more effective when there is less data to sort.
But with big amounts of data, it is always easier to apply the insertion_sort to smaller arrays (min_run) and then merge them.
Seeing as the difference with 10s and 1000s are miliseconds, it can be neglected.

As for merge_sort, it is always slower then timsort, because there is never a need to reach minimal elements.

Therefore timsort is the most effective.
