#!/usr/bin/env python3

dsetlist = ["ipinyou"]

try:
	nasdir = input("Where is your NAS directory?\n(default /NAS/) >>> ")
except KeyboardInterrupt:
	print("Exit.")
	exit(0)

if nasdir == "":
	nasdir = "/NAS/"

import os.path
datasetdir = os.path.join(nasdir, "Dataset", "Ads", "APEXDatasets")

import subprocess
def softlink_dataset(dsetname):
	filepath = os.path.realpath(os.path.join(datasetdir, dsetname, "data"))
	subpath = os.path.realpath(os.path.join(".", dsetname, "data"))
	subprocess.run(["ln", "-s", filepath, subpath])

for dsetname in dsetlist:
	softlink_dataset(dsetname)

