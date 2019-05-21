import configparser


class ConfigHandler(object):
	def __init__(self):
		config_parse = configparser.ConfigParser()
		config_parse.read("config.cfg")
		self.guiswitch = config_parse.get("configuration", "GUI")
		self.testrunnerbatlocation = config_parse.get("configuration", "testrunnerbatlocation")
		self.testsuitetorun = config_parse.get("configuration", "TestSuiteToRun")
		self.soapuixmlprojectlocation = config_parse.get("configuration", "SOAPUIXMLProjectLocation")
		self.raportoutputlocation = config_parse.get("configuration", "RaportOutputLocation")
		self.zipreportfolder = config_parse.get("configuration", "ZipAllReports")
		self.zipwithtesttime = config_parse.get("configuration", "ZipWithTestTime")
		self.sendemail = config_parse.get("configuration", "SendEmail")
		self.from_email = config_parse.get("email_settings", "From_email")
		self.password_email = config_parse.get("email_settings", "Password_email")
		self.to_email = config_parse.get("email_settings", "To_email")
		self.smtp_server = config_parse.get("email_settings", "SMTP_server")
		self.smt_port = config_parse.get("email_settings", "SMTP_port")


config = ConfigHandler()
