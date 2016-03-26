MAP REDUCE

3 parts are in this folder.

 MathStats:
  Runs through all numbers in the "numbers.txt" file and finds statistics for it.
  Going through all data only once.
  Returns Total(sum) , Average(mean), Standard Deviation(std) and Count

 Primes:
  Mapfn runs through a database of values and finds all the Primes
  Sends these key value pairs to reducefn

  Reduce runs through the primes and checks for palindrome.
  Which then returns all the palindrome primes from 2 -> given number.
  (need to change the given number to 10mil
  <line 6 col 19 of primes.py to wanted number>)

 Passcheck:
  
