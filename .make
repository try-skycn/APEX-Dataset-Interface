#!/usr/bin/env python3

dsetlist = ["ipinyou"]

nasdir = input("Where is your NAS directory?\n(default /NAS/) >>> ")

if nasdir == "":
	nasdir = "/NAS/"

import os.paht
datasetdir = os.path.join(nasdir, "Dataset", "Ads", "APEXDatasets")

import subprocess
def softlink_dataset(dsetname):
	filepath = os.path.realpath(os.path.join(datasetdir, dsetname, "data"))
	subpath = os.path.realpath(os.path.join(".", dsetname, "data"))
	subprocess.run(["ln", "-s", filepath, subpath])

for dsetname in dsetlist:
	softlink_dataset(dsetname)

