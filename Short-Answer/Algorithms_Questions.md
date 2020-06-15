# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n): // O(n * n)/2
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies): 
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
1 : 2 -> 3 -> 4 t'wil never reach 0
## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

given:
  n-story building
  n = number of stories, p = current floor, f = point of inflection

  n > f egg breaks
  n < f egg does not break

  
