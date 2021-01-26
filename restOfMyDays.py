# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

class Solution:
    def toLowerCase(self, str: str) -> str:
        lowerCase = str.lower()
        return lowerCase

# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #use reverse method to reverse the list
        s.reverse()

# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        reversedWords=[]
        listOfWords= s.split()
        print(listOfWords)
        for word in listOfWords:
            print("This is word", word)
            reversedWords.append(word[::-1])
        
        
        print("This is reversed words", reversedWords)
        return " ".join(reversedWords)

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = []
        for num in nums:
            if num not in single_number:
                single_number.append(num)
            else:
                single_number.remove(num)
        return single_number[0]


