# Python3 program to find the length
# of the longest substring without
# repeating characters

# This function returns true if all
# characters in str[i..j] are
# distinct, otherwise returns false


def areDistinct(str, i, j):

	# Note : Default values in visited are false
	visited = [0] * (256)

	for k in range(i, j + 1):
		if (visited[ord(str[k])] == True):
			return False

		visited[ord(str[k])] = True

	return True

# Returns length of the longest substring
# with all distinct characters.


def longestUniqueSubsttr(str):

	n = len(str)

	# Result
	res = 0

	for i in range(n):
		for j in range(i, n):
			if (areDistinct(str, i, j)):
				res = max(res, j - i + 1)

	return res


# Driver code
if __name__ == '__main__':

	str = "geeksforgeeks"
	print("The input is ", str)

	len = longestUniqueSubsttr(str)
	print("The length of the longest "
		"non-repeating character substring is ", len)

# This code is contributed by mohit kumar 29
 
