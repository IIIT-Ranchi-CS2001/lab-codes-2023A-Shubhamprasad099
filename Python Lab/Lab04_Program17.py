#                                                                             Program 17

# Generate 2 lists (course code and course name). create a new list with both course code and name like["CS1001:Python",...]

course_codes = ["CS1001", "CS1002", "CS1003", "CS1004"]
course_names = ["Python", "TOC", "Algorithms", "Maths"] 
print([code + ":" + name for code, name in zip(course_codes, course_names)])

