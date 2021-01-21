from abc import ABC, abstractmethod


class Element(ABC):

	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)

	def __set__(self, obj, value):
		value = self.parser(value)
		setattr(obj, self.private_name, value)

	@abstractmethod
	def parser(self, value):
		pass
