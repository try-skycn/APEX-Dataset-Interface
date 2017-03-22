import json, numpy as np
from h5py import File

class CTRLoader:
	def __init__(self, datafile):
		self._f_ = File(datafile)
		self._sizes_ = self.meta("sizes")
		self.unified_size = int(np.sum(self._sizes_[1:]))
		self._offset_ = np.array([np.sum(self._sizes_[1:i+1]) for i, _ in enumerate(self._sizes_[1:], start=1)], dtype=int)
	
	def meta(self, key):
		return json.loads(self._f_.attrs[key])
	
	def _line_generator_(self, dsetname, loop_times):
		for i in range(loop_times):
			for line in self._f_[dsetname]:
				yield line
	
	def data_generator(self, dsetname, batch_size, unified_index=True, loop_times=1):
		generator = self._line_generator_(dsetname, loop_times)
		while True:
			inputs, labels = np.zeros((batch_size, len(self._sizes_[1:])), dtype=int), np.zeros((batch_size, ), dtype=int)
			for i, line in zip(range(batch_size), generator):
				inputs[i], labels[i] = line[1:], line[0]
			if i < batch_size - 1: break
			if unified_index: inputs = inputs + self._offset_
			yield inputs, labels
