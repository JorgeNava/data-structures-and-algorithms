"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
  Every close bracket has a corresponding open bracket of the same type.

  Example 1:
  Input: s = "()"
  Output: true

  Example 2:
  Input: s = "()[]{}"
  Output: true

  Example 3:
  Input: s = "(]"
  Output: false
"""
def isValidString(s):
	"""
		We can use a stack to order the chars to know which char most be closed first
    The higher their are at the stack the higher priority to be closed they have
    If a char is closed that doesnt correspond to the one with higher priority then return False
		
		Iterate through the string's characters
    For each character:
			if its an open char then:
				Push into stack
			else:
        compare last char type with actChar
        if the same:
					pop the last char
				if not:
					return false
	"""
	output = True
	openChars = ['(','[','{']
	closeChars = [')',']','}']
	stack = []

	for char in s:
		if char in openChars:
			stack.append(char)
		elif char in closeChars:
			if len(stack) == 0: 
				output = False
				break
			if char == ')':
				separtionBetweenOpenAndClosingChars = 1
			else:
				separtionBetweenOpenAndClosingChars = 2
			if chr(ord(char) - separtionBetweenOpenAndClosingChars) == stack[-1]:
					stack.pop()
			else:
				output = False
	if len(stack) != 0: output = False
	return output

tests = [
	{
		"s": "()",
		"expectedOutput": True
	},
	{
		"s": "()[]{}",
		"expectedOutput": True
	},
	{
		"s": "(]",
		"expectedOutput": False
	},
	{
		"s": "[",
		"expectedOutput": False
	},
	{
		"s": "]",
		"expectedOutput": False
	},
]
for test in tests:
	output = isValidString(test["s"])
	print('output',output)
	print('>', output == test["expectedOutput"])