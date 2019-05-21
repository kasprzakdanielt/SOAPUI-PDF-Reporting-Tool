

class FileHandler(object):

	def createfile(self, content_to_save, filename):
		"""

		:param content_to_save:
		:param filename:
		:return:
		"""
		current_file = open(filename, "w")
		current_file.write(content_to_save)
		current_file.close()
