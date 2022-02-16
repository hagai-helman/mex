class MexFinder:
    """This class collects non-negative integers, and finds the minimal
    non-negative integer that was not added to it.
    """
    def __init__(self):
        # We maintain a dict, representing a set, with the following
        # invariants:
        # (a) Its keys are the elements of the set (and -1, see below);
        # (b) For any maximal sequence of consecutive elements, the first
        #     one is mapped to last one, and vice-versa.
        #
        # The key (-1) is mapped to 0, so when an element is added, we
        # don't need to give special treatment to the special case when
        # this element is 0.
        self._d = {-1: 0}

    def add(self, n):
        """Adds a number to the collection.

        `n` is assumed to be a non-negative integer.
        """
        if n in self._d:
            return

        # We make sure `n` is in `self._d`.
        self._d[n] = n

        # We find the first element (`left`) and the last element (`right`) of
        # the maximal sequence of consecutive elements that contains `n`.
        left = self._d.get(n - 1, n)
        right = self._d.get(n + 1, n)

        # We make sure `left` and `right` are mapped to each other.
        self._d[left] = right
        self._d[right] = left

    def mex(self):
        """Returns the minimal non-negative integer excluded from the set."""
        if 0 not in self._d:
            return 0
        else:
            return self._d[0] + 1
        

def mex(values):
    """Finds the minimal non-negative integer excluded from a given iterable
    of non-negative integers."""
    finder = MexFinder()
    for value in values:
        finder.add(value)
    return finder.mex()
