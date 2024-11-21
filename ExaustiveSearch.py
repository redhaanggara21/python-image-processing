# Python code for the above approach
def maxPackedSets(items, sets):

	# Initialize the maximum number of sets that can be packed to 0
	maxSets = 0

	# Loop through all the sets
	for set in sets:
		# Initialize the number of sets that can be packed to 0
		numSets = 0

		# Loop through all the items
		for item in items:
			# Check if the current item is in the current set
			if item in set:
				# If the item is in the set, increment 
				# the number of sets that can be packed
				numSets += 1

				# Remove the item from the set of items, 
				# so that it is not counted again
				items = [i for i in items if i != item]

		# Update the maximum number of sets that can be packed
		maxSets = max(maxSets, numSets)

	return maxSets

# Set of items
items = [1, 2, 3, 4, 5, 6]

# List of sets
sets = [
	[1, 2, 3],
	[4, 5],
	[5, 6],
	[1, 4]
]

# Find the maximum number of sets that 
# can be packed into the given set of items
maxSets = maxPackedSets(items, sets)

# Print the result
print(f"Maximum number of sets that can be packed: {maxSets}")

# This code is contributed by Potta Lokesh
