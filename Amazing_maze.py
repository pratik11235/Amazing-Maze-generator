#----------------------------------------------------------#
# Author: Pratik Antoni Patekar | Student id: 1001937948   #
#----------------------------------------------------------#
# Language: Python (v3.10.5) | OS tested on: Windows 11    #
#----------------------------------------------------------#
# Submission date: 04/20/2023                              #
#----------------------------------------------------------#

#------- IMPORTANT NOTE REGRADING THE GOTO FUNCTIONALITY -------#
# Python implementation of the given code required conversion   #
# of the GOTO functionality to Python function call. In the     #
# following code, for implementing the same, I have used        #
# a function "visit" (which is a sub function of generate_maze  #
# function) and called it recursively to avoid the use of       #
# while or do while loop.                                       #
#---------------------------------------------------------------#

# import the required packages
import random

# Function: find_direction
# This function is a helper function for generate_maze function.
# This function basically return the 1,2,3 or 4 depending on the
# possible directions. x and y are current coordinates and 
# nx and ny are next x and y coordinates.
def find_direction(x,y,nx,ny):
	# down : 1, up : 2, left : 3, right : 4 
	if x - nx == 0: # up or down direction
		if y - ny == 1:
			return 2 # return up
		else:
			return 1 # return down
	else: # left or right direction 
		if x - nx == 1: 
			return 3 # return left
		else:
			return 4 # return right

# Function: generate_maze
# This function generates the two matrices that are necessary for 
# generating the maze i.e. W and V as per the given "AMAZING" code
# in BASIC language.
# The matrix W contains the paths that are possible from the source
# to destination.
# The matrix V contains the directions in which the paths are possible.
# For eg. if below is a given maze then
# SOURCE
#   |
#   V 
# .  .--.--.--.
# |        |  |
# :--:--:  :  .
# |     |  |  |
# :  :  :  :  .
# |  |        |
# .--.--.  .--.
#         ^
#         | 
#     DESTINATION
#  
# W = [	[1 2 3 8]	# indicates paths starting from 1
#  		[8 7 4 7]
#  		[9 6 5 6]]
# V = [	[4 4 1 0]   # indicates directions using 1,2,3,4
#  		[1 3 1 2]
#  		[0 2 4 2]]
def generate_maze(width, height):
	# Initialize the W and V matrix with zeros
	W = [[0 for x in range(width)] for y in range(height)]
	V = [[0 for x in range(width)] for y in range(height)]
	
	# Function: visit
	# This is a recursive function call that basically performs the logic
	# same as the one represented in the lines 195 to 980.
	# As this is a recursive function call, this code is in fewer lines
	# This function bbasically modifies the W array and marks the paths 
	# by assigning values to elements in the W array as and when it explores
	# that particular cell. 
	# Each element of matrix V is assigned the value corresponding to the 
	# direction as mentioned in the functionfind_direction 
	def visit(x, y, c):
		W[y][x] = c # line 195
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		random.shuffle(directions) 
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if nx < 0 or ny < 0 or nx >= width or ny >= height:
				continue
			if W[ny][nx] != 0:
				continue
			V[y][x] = find_direction(x,y,nx,ny)
			# make a recursive call to itself
			visit(nx, ny, c + 1)
	
	# initial call to visit function as per line 195 in BASIC code
	x = random.randint(0, width - 1)
	visit(x, 0, 1)
	
	return W, V # return the computed W and V matrix

# Function: print_maze
# This function prints the maze using the W and V matrix. 
# This function is an adaptation and not the exact represntation of
# how the given BASIC code prints the maze. 
def print_maze(W, V):
	# print the first horizontal wall of the maze with entry point
	# corresponding to the "1" in W array
	start_point = W[0].index(1)
	print(".",end="")
	for i in range(len(W[0])):
		if i == start_point:
			print("  ",end="")
		else:
			print("--",end="")
		print(".",end="")
	print("\n",end="")

	# print the middle part of the maze
	for i in range(len(W)):
		#printing the line with vertical walls
		print("|  ", end="") #print leftmost vertical wall 
		for j in range(1,len(W[0])):
			# check if there is any possible movement in
			# left or right direction. If possible then
			# print "   " else "|  "
			if abs(W[i][j-1] - W[i][j]) == 1:
				print("   ",end="")
			else:
				print("|  ",end="")
		print("|") # print rightmost vertical wall

		#printing the lines with horizontal walls
		if i != len(W) - 1:
			for j in range(len(W[0])):
				# check if there is any motion possible in
				# upward or downward direction
				# if possible then print ":  " else ":--" 
				if abs(W[i+1][j] - W[i][j]) == 1:
					print(":  ",end="")
				else:
					print(":--",end="")
			print(".")

	# printing the last horizontal wall of the maze
	# the end point can be any possible position, therefore 
	# randomly choosing the endpoint.
	end_point = W[len(W)-1].index(max(W[len(W)-1]))
	print(".",end="")
	for i in range(len(W[0])):
		if i == end_point:
			print("  ",end="")
		else:
			print("--",end="")
		print(".",end="")
	print("\n",end="")

# Function: main
# This function basically takes inputs from user and calls the required functions
# with appropriate inputs. 
def main():
	print("\n\n\n\t\t\t\t  AMAZING PROGRAM")
	print("\t\t    CREATIVE COMPUTING MORRISTOWN, NEW JERSEY")
	print("(Output is the Python adaptation of the above mentioned source by Pratik Antoni Patekar)\n\n\n")
	print("Enter the width and height of the maze.")
	# take inputs from the user
	try:
		[in1,in2] = input("WHAT ARE YOUR WIDTH AND LENGTH? ").split(",")
		in1 = int(in1)
		in2 = int(in2)
	except: # if inputs are invalid then exit execution
		print("ERROR: Please enter comma seperated values.")
		return
	# call the generate_maze function to generate the W and V array
	W, V = generate_maze(in1,in2)
	# print the maze using W and V arrays
	print_maze(W,V)
	print("OK")

main()