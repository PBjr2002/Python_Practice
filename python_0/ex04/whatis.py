import argparse

class NewParser(argparse.ArgumentParser):
	def error(self, message):
		if "unrecognized arguments" in message:
			raise AssertionError("more than one argument is provided")
		elif "invalid int value" in message:
			raise AssertionError("argument is not an integer")
		elif "the following arguments are required" in message:
			self.exit(2)
		else:
			self.exit(2, f"Error: {message}\n")

try:
    parser = NewParser()
    parser.add_argument("integer", type=int, help="Number to verify if even/odd")
    args = parser.parse_args()
    n = args.integer
    if n % 2 == 0:
    	print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as error:
	print(f"AssertionError: {error}")
