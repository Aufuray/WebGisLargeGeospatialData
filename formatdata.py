formattedFile = 'new_gbif_taxon.txt'
writeFile = open(formattedFile, 'w')

origFileLines = 0
newFileLines = 0

with open ('gbif_taxon.txt', 'r') as largeFile:
	for line in largeFile:
		origFileLines += 1
		if ('\N' in line):
			continue
		else:
			writeFile.write(line)
			newFileLines +=1

		# if origFileLines >= 20:
		# 	break

print 'Old File Line Num:', origFileLines
print 'New File Line Num', newFileLines
print 'Line Diff', origFileLines-newFileLines