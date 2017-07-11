The number should be in the range of [1, n], so we just scan each number once and when we see a valid number at its appropriate position, move to the next one.

A[A[i]-1] == A[i] checks if a number is at the supposed index or not. 

If it is not at its right position, swap with the number with the one that current at that spot.

After that, scan the array again to find the first one that does not match with its index, it will be the one we are looking for.
