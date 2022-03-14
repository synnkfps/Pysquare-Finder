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

