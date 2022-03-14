### Pysquare-Finder
finds the square root of an specific number using vanilla python

### Calculations
To get the square root of a not exact number you need to do: <br>
`(X + Y) / √(Y) * 2` <br> 
Example: <br>
To get the square root of √(634): <- not exact<br>
1. get the radicand of √(634), add the radicand of the closest exact square root (625)
2. divide by the square root of the closest exact square root and multiply by two
You should have something like: <br>
```
634 + 625
--------- = 25.18
 25 * 2
```

### Note
The code isnt 100% clean! It have a specific bug that: <br>
- really close square numbers are automatically rounded, e.g: square of 15 shows as 4.0, but in reality it is 3.87

 ### How it works
 **Exact Square Roots**
 1. first uses a `for` loop in range of 1 to the specified number.
 2. checks if one of the checked values on the loop multiplied by himself is the specified value
 3. if it is, just tell you!
 4. 
 **Not Exact Square Roots**
 1. first subtracts the n.e square roots with the range of the amount to be checked
 2. if in the range that you specified in bforce has a exact square root, pick the closest exact square root
 3. re-verify if its really an exact square root
 4. if it is, do the calcs
