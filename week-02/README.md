We need to find the number of contiguous substrings in the given string that starts and ends with the same letter.

For this we do not need to check every substring as that will create a time complexity of O(n^2). So at first, we find the frequency of each letter in the string and then apply the formula freq*(freq+1)//2. Adding the result of this formula for all distinct letters in the string gives the total number of contiguous substrings starting and ending with the same letter.

Time complexity here is O(n) because we are only traversing over all the letters in the string once.