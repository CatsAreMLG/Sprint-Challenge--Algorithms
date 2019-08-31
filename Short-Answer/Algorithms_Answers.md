#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This problem is O(n) because while the while loop shows it would be n^3 `n * n * n`, a increases by n^2
making the solution iterate O(n) times.

b) This problem is O(n^2) because the while loop is n/2 but here you assume it scales worse as it gets bigger so you make it n
and that is in a for loop of n iterations making this a O(n^2) solution.

c) This problem is O(n) because the recursion only iterates by 1 each time down to 0 meaning this solution only can iterate O(n) times

## Exercise II

Here I would start by going through n and throwing an egg at each floor testing to see if it breaks then returning the floor it broke at,
this at worst is `thrown+broken=n`. This solution is O(n), here is my psuedocode:

```
  For each floor of n  #O(n)
    if thrown egg equals broken egg  #O(1)
      return current floor n
```
