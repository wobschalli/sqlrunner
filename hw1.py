# Use this file to write your queries. Submit this file to Gradescope after finishing your homework.

# To verify your submission is in the correct format: `python3 hw1.py`

# Make sure the program prints out your SQL statements correctly. That means the autograder will read you SQL correctly. 

# Running the Python file will not execute your SQL statements, it simply prints them. You can test your SQL statements in your own SQL environment.

# Please only edit the parts that say `Your code here` and do not edit anything else. 

instr = '''Instructions:
	Please put the queries under the corresponding functions below.
	Running this python file will check if the formatting is okay.
	Example:
		def query1():
			return """
				SELECT * FROM agent
			"""
'''

def query1():
	return """
		SELECT raceId, year, round, circuitId, name, date, url FROM races WHERE year = 1950 
	"""

def query2():
	return """
		-- Your code here
	"""

def query3():
	return """
		-- Your code here
	"""
	
def query4():
	return """
		-- Your code here
	"""

def query5():
	return """
		-- Your code here
	"""

def query6():
	return """
		-- Your code here
	"""

def query7():
	return """
		-- Your code here
	"""

def query8():
	return """
		-- Your code here
	"""

def query9():
	return """
		-- Your code here
	"""

def query10():
	return """
		-- Your code here
	"""

def query11():
	return """
		-- Your code here
	"""

def query12():
	return """
		-- Your code here
	"""

def query13():
	return """
		-- Your code here
	"""

def query14():
	return """
		-- Your code here
	"""

def query15():
	return """
		-- Your code here
	"""

# Do not edit below

if __name__ == "__main__":
	try:
		if all(type(eval(f'print(t:=query{f+1}()),t')[1])==str for f in range(15)):
			print(f'Your submission is valid.')
		else:
			raise TypeError('Invalid Return Types.')
	except Exception as e:
		print(f'Your submission is invalid.\n{instr}\n{e}')
