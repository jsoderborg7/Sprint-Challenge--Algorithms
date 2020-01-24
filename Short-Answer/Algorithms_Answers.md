#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is O(n^3). The runtime is proportional to n cubed in this part:  while (a < n * n * n):


b) This is O(n(log(n))). The first half:  for i in range(n):  is O(n), but the second half:  while j < n:  is O(log(n))
                                            j = 1                                              j *= 2
                                                                                                 sum += 1
                                          

c) This is O(n). Because it is recursive, there is only one more call for each decreasing value, making it a linear function.

## Exercise II

I think a binary search would be the most efficient way to solve this.

We would start with determining the middle floor of the set

We would then drop an egg from the middle floor, and see if it breaks

If it breaks, we know that the safe floor is in the lower half of floors, with the highest floor then being set at the floor just below the current. 

If it does not break, we know that the safe floor is in the upper half, with the lowest floor then becoming the floor just above the current.

For this exercise, I'm goint to assume the egg breaks, and I know that the safe floor is in the lower half.

So I would take the middle floor of the new range (lowest floor to the highest which is now the floor just below the initial drop floor) and drop the egg from there to see if it breaks.

The loop repeats itself until we find the one safe floor, with each pass determining if the safe floor is higher or lower than the current floor.

By doing a binary search, we minimize the number of eggs needed to drop in order to determine the safe floor.


