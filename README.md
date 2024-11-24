My professor proposed that a merge sort algorithm can benefit from multiprocessing to increase its speed.
He opined that the benefit of multiprocessing in the result of faster execution time would only be apparent if the array to merge sort was large.
The overhead of spinning up multiple processes would outweigh the benefits on arrays under a certain size.

The purpose of this program is to apply multiprocessing to a merge sort algorithm and to analyze whether it is faster than a traditional algorithm.
If the multiprocess algorithm is faster, is it always faster or at what point does it become faster?