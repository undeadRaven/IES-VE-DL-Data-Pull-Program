#Defining key to use as line indicator:
key1 = "Analysis calculation for room -"
with open('Inputfile.txt') as fi:
    lines = fi.readlines()

#Finding relevant lines (that incorporate DL results) and inserting them into a new list

relevant = [i for (i, item) in enumerate(lines) if item.startswith(key1)]
out1 = []
for r in relevant:
    for offset in -2, 6, 10, 11:
        index = r + offset
        if 0 < index < len(lines):
        	out1.append(lines[index])

# Finding relevant values in filtered lines from the list "out1"

out2 = []	
for line in out1:
	if line.startswith("Room"):
		out2.append(line[5:])
	elif line.startswith("Working"):
		out2.append(line[38:42]+"\n")
	elif line.startswith("Area"):
		if line[6] ==".":
			out2.append(line[5:10]+"\n")
		elif line[7] ==".":
			out2.append(line[5:11]+"\n")
	elif line.startswith("Margin"):
		if line[25]== "1":
			out2.append("1\n")
		else:
			out2.append(line[25:29]+ "\n")

# Moving results to single line. Every set of four lines are concatenated, 
# making it easy to paste into spreadsheet program and separate using ";" deliminator

out3=[]
count = 1
for line in out2:
	line=line.rstrip()
	line.replace(" ","")
	if count ==1:
		concatenated_line = line
		count+=1
	elif count == 2 or count == 3:
		concatenated_line += ";" + line
		count +=1
	elif count == 4:
		concatenated_line += ";" + line
		count -=3
		out3.append(concatenated_line+"\n")

with open('Outputfile.txt', 'w') as fi:
    fi.writelines(out3)
