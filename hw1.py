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
		SELECT raceId, year, round, circuitId, name, date, url
		FROM races
		WHERE year = 1950 
	"""

def query2():
	return """
		SELECT r.year, r.round, r.circuitId, r.name, r.date, c.location, c.country
		FROM races r, circuits c
		WHERE r.year = 1950
			AND c.circuitId = r.circuitId
	"""

def query3(): #is actually correct even if runner file doesn't show... modify a.name AS racename
	return """
		SELECT a.raceId, a.name, e.position, e.driverId, d.forename, d.surname, c.constructorId, c.name
		FROM races a, results e, drivers d, constructors c
		WHERE e.raceId = 42
			AND a.raceId = 42
			AND d.driverId = e.driverId
			AND c.constructorId = e.constructorId
		ORDER BY e.position
	"""
	
def query4():
	return """
		SELECT a.raceId, a.name, d.forename, d.surname, ds.position, ds.points, ds.wins
		FROM races a, drivers d, driver_standings ds
		WHERE a.raceId = 988
			AND ds.raceId = 988
			AND d.driverId = ds.driverId
		ORDER BY ds.position
	"""

def query5():
	return """
		SELECT DISTINCT a.raceId, a.name, e.position, d.forename, d.surname, c.name AS constructor, e.laps, e.milliseconds, e.statusId, s.status
		FROM races a, results e, drivers d, driver_standings ds, status s, constructors c
		WHERE e.raceId = 988
			AND a.raceId = 988
			AND ds.driverId = e.driverId
			AND ds.raceId = 988
			AND d.driverId = e.driverId
			AND s.statusId = e.statusId
			AND c.constructorId = e.constructorId
		ORDER BY e.position
	"""

def query6():
	return """
		SELECT a.raceId, a.name, c.constructorId, c.name AS constructor, cs.position, cs.points, cs.wins
		FROM races a, constructors c, constructor_standings cs
		WHERE a.raceId = 988
			AND cs.raceId = 988
			AND c.constructorId = cs.constructorId
		ORDER BY cs.position
	"""

def query7(): #very inefficient
	return """
		SELECT DISTINCT pd.forename, pd.surname, c.name AS constructor, c.nationality
		FROM results e, constructors c,
			(SELECT DISTINCT d.forename, d.surname, d.nationality, e.constructorId
			FROM drivers d, results e
			WHERE e.points >= 9
				AND e.driverId = d.driverId
			) AS pd
		WHERE e.points >= 9
			AND c.constructorId = pd.constructorId
			AND pd.nationality = c.nationality
	"""

def query8():
	return """
		SELECT DISTINCT nationality
		FROM drivers
		EXCEPT
		SELECT DISTINCT nationality
		FROM constructors
	"""

def query9():
	return """
		SELECT c.name AS constructor, SUM(e.points) AS sum_points
		FROM constructors c, results e
		WHERE e.constructorId = c.constructorId
		GROUP BY constructor
		HAVING sum_points >= 100
		ORDER BY sum_points DESC
	"""

def query10():
	return """
		SELECT c.name AS constructor, a.year, SUM(e.points) AS sum_points
		FROM constructors c, results e, races a
		WHERE e.constructorId = c.constructorId
			AND e.raceId = a.raceId
		GROUP BY constructor, a.year
		HAVING sum_points >= 100
	"""

def query11():
	return """
		SELECT c.name AS constructor, a.year, SUM(e.points)
		FROM results e, races a,
			(SELECT DISTINCT constructorId, name
			FROM constructors
			WHERE name = "Ferrari")
			AS c
		WHERE e.constructorId = c.constructorId
			AND e.raceId = a.raceId
		GROUP BY a.year
	"""

def query12():
	return """
		SELECT d1.forename AS d1_forname, d1.surname AS d1_surname, d2.forename AS d2_forname, d2.surname AS d2_surname, d2.nationality
		FROM drivers d1
		INNER JOIN drivers d2
		ON d1.surname = d2.surname
			AND d1.nationality = d2.nationality
			AND d1.driverId < d2.driverId
	"""

def query13():
	return """
		SELECT d1.forename, d1.surname, d1.nationality
		FROM drivers d1
		INNER JOIN drivers d2
		ON d1.surname = d2.surname
			AND d1.nationality = d2.nationality
			AND d1.driverId <> d2.driverId
		GROUP BY d1.nationality, d1.surname, d1.forename
	"""

def query14():
	return """
		SELECT DISTINCT r.raceId, r.year, r.name, r.date, COALESCE(COUNT(DISTINCT e.driverId), 0) AS cnt
		FROM
			(SELECT DISTINCT raceId, year, name, date
			FROM races) AS r
		LEFT JOIN results e
		ON r.raceId = e.raceId
		GROUP BY r.raceId
		HAVING cnt <= 15
		ORDER BY cnt
	"""

def query15():
	return """
		SELECT d.driverId, d.forename, d.surname, d.dob, d.nationality
		FROM drivers d,
			(SELECT e.driverId
			FROM status s, results e
			WHERE s.status LIKE "Fuel leak"
				AND e.statusId = s.statusId
			INTERSECT
			SELECT e.driverId
			FROM status s, results e
			WHERE s.status LIKE "Water pipe"
				AND e.statusId = s.statusId
			) AS s
		WHERE d.driverId = s.driverId
		LIMIT 5
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
