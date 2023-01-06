def print_combo(combo, heading = "valid combo"):
	twos, threes, sum = combo
	print(heading + "\ttwos:" + str(twos) \
                                + "\tthrees:" + str(threes) + "\tsum:" + str(sum)) 


def find_point_combos(total_points = 8, print_combos = True):
	max_twos = int(total_points / 2)
	max_threes = int(total_points / 3)
	combinations = 0
	for twos in range(0,max_twos+1):
		for threes in range(0,max_threes+1):
			sum = 2*twos + 3*threes
			if sum == total_points:
				valid = (twos, threes, sum)
				if print_combos:
					print_combo(valid)
				combinations = combinations + 1
	return combinations

solution = find_point_combos(8)
print("combinations for 8:" + str(solution))
solution = find_point_combos(60)
print("combinations for 60:" + str(solution))
solution_60 = solution
search_start = 61
search_end = 1024
for i in range(search_start, search_end+1):
	solution = find_point_combos(i, False)
	if solution <= solution_60:
		print("found:\t"+str(i)+" with only:\t"+str(solution)+" combinations.")
	if solution < solution_60:
		print(str(i) + " combinations:")
		find_point_combos(i, True)
