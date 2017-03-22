from apexdsets._util_ import loader, miscell

__all__ = ["CTRLoader"]

_default_path_ = miscell.datapath("criteo")

def CTRLoader(loader.CTRLoader):
	def __init__(self, datapath=_default_path_):
		super(CTRLoader, self).__init__(datapath)
