from weasyprint import HTML


class HTMLtoPDF(object):

	def convert_html_to_pdf_file(self, html_to_convert, output_location):
		HTML(html_to_convert).write_pdf(output_location, presentational_hints=True)
