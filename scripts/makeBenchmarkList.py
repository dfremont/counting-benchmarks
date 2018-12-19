import os

benchmarkListName = 'benchmarkList.txt'
benchmarkExtensions = ['.cnf', '.dimacs']
compressionExtensions = ['.gz']

def isABenchmark(filename):
	for ext in compressionExtensions:
		if filename.endswith(ext):
			newLen = len(filename) - len(ext)
			filename = filename[:newLen]
			break
	for ext in benchmarkExtensions:
		if filename.endswith(ext):
			return True
	return False

benchmarkPaths = {}

for currentPath, directories, files, in os.walk('.'):
	for f in files:
		if isABenchmark(f):
			benchPath = os.path.normpath(os.path.join(currentPath, f))
			if f in benchmarkPaths:
				oldPath = benchmarkPaths[f]
				print('WARNING: skipping duplicate!\nnew: %s\nold: %s' % (benchPath, oldPath))
			else:
				benchmarkPaths[f] = benchPath

sortedPaths = list(benchmarkPaths.values())
sortedPaths.sort()

listFile = open(benchmarkListName, 'w')

for path in sortedPaths:
	listFile.write(path)
	listFile.write('\n')

listFile.close()

