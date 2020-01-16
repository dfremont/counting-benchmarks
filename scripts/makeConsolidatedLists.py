import os

benchmarkListName = 'benchmarkList.txt'

benchmarkLists = {}

for currentPath, directories, files, in os.walk('.', topdown=False):
	# find lists one level down
	sublists = []
	directories.sort()
	for dname in directories:
		dirPath = os.path.join(currentPath, dname)
		if dirPath in benchmarkLists:
			sublists.extend(os.path.join(dname, bench) for bench in benchmarkLists[dirPath])
	# if any lists found, write out; otherwise search for list at this level
	if len(sublists) > 0:
		benchmarkLists[currentPath] = sublists
		f = open(os.path.join(currentPath, benchmarkListName), 'w')
		f.writelines(sublists)
		f.close()
	else:
		for fname in files:
			if fname == benchmarkListName:
				listPath = os.path.join(currentPath, fname)
				f = open(listPath, 'r')
				benchmarks = f.readlines()
				f.close()
				benchmarkLists[currentPath] = benchmarks
				break

