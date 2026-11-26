"""
Assessment 3.7: Sorting Algorithms
Sorting method: Insertion Sort

ALGORITHM
1. Start with the full name as a string.
2. Convert it to lowercase.
3. Go through each character:
   - skip it if it is not a letter (spaces and symbols are excluded)
   - skip it if it is already in the array (duplicates are discarded)
   - otherwise, add it to the unsorted array
4. Copy the unsorted array to a new array (so the original stays unsorted).
5. Insertion Sort:
   a. Treat the first element as the sorted part.
   b. Take the next element (the "key").
   c. Compare the key with the elements on its left; shift each larger
      element one position to the right.
   d. Insert the key into the gap.
   e. Repeat for every remaining element.
6. Print the unsorted array and the sorted array.
"""


def build_letter_array(full_name):
    """Return a list of unique letters (no spaces, no symbols) in order of appearance."""
    letters = []
    for ch in full_name.lower():
        if not ch.isalpha():      # exclude spaces / symbols
            continue
        if ch in letters:         # discard duplicate letters
            continue
        letters.append(ch)
    return letters


def insertion_sort(arr):
    """Sort a list in ascending order using Insertion Sort (returns a new list)."""
    result = arr[:]               # copy so the unsorted array is preserved
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def main():
    full_name = "james stephen canoy"

    unsorted_array = build_letter_array(full_name)
    sorted_array = insertion_sort(unsorted_array)

    print("Full name:      ", full_name)
    print("Unsorted array: ", unsorted_array)
    print("Sorted array:   ", sorted_array)


if __name__ == "__main__":
    main()