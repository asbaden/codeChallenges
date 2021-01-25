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

