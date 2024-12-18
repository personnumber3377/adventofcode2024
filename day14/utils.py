
INT_SCAN_SEP_STRING = "INTEGER"

def integer_scan(template, actual_string) -> list[int]: # This function basically applies an integer scan.
	assert INT_SCAN_SEP_STRING in template
	string_stuff = template.split(INT_SCAN_SEP_STRING)
	lengths = [len(x) for x in string_stuff]
	cur_idx = 0
	for length in lengths:
		cur_idx 

