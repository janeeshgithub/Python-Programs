# Print all subsets if there is at least one subset of set[]
# with a sum equal to the given sum
flag = False

def print_subset_sum(i, n, _set, target_sum, subset):
	global flag
	# If targetSum is zero, then there exists a subset
	if target_sum == 0:
		# Prints valid subset
		flag = True
		print("[", end=" ")
		for element in subset:
			print(element, end=" ")
		print("]", end=" ")
		return

	if i == n:
		# Return if we have reached the end of the array
		return

	# Not considering the current element
	print_subset_sum(i + 1, n, _set, target_sum, subset)

	# Consider the current element if it is less than or equal to targetSum
	if _set[i] <= target_sum:
		# Push the current element into the subset
		subset.append(_set[i])

		# Recursive call for considering the current element
		print_subset_sum(i + 1, n, _set, target_sum - _set[i], subset)

		# Remove the last element after recursive call to restore subset's original configuration
		subset.pop()

if __name__ == "__main__":

	set_1 = list(map(int,input().split()))
	sum_1 = int(input())
	n_1 = len(set_1)
	subset_1 = []
	print("Output 1:")
	print_subset_sum(0, n_1, set_1, sum_1, subset_1)
