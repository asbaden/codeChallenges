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

# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #sort the array so we know where the biggest numbers are 
        nums.sort()
        print("THIS IS NUMS", nums)
        #return the output of multiplying the two biggest numbers where both are subtracted by 1
        return (nums[-1]-1) * (nums[-2]-1)

# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        #create two empty arrays 
        even=[]
        odd=[]
        #iterate through the list of numbers checking if even or odd, appending to appropriate list
        for num in A:
            if (num%2)==0:
                even.append(num)
            else:
                odd.append(num)
        for num in odd:
            even.append(num)
        return even


