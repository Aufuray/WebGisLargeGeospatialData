import json
outFile = open('out1.txt','w+')

outFile.write('[\n')
outFile.write('\t{\n')
outFile.write('\t\t"name": "GBIF",\n')
outFile.write('\t\t"parent": "null",\n')
outFile.write('\t\t"children": [\n')


lastkingdom 	= ''
lastphylum 	= ''
lastclass 	= ''
lastorder 	= ''
lastfamily 	= ''
lastgenus 	= ''

linecount = 0

with open ('new_gbif_taxon.txt', 'r') as file:
	for line in file:
		if line.endswith('\n'):
			line = line[:-1]
		splitLine = line.split(',')
		if len(splitLine) == 8:
			linecount += 1

			kingdom = splitLine[0]
			phylum  = splitLine[1]
			_class  = splitLine[2]
			order   = splitLine[3]
			family  = splitLine[4]
			genus   = splitLine[5]
			specie  = splitLine[6]
			taxoid  = splitLine[7]

			closedKingdom 	= False
			closedPhylum 	= False
			closedClass		= False
			closedOrder		= False
			closedFamily	= False
			closedGenus		= False
			tab = 1

			if genus != lastgenus and linecount != 1:
				outFile.write('{}\n'.format(']'))
				outFile.write('{}{}\n'.format('\t'*6, '}'))	
				closedGenus = True
				tab = 6

			if family != lastfamily and linecount != 1:
				# close family
				outFile.write('{}{}\n'.format('\t'*5, ']'))
				outFile.write('{}{}\n'.format('\t'*4, '}'))
				closedFamily = True
				tab = 4

			if order != lastorder and linecount != 1:
				#close genus
				outFile.write('{}{}\n'.format('\t'*4, ']'))
				outFile.write('{}{}\n'.format('\t'*3, '}'))
				closedOrder = True
				tab = 3
			

			if _class != lastclass and linecount != 1:
				outFile.write('{}{}\n'.format('\t'*3, ']'))
				outFile.write('{}{}\n'.format('\t'*2, '}'))
				closedClass = True
				tab = 2

			if phylum != lastphylum and linecount != 1:
				outFile.write('{}{}\n'.format('\t'*2, ']'))
				outFile.write('{}{}\n'.format('\t'*1, '}'))
				closedPhylum = True

			if kingdom != lastkingdom and linecount != 1:
				outFile.write('{}{}\n'.format('\t'*2, ']'))
				outFile.write('{}{}\n'.format('\t'*1, '}'))
				closedKingdom = True

			if closedKingdom == True or closedPhylum == True or closedClass == True or closedOrder == True or closedFamily == True or closedGenus == True:
				outFile.write('{}{}\n'.format('\t'*tab, ','))
			


			if kingdom != lastkingdom:
				outFile.write('{}{}\n'.format('\t'*2,'{'))
				outFile.write('{}"name": "{}",\n'.format('\t'*2,kingdom))
				outFile.write('{}"parent": "{}",\n'.format('\t'*2,'GBIF'))
				outFile.write('{}"children": {}\n'.format('\t'*2,'['))				


			if phylum != lastphylum:
				outFile.write('{}{}\n'.format('\t'*2,'{'))
				outFile.write('{}"name": "{}",\n'.format('\t'*2,phylum))
				outFile.write('{}"parent": "{}",\n'.format('\t'*2,kingdom))
				outFile.write('{}"children": {}\n'.format('\t'*2,'['))		
			

			if _class != lastclass:
				outFile.write('{}{}\n'.format('\t'*2,'{'))
				outFile.write('{}"name": "{}",\n'.format('\t'*2,_class))
				outFile.write('{}"parent": "{}",\n'.format('\t'*2,phylum))
				outFile.write('{}"children": {}\n'.format('\t'*2,'['))			



			if order != lastorder:
				outFile.write('{}{}\n'.format('\t'*3,'{'))
				outFile.write('{}"name": "{}",\n'.format('\t'*3,order))
				outFile.write('{}"parent": "{}",\n'.format('\t'*3,_class))
				outFile.write('{}"children": {}\n'.format('\t'*3,'['))


			if family != lastfamily:
				outFile.write('{}{}\n'.format('\t'*4,'{'))
				outFile.write('{}"name": "{}",\n'.format('\t'*4,family))
				outFile.write('{}"parent": "{}",\n'.format('\t'*4,order))
				outFile.write('{}"children": {}\n'.format('\t'*4,'['))			


			if genus != lastgenus:
				outFile.write('{}{}\n'.format('\t'*5,'{'))
				outFile.write('{}"name": "{}",\n'.format('\t'*5,genus))
				outFile.write('{}"parent": "{}",\n'.format('\t'*5,family))
				outFile.write('{}"children": {}\n'.format('\t'*5,'['))

			specieTaxoid = '{},{}'.format(specie, taxoid)
			outFile.write('{}{}\n'.format('\t'*6,'{'))
			outFile.write('{}"name": "{}",\n'.format('\t'*6,specieTaxoid))
			outFile.write('{}"parent": "{}"\n'.format('\t'*6,genus))
			outFile.write('{}{},'.format('\t'*6,'}'))


			lastkingdom 	= kingdom
			lastphylum 	= phylum
			lastclass 	= _class
			lastorder 	= order
			lastfamily 	= family
			lastgenus 	= genus




	#close genus
	outFile.write('{}\n'.format(']'))
	outFile.write('{}{}\n'.format('\t'*3, '}'))
	# close family
	outFile.write('{}{}\n'.format('\t'*3, ']'))
	outFile.write('{}{}\n'.format('\t'*2, '}'))
	# close order
	outFile.write('{}{}\n'.format('\t'*2, ']'))
	outFile.write('\t{}\n'.format('}'))
	# close class
	outFile.write('\t{}\n'.format(']'))
	outFile.write('{}\n'.format('}'))	
	# close pyhum
	outFile.write('\t{}\n'.format(']'))
	outFile.write('{}\n'.format('}'))	

	# close kingdom
	outFile.write('\t{}\n'.format(']'))
	outFile.write('{}\n'.format('}'))

	# close GBIF elem
	outFile.write('\t{}\n'.format(']'))
	outFile.write('{}\n'.format('}'))

	#close JSON root elem
	outFile.write('\t{}\n'.format(']'))


outFile.close()

# json formatted readable version
out = open('out2.txt','w+')
with open('out1.txt') as file:
	for line in file:
		if '},]' in line:
			line = '\t\t\t\t\t\t}]\n'
		out.write(line)
out.close()

# remove special chars from json
out = open('gbif.json', 'w+')
with open('out2.txt') as file:
	for line in file:
		line = line.strip('\t')
		line = line.strip('\n')

		out.write(line)

out.close()





