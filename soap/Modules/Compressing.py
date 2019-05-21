import os
import time
import zipfile


class ZipFiles(object):

	@staticmethod
	def file_compression(zipname, folderpath, testsuitename):
		"""
		Compresses specified folder and it contents to a zip
		:param zipname: Name of the archive to be created
		:param folderpath: Specify folderpath what to compress
		:param testsuitename: Test suite name for zip name
		:return: staticmethod
		"""
		if zipname == 'Yes':
			zipname = "{} at {}.zip".format(testsuitename, time.strftime("%Y%m%d%H%M%S"))
		zf = zipfile.ZipFile(folderpath + "\\" + zipname, "w", zipfile.ZIP_DEFLATED)
		for folder, subfolders, files in os.walk(folderpath + "\\Reports"):
			for fieli in files:
				zf.write(os.path.join(folder, fieli), os.path.relpath(os.path.join(folder, fieli), folderpath + "\\Reports"))
		zf.close()
		print("Created zipfile: " + zipname)
