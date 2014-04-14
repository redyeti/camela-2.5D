from collections import Mapping

class ConfigItem(Mapping):
	"""
	Config adapter object. Input works like an object with
	attributes, output works like a dict.
	"""

	def __init__(self):
		super.__setattr__(self, "_ConfigItem__data", {})

	def __setattr__(self, k, v):
		self.__data[k] = v

	def __getitem__(self, k):
		return self.__data[k]

	def __len__(self):
		return len(self.__data)

	def __iter__(self):
		return iter(self.__data)

