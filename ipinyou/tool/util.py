import sys
from tqdm import tqdm

def enum(gen, start=1, loop=100000):
	for i, x in enumerate(gen, start=start):
		if i == 1 or i % loop == 0:
			print("\033[K" + str(i), end='\r', flush=True, file=sys.stderr)
		yield i, x
	print("\033[K" + str(i), file=sys.stderr)

def lrange(start, end, buffer_size=100000, progress_bar=False):
	if progress_bar:
		with tqdm(total=end-start, dynamic_ncols=True) as pb:
			for l in range(start, end, buffer_size):
				r = min(l + buffer_size, end)
				yield l, r
				pb.update(r - l)
	else:
		for l in range(start, end, buffer_size):
			yield l, min(l + buffer_size, end)