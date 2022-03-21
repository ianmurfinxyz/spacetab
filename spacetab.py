################################################################################
# project: spacetab
# author: Ian Murfin - github.com/ianmurfinxyz
# brief: Converts space indents to tab indents in code files.
################################################################################

import sys
import io
import math

help_msg = """
Usage: spacetab [OPTION] ... FILE [FILE ...]

Converts space indents to tab indents in FILE.

	I once was blind but now I see.
	Tabs are all that must be!
	To the world of space sinners I donate to thee.
	A script of forgiveness, by a tab devotee.

OPTIONS:
	-c	Number of space to compress into a single tab.
	-h	Show this help message.
"""

arg_count = len(sys.argv)

if arg_count < 1:
	print("ERROR: expected at least 1 file argument.")
	exit(-1)

tab_width = 2

for arg in sys.argv:
	if arg == "-h":
		print(help_msg)
		exit(0)

count_index = -1
for index, arg in enumerate(sys.argv):
	if arg == "-c":
		count_index = index
		break

if count_index + 1 >= arg_count:
	print("ERROR: expected integer argument after -c switch.")

if count_index != -1:
	tab_width = int(sys.argv[count_index + 1])

filenames = []
for index, arg in enumerate(sys.argv):
	if index == 0: continue
	if index == count_index: continue
	if index == count_index + 1: continue
	filenames += [arg]

for filename in filenames:
	file = io.open(filename, 'r')
	old_lines = file.readlines()
	file.close()

	new_lines = []
	for old_line in old_lines:

		space_count = 0
		for c in old_line:
			if c == ' ': space_count += 1
			else: break

		surplus_space_count = space_count % 2
		tab_count = int(math.floor(space_count / 2))
		new_line = ['\t' for i in range(tab_count)]
		new_line += [' ' for i in range(surplus_space_count)]

		stripped_old_line = old_line.lstrip()
		if len(stripped_old_line) == 0:
			new_lines += old_line
		else:
			new_line += stripped_old_line
			new_lines += new_line

	file = io.open(filename, 'w')
	file.writelines(new_lines)
	file.close()
