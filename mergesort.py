class MergeSort:
    """MergeSort Class"""

    def __init__(self):
        # constructor
        self._aux = []

    # Main entry point to sort
    def sort(self, mergeable):
        """sort method"""
        self._populate_aux_initially(mergeable)
        self._sort(mergeable, 0, len(mergeable) - 1)

    def _populate_aux_initially(self, mergeable) -> None:
        """method to populate aux array"""
        self._aux = [None for i in range(len(mergeable))]

    def _sort(self, mergeable, low, high):
        """recursive sort method"""
        if high <= low:
            return
        mid = low + int((high - low) / 2)
        self._sort(mergeable, low, mid)
        self._sort(mergeable, mid + 1, high)
        self._merge(mergeable, low, mid, high)

    def _merge(self, mergeable, low, mid, high):
        """merge method"""
        self._copy_from_main_to_aux(mergeable, low, high)
        self._merge_from_aux_to_main(mergeable, low, mid, high)
        return

    def _copy_from_main_to_aux(self, mergeable, low, high) -> None:
        """method to copy from main array to aux"""
        for k in range(low, high + 1):
            self._aux[k] = mergeable[k]

    def _merge_from_aux_to_main(self, mergeable, low, mid, high) -> None:
        """method to merge from aux to main"""
        i = low
        j = mid + 1
        for k in range(low, high + 1):
            if i > mid:  # Index past left subarray max index
                mergeable[k] = self._aux[j]
                j += 1
            elif j > high:  # index past right subarray max index
                mergeable[k] = self._aux[i]
                i += 1
            elif self._aux[j] < self._aux[i]:  # compare
                mergeable[k] = self._aux[j]
                j += 1
            else:
                mergeable[k] = self._aux[i]
                i += 1
