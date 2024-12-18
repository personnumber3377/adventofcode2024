





'''

This function tries to give general integral solutions to the system of equations:

x1*a + x2*b = K1
x1*c + x2*d = K2

Using the diophantine equation.

'''

from math import gcd
import sys

'''
def extended_euclidean_algorithm(a,b,c):
	# Solves the euclidean algorithm a*x + b*y = c

	# First transform this into a = b*q + r where q is the quotient and r is the remainder...

	a_remaining = a
	b_current = b
	quotient_list = []
	remainder = 1
	while remainder != 0:
		quotient = a_remaining // b_current
		quotient_list.append(quotient)
		remainder = a_remaining % b_current
		assert quotient*b_current + remainder + a_remaining
		a_remaining = b_current
		b_current = remainder


		print("="*100)
		print(a_remaining)
		print(quotient)
		#print(b_current)
		#print(remainder)
	x0 = a_remaining
	y0 = quotient
	assert c % gcd(a,b) == 0
	scale_factor = c / gcd(a,b)

	x0_scaled = x0 * scale_factor
	y0_scaled = y0 * scale_factor
	print(x0_scaled)
	print(y0_scaled)
	assert x0_scaled*a + y0_scaled*b == c
	return
'''





A_PRICE = 3
B_PRICE = 1

def extended_euclidean_algorithm(a,b,c):
	# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Description

	r0, r1 = a, b
	s0, s1 = 1, 0
	t0, t1 = 0, 1

	# The computation stops when one reaches a remainder  r_(k+1){\displaystyle r_{k+1}} which is zero; the greatest common divisor is then the last non zero remainder 	r	k	.	{\displaystyle r_{k}.}
	while r1 != 0:
		q = r0 // r1
		r0, r1 = r1, r0 - q*r1
		s0, s1 = s1, s0 - q*s1
		t0, t1 = t1, t0 - q*t1

	# Ok, so now I think that the gcd is in r0 because r1 is now zero.
	# Return the scaled versions
	k = c//r0# // r0
	if c % r0 != 0:
		print("FUCK!"*1000)
		exit(1)
	s0 *= k
	t0 *= k

	s0 = (s0 % b + b) % b  # Ensures s0 is in [0, b)
	t0 = (c - a * s0) // b  # Recalculate t0 using the modified s0
	if (c - a * s0) % b != 0:
		print("FUCK!"*100)
		exit(1)
	# Make coefficients nonnegative (if desired)
	# Adjust s0 modulo b to be nonnegative
	return r0, s0, t0 # r0 is gcd, s0 and t0 are the coefficients




BUT_SEP = "Button A: "
LEN_BUT_SEP = len(BUT_SEP)

PRIZE_SEP = "Prize: "
LEN_PRIZE_SEP = len(PRIZE_SEP)

def solve(x1, x2, a, b, c, d, K1, K2):
	# The first equation is x1*a + x*2*b = K1 , if the gcd(a,b) does not divide K1, then no solution exists...
	if gcd(a,b) % K1 != 0:
		return None # No solutions automatically.



def solve_system(d_red_x, d_blue_x, K_x, d_red_y, d_blue_y, K_y):
	
	# extended_euclidean_algorithm

	# Check for infinite solutions...
	if d_red_x*d_blue_y - d_blue_x*d_red_y == 0:
		print("Infinite solutions..."*1)
		print("Values:")
		print(d_red_x, d_blue_x, K_x, d_red_y, d_blue_y, K_y)
		print("="*30)
		exit(1)
		return None
		#exit(1)
	else:
		print("Finite solutions...")
	# The first equation on our list is just  the x coordinates.
	print("Print passing this stuff:")
	print(d_red_x)
	print(d_blue_x)
	print(K_x)
	if K_x % gcd(d_red_x, d_blue_x) != 0 or K_y % gcd(d_red_y, d_blue_y) != 0:
		print("Shitfuck"*100)
		return None # No solution
	initial_solution = extended_euclidean_algorithm(d_red_x, d_blue_x, K_x)
	gcd_thing, x0, y0 = initial_solution[0], initial_solution[1], initial_solution[2]
	assert gcd_thing == gcd(d_red_x,d_blue_x)
	#assert x0 >= 0 and y0 >= 0
	# Now initial_solution[0] is gcd and initial_solution[1] is x0 and initial_solution[2] is y0. These are already scaled, so no need to scale them here.
	assert d_red_x*x0 + d_blue_x*y0 == K_x
	# Check if there actually is a solution. If RHS % gcd != 0 then no solution exists

	

	# Now calculate the t thing. This can be used to calculate the bullshit.
	# We basically solved the first equation and then substituted the parameterized solution to the bottom equation and just solved for the parameter t (https://math.stackexchange.com/questions/2018981/how-do-you-solve-diophantine-equations-using-euclidean-algorithm)
	
	# We need to do this bullshit because reasons...

	if (d_blue_x*d_red_y) % gcd_thing != 0 or (d_red_x*d_blue_y) % gcd_thing != 0 or (K_y - x0*d_red_y-y0*d_blue_y) % ((((d_blue_x*d_red_y)//gcd_thing)-((d_red_x*d_blue_y)//gcd_thing))) != 0:
		print("Fuckooofffff")
		return None


	t = (K_y - x0*d_red_y-y0*d_blue_y)//(((d_blue_x*d_red_y)//gcd_thing)-((d_red_x*d_blue_y)//gcd_thing))
	print("t: "+str(t))
	# Now calculate the actual solution for the thing...

	# Notice that x = x0 + t*d_blue_x/gcd_thing

	print("x0: "+str(x0))
	print("y0: "+str(y0))
	'''
	if x0 == 0 or y0 == 0:
		print("fefe")
		#exit(0)
		if x0 > 100 or y0 > 100:
			return None
		return x0, y0
	'''
	actual_x = x0 + t*(d_blue_x//gcd_thing)
	actual_y = y0 - t*(d_red_x//gcd_thing)
	assert d_red_x*x0 + d_blue_x*y0 == K_x
	#assert d_red_y*x0 + d_blue_y*y0 == K_y
	assert d_red_x*actual_x + d_blue_x*actual_y == K_x

	print("Here is the actual_x: "+str(actual_x))
	print("Here is the actual_y: "+str(actual_y))

	#if actual_x < 0 or actual_y < 0: # Sanity checking..
	#	return None

	# Check for the hundred shit:
	'''
	if actual_x > 100 or actual_y > 100:
		print("poopoo")
		exit(0)
		return None
	'''
	assert d_red_y*actual_x + d_blue_y*actual_y == K_y
	return (actual_x, actual_y)










def get_machines(machines_strings) -> list: # Returns the tuples which describe this machine.
	# This assumes that the stuff is in the format.
	a_shit, b_shit, prize = machines_strings
	a_shit = a_shit[LEN_BUT_SEP:]
	b_shit = b_shit[LEN_BUT_SEP:]
	prize = prize[LEN_PRIZE_SEP:]
	a_shit, b_shit, prize = [int(x[2:]) for x in a_shit.split(", ")], [int(x[2:]) for x in b_shit.split(", ")], [int(x[2:]) for x in prize.split(", ")]
	return a_shit, b_shit, prize

def solve_machines(machines_strings_list):
	tot = 0
	specific_index = 1 # [specific_index:specific_index+1]
	for machines_strings in machines_strings_list: # machines_strings_list[:1]: # Just run the first thing...
		print("Running this:")
		print("".join(machines_strings))
		a_shit, b_shit, prize = get_machines(machines_strings)
		# Ok, so now we have the parameters. Time to just pass to the solve function.

		d_red_x, d_red_y = a_shit # red is basically A
		d_blue_x, d_blue_y = b_shit

		K_x, K_y = prize # The right hand side in our equations...

		K_x += 10000000000000
		K_y += 10000000000000

		# Now we basically have the equation shit, so it is time to actually solve the system of diophantine equations...

		solution = solve_system(d_red_x, d_blue_x, K_x, d_red_y, d_blue_y, K_y)
		sol_bruteforce = bruteforce_solve(d_red_x, d_blue_x, K_x, d_red_y, d_blue_y, K_y)
		'''
		if solution != sol_bruteforce: # Mismatch. A bug.
			print("Bruteforced solution: "+str(sol_bruteforce))
			print("Our solution: "+str(solution))
			x_red, x_blue = solution
			print("x_red * d_red_x + x_blue * d_blue_x == "+str(x_red * d_red_x + x_blue * d_blue_x))
			print("K_x: "+str(K_x))
			print("x_red*d_red_y + x_blue * d_blue_y == "+str(x_red*d_red_y + x_blue * d_blue_y))
			print("K_y: "+str(K_y))
			exit(1)
		'''
		if solution == None:
			continue # No solutions, just ignore.
		# We have the solution. Just add the solution
		x_amount, y_amount = solution # x amount is basically red and y is blue.
		tot += x_amount * A_PRICE + y_amount * B_PRICE
	return tot



def bruteforce_solve(d_red_x, d_blue_x, K_x, d_red_y, d_blue_y, K_y):
	for x_red in range(101):
		for x_blue in range(101):
			if x_red * d_red_x + x_blue * d_blue_x == K_x and x_red*d_red_y + x_blue * d_blue_y == K_y:
				return (x_red, x_blue)
	return None




def main() -> int: # Main function...
	
	if len(sys.argv) != 2:
		print("Usage: "+str(sys.argv[0])+" INPUTFILE")
		return 1

	fh = open(sys.argv[1], "r")
	lines = fh.readlines()
	fh.close()

	# Split every four lines...
	n = 4
	machines = [lines[i:i+n-1] for i in range(0, len(lines), n)] # -1 because we don't want the empty lines in our stuff.
	print(machines)

	actual_thing = solve_machines(machines)
	print(actual_thing)

	return 0


if __name__=="__main__":

	ret = main()

	exit(ret)
