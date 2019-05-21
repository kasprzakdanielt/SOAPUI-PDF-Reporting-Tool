from pylab import *


class HTMLReportGenerator(object):
	payload_converted_to_list = None
	raw_output = None

	def start_report(self, payload, time_started, time_ended, xml_root):
		"""
		:param payload: Catched output from a testrunner.bat
		:param time_started: Timestamp when test suite started
		:param time_ended: Timestamp when test suite ended
		:return: final_report_in_html, table_result_metrics, non_html_table_with_test_steps
		"""
		self.raw_output = payload
		self.payload_converted_to_list = payload.split("\n")
		self.xml_root = xml_root
		return self.create_body(time_started, time_ended)

	def create_table_with_metrics(self, time_started, time_ended):

		dynamic_content = '<tr><td><img src="clock.png" alt=" " height=auto width=auto>   Time started</td><td>{}</td></tr><tr><td><img src="clock.png" alt=" " height=auto width=auto>   Time ended</td><td>{}</td></tr>'.format(
			time_started, time_ended)
		static_tags = ['<img src="clock.png" alt=" " height=auto width=auto>   Time taken',
		               '<img src="clipboard-symbol.png" alt=" " height=auto width=auto>   Total Test Suites',
		               '<img src="clipboard-symbol.png" alt=" " height=auto width=2auto>   Total Test Cases',
		               '<img src="clipboard-symbol.png" alt=" " height=auto width=auto>   Total Test Steps',
		               '<img src="clipboard-symbol.png" alt=" " height=auto width=auto>    Total Request Assertions',
		               '<img src="clipboard-symbol.png" alt=" " height=auto width=auto>    Total Failed Assertions',
		               '<img src="clipboard-symbol.png" alt=" " height=auto width=auto>   Total Exported Results']
		regexes = [r"Time Taken: (\d{1,}..)",
		           r"Total TestSuites: (\d{1,})",
		           r"Total TestCases: (\d+ .*)",
		           r"Total TestSteps: (\d+)",
		           r"Total Request Assertions: (\d+)",
		           r"Total Failed Assertions: (\d+)",
		           r"Total Exported Results: (\d+)"]

		for i in range(len(regexes)):
			z = re.search(regexes[i], self.raw_output)
			dynamic_content += "<tr><td>{}</td><td>{}</td></tr>".format(static_tags[i], z.group(1))

		table_content = "<tr><th>Result Metrics</th></tr>{}".format(dynamic_content)
		table_with_metrics = '<table id="t01">{}</table>'.format(table_content)

		return table_with_metrics

	def create_table_with_test_steps(self):
		lista = self.payload_converted_to_list
		non_html_table_with_test_steps = []
		dynamic_content = ""

		for line in lista:
			z = re.match(
				r"(?P<time>\d\d:\d\d:\d\d,\d\d\d)(.INFO..|.ERROR.)\[(?P<runner>SoapUITestCaseRunner)\](?P<message>.*)",
				line)
			if z:
				dynamic_content += "<tr><td>{}</td><td>{}</td></tr>".format(z.group('time'), z.group('message'))
				non_html_table_with_test_steps.append([z.group('time'), z.group('message')])

		table_content = "<tr><th>Time</th><th>Message</th></tr>{}".format(dynamic_content)
		table_with_test_steps = "<table>{}</table>".format(table_content)

		return table_with_test_steps, non_html_table_with_test_steps

	def create_table_with_test_case_statuses(self):
		lista = self.payload_converted_to_list
		dynamic_content = ""
		status = ""

		for line in lista:
			z = re.match(
				r'.*\[(?P<testcasename>.*)\],.time.taken:(?P<timetaken>.\d+)ms,.status:.(?P<status>\w*)',
				line)
			if z:
				if z.group('status') == "FINISHED":
					status = '<td bgcolor="#00FF00" style="width: 0%; white-space: nowrap;">OK</td>'
				if z.group('status') == "FAILED":
					status = '<td bgcolor="#FF0000" style="width: 0%; white-space: nowrap;">FAILED</td>'

				dynamic_content += "<tr>{}<td>{}</td><td>{}</td></tr>".format(status,
				                                                              z.group('testcasename'),
				                                                              z.group('timetaken')
				                                                              )
		table_content = "<tr><th>Status</th><th>Test Case</th><th>Time taken(ms)</th></tr>{}".format(dynamic_content)
		table_with_test_case_statuses = "<table>{}</table>".format(table_content)
		return table_with_test_case_statuses

	def create_project_description(self):
		dynamic_content = ''
		dynamic_content += '<tr><td><b>Project Name</b></td><td>{}</td>'.format(self.xml_root.attrib["name"])
		for child in self.xml_root.findall('{http://eviware.com/soapui/config}description'):
			dynamic_content += '<tr><td><b>Project Description</b></td><td>{}</td>'.format(child.text)
		table_with_project_description = '<table id="t02">{}</table>'.format(dynamic_content)

		return table_with_project_description

	def create_body(self, time_started, time_ended):
		piecharts_flex = '<div class="container"><div style="text-align:center"><img src="piechart.png" alt=" " height=auto width=auto></div><div style="text-align:center"><img src="piechart2.png" alt=" " height=auto width=auto></div></div>'

		logo_flex = '<div class="container"><div><img src="placeholder.com-logo1.jpg" alt=" " height=50px width=auto></div></div>'

		table_result_metrics = self.create_table_with_metrics(time_started, time_ended)
		table_with_test_steps, non_html_table_with_test_steps = self.create_table_with_test_steps()
		table_with_test_case_statuses = self.create_table_with_test_case_statuses()
		table_with_project_description = self.create_project_description()
		flex_body = '{}<br><br><div class="container"><div><h2>Overview</h2><hr>{}</div></div><br><br><br><br><br><br><br>{}<div class="container"><div><h2>Result Metrics</h2><hr>{}</div></div><div class="container"><div><h2>TestCases</h2><hr>{}</div></div><div class="container"><div><h2>TestSuite progress</h2><hr>{}</div></div></div>'.format(
			logo_flex,
			table_with_project_description,
			piecharts_flex,
			table_result_metrics,
			table_with_test_case_statuses,
			table_with_test_steps)

		head = '<head><link rel="stylesheet" type="text/css" href="html.css"></head>'

		final_report_in_html = '<!DOCTYPE html><html>{}<div class="page">{}</div></html>'.format(head, flex_body)
		self.create_pie_charts()
		return final_report_in_html, table_result_metrics, non_html_table_with_test_steps

	def create_pie_charts(self):
		explode = (0.1, 0)

		z = re.search(r'Total TestCases: (\d+)*.\((\d+)', self.raw_output)
		plt.figure(3, figsize=(4, 4))
		labels = ['Passed', 'Failed']
		passed = int(z.group(1)) - int(z.group(2))
		failed = int(z.group(2))
		fracs = [passed, failed]
		plt.suptitle("Total Test Cases", fontsize=12)
		plt.pie(fracs, labels=labels, explode=explode, colors=['#34cb34', '#FF0000'], autopct='%1.1f%%', shadow=True)

		plt.savefig("Html_files/piechart.png")

		regex_a = re.search(r"Total Request Assertions: (\d+)", self.raw_output)
		regex_b = re.search(r"Total Failed Assertions: (\d+)", self.raw_output)
		plt.figure(4, figsize=(4, 4))
		passed_total_assertions = int(regex_a.group(1)) - int(regex_b.group(1))
		failed_total_assertions = int(regex_b.group(1))
		fracs = [passed_total_assertions, failed_total_assertions]
		plt.suptitle("Total Request Assertions", fontsize=12)
		plt.pie(fracs, labels=labels, explode=explode, colors=['#34cb34', '#FF0000'], autopct='%1.1f%%', shadow=True)

		plt.savefig("Html_files/piechart2.png")
