import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime


class EmailMethods(object):

	@staticmethod
	def send_mail(password, sender_email, receiver_email, attachment, smtp_server, smtp_port, table_result_metrics):
		"""
		:param table_result_metrics: generated table with metrics
		:param password: password to sender email
		:param sender_email: email to send from
		:param receiver_email: receiver email
		:param attachment: file to attach
		:param smtp_server: smtp server
		:param smtp_port:  smtp port
		:return: Static method
		"""
		# Create a multipart message and set headers
		message = MIMEMultipart()
		message["From"] = sender_email
		message["To"] = receiver_email
		message["Subject"] = "Test results from {}".format(datetime.datetime.now()).split('.')[0]
		message["Bcc"] = receiver_email  # Recommended for mass emails

		# Add body to email
		message.attach(MIMEText(table_result_metrics, 'html'))

		filename = attachment
		# Open PDF file in binary mode
		with open(filename, "rb") as attachment:
			# Add file as application/octet-stream
			# Email client can usually download this automatically as attachment
			part = MIMEBase("application", "octet-stream")
			part.set_payload(attachment.read())

		# Encode file in ASCII characters to send by email
		encoders.encode_base64(part)

		# Add header as key/value pair to attachment part
		part.add_header(
			"Content-Disposition",
			f"attachment; filename= {filename}",
		)

		# Add attachment to message and convert message to string
		message.attach(part)
		text = message.as_string()

		# Log in to server using secure context and send email
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, text)

		print("Email has been sent to: {}".format(receiver_email))
