import datetime
import subprocess
import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication

from Modules import FileHandler, ReportGenerator, HTMLToPDF, Compressing, EmailHandler
from Modules.ConfigHandler import config
from Modules.gui import Ui_MainWindow
import xml.etree.ElementTree as ET


class UserInterface(QMainWindow):

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)

		self.gui_window = Ui_MainWindow()
		self.gui_window.setupUi(self)

		self.gui_window.pushButton_exit.clicked.connect(self.zamknij)
		self.gui_window.pushButton_start.clicked.connect(self.run)
		self.gui_window.checkBox_zipfiles.stateChanged.connect(self.zipfiles_checkbox_state_changed)
		self.gui_window.checkBox_email.stateChanged.connect(self.email_checkbox_state_changed)
		self.gui_window.checkBox_zipname.stateChanged.connect(self.zipname_checkbox_state_changed)
		self.gui_window.statusBar.showMessage("Loaded and ready to go")

	@staticmethod
	def zamknij():
		sys.exit(app.exec_())

	def zipname_checkbox_state_changed(self):
		if self.gui_window.checkBox_zipname.isChecked():
			self.gui_window.lineEdit_zipname.setEnabled(True)
		else:
			self.gui_window.lineEdit_zipname.setEnabled(False)

	def zipfiles_checkbox_state_changed(self):
		if self.gui_window.checkBox_zipfiles.isChecked():
			self.gui_window.checkBox_zipname.setEnabled(True)
		else:
			self.gui_window.lineEdit_zipname.setEnabled(False)
			self.gui_window.checkBox_zipname.setEnabled(False)
			self.gui_window.checkBox_zipname.setCheckState(False)

	def email_checkbox_state_changed(self):
		if self.gui_window.checkBox_email.isChecked():
			self.gui_window.tab_2.setEnabled(True)
		else:
			self.gui_window.tab_2.setEnabled(False)

	def run(self):

		if self.gui_window.checkBox_email.isChecked():
			checkbox_email = "Yes"
		else:
			checkbox_email = "No"

		if self.gui_window.checkBox_zipfiles.isChecked():
			checkbox_zipfiles = "Yes"
		else:
			checkbox_zipfiles = "No"
		if self.gui_window.checkBox_zipname.isChecked():
			zipname = self.gui_window.lineEdit_zipname.text()
		else:
			zipname = "Yes"
		self.gui_window.pushButton_start.setEnabled(False)
		self.gui_window.pushButton_exit.setEnabled(False)
		self.gui_window.statusBar.showMessage("Started Test Suite")

		start.execute_all_funcions(self.gui_window.lineEdit_outputpath.text(),
		                           self.gui_window.lineEdit_testsuitetorun.text(),
		                           zipname,
		                           self.gui_window.lineEdit_projectxml.text(),
		                           self.gui_window.lineEdit_testrunnerbat.text(),
		                           checkbox_zipfiles,
		                           checkbox_email,
		                           self.gui_window.lineEdit_password.text(),
		                           self.gui_window.lineEdit_fromemail.text(),
		                           self.gui_window.lineEdit_toemail.text(),
		                           self.gui_window.lineEdit_smtpserver.text(),
		                           self.gui_window.lineEdit_smtpport.text())
		self.gui_window.pushButton_start.setEnabled(True)
		self.gui_window.pushButton_exit.setEnabled(True)
		self.gui_window.statusBar.showMessage("Report finished")

class ReportDefinitions(object):

	def __init__(self):
		self.file = FileHandler.FileHandler()
		self.html_parser = ReportGenerator.HTMLReportGenerator()
		self.html_to_pdf = HTMLToPDF.HTMLtoPDF()

	@staticmethod
	def take_current_time():
		return str(datetime.datetime.now()).split('.')[0]

	@staticmethod
	def start_tests_and_capture_results(testsuitetorun, soapuixmlprojectlocation, raportoutputlocation,
	                                    testrunnerbatlocation):
		"""
		FLAGS
		 a : Turns on exporting of all test results, not only errors
		 A : Turns on exporting of all results using folders instead of long
		 c : The TestCase to run, used to narrow down the tests to run
		 D : Sets system property with name=value
		 d : The domain to use in any authentications, overrides any domain set for any TestRequests
		 e : The endpoint to use when invoking test-requests, overrides the endpoint set in the project file
		 E : Sets which environment to use (SoapUI Pro only)
		 F : Sets the format of the report specified with the -R option, for Printable reports this is one of PDF, XLS, HTML, RTF, CSV, TXT, and XML. For Data Export this is either XML or CSV (SoapUI Pro only)
		 f : Specifies the root folder to which test results should be exported (see below)
		 G : Sets global property with name=value
		 g : Sets the output to include Coverage HTML reports ( SoapUI Pro only )
		 h : The host:port to use when invoking test-requests, overrides only the host part of the endpoint set in the project file
		 I : Do not stop if error occurs, ignore them: Execution does not stop if error occurs, but no detailed information about errors are stored to the log. (If you need full information about errors, do not use this option).
		 i : Enables SoapUI UI-related components, required if you use the UISupport class for prompting or displaying information
		 j : Turns on exporting of JUnit-compatible reports, see below
		 M : Creates a Test Run Log Report in XML format
		 m : Sets the maximum number of TestStep errors to save for each
		 o : Opens the generated report in a browser (SoapUI Pro only)
		 P : Sets project property with name=value, e.g. -Pendpoint=Value1 -PsomeOtherProperty=value2
		 p : The password to use in any authentications, overrides any password set for any TestRequests
		 r : Turns on printing of a small summary report (see below)
		 R : Selects which report to generate for the test objects executed, for example if running the entire project, this could specify the name of a test-suite-level report that would be generated for each TestSuite. The report is saved as specified with the -F option to the folder specified with the -f option. (SoapUI Pro only)
		 S : Sets to save the project file after tests have been run
		 s : The TestSuite to run, used to narrow down the tests to run
		 t : Sets the soapui-settings.xml file to use, required if you have custom proxy, ssl, http, etc setting
		 u : The username to use in any authentications, overrides any username set for any TestRequests
		 v : Sets password for soapui-settings.xml file
		 w : Sets the WSS password type, either 'Text' or 'Digest'
		 x : Sets project password for decryption if project is encrypted
		"""
		return subprocess.check_output(
			[testrunnerbatlocation,
			 "-a",
			 "-I",
			 "-r",
			 "-s",
			 testsuitetorun,
			 soapuixmlprojectlocation,
			 "-f",
			 raportoutputlocation]).decode("utf-8")

	def execute_all_funcions(self, output_location, testsuite_to_run, zip_autodate, soapuixmlprojectlocation,
	                         testrunnerbatlocation, zipreportfolder, sendemail, email_password, from_email, to_email,
	                         smtp_server, smtp_port):
		xml_root = ET.parse(soapuixmlprojectlocation).getroot()


		# Start time timestamp
		time_started = self.take_current_time()
		# execute tests and capture test results
		test_results = self.start_tests_and_capture_results(testsuite_to_run, soapuixmlprojectlocation,
		                                                    output_location + "\\Reports",
		                                                    testrunnerbatlocation)
		# End time timestamp
		time_ended = self.take_current_time()
		print(test_results)
		# parse results to html and save them
		final_report_in_html, table_result_metrics, non_html_table_with_test_steps = self.html_parser.start_report(
			test_results, time_started, time_ended, xml_root)
		self.file.createfile(final_report_in_html,
		                     "Html_files/html_report.html")
		# convert that html to pdf
		self.html_to_pdf.convert_html_to_pdf_file("Html_files/html_report.html",
		                                          output_location + "\\Reports" + '\\test_results.pdf')

		if sendemail == "Yes":
			EmailHandler.EmailMethods.send_mail(email_password, from_email,
			                                    to_email,
			                                    output_location + "\\Reports\\test_results.pdf", smtp_server,
			                                    smtp_port, table_result_metrics)

		if zipreportfolder == "Yes":
			Compressing.ZipFiles.file_compression(zip_autodate, output_location,
			                                      testsuite_to_run)


if __name__ == '__main__':

	start = ReportDefinitions()

	if config.guiswitch == "Yes":
		app = QApplication(sys.argv)
		UI = UserInterface()
		UI.show()
		sys.exit(app.exec_())

	else:
		start.execute_all_funcions(config.raportoutputlocation, config.testsuitetorun, config.zipwithtesttime,
		                           config.soapuixmlprojectlocation, config.testrunnerbatlocation,
		                           config.zipreportfolder, config.sendemail, config.password_email, config.from_email,
		                           config.to_email, config.smtp_server, config.smt_port)
