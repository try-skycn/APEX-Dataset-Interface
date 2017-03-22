from os.path import realpath, dirname, join

def _naspath_():
	with open(join(dirname(dirname(realpath(__file__))), ".naspath"), "r") as f:
		return f.read().strip()

def datapath(dataname):
	return join(_naspath_(), "Dataset", "Ads", "APEXDatasets", dataname)
