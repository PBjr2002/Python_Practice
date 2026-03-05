import argparse

class NewParser(argparse.ArgumentParser):
	def error(self, message):
		if "unrecognized arguments" in message:
			self.exit(2, "AssertionError: more than one argument is provided\n")
		elif "invalid int value" in message:
			self.exit(2, "AssertionError: argument is not an integer\n")
		elif "the following arguments are required" in message:
			self.exit(2)
		else:
			self.exit(2, f"Error: {message}\n")

parser = NewParser()
parser.add_argument("integer", type=int, help="Number to verify if even/odd")
args = parser.parse_args()
n = args.integer

if n % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")
