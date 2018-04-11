import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import numpy as np

class Hermes():
	def __init__(self, host, guest, modelname, smtp='smtp.gmail.com', port=587):
		self.smtp = smtp
		self.port = port
		self.host = host
		self.guest = guest
		self.modelname = modelname
		
		self.server = smtplib.SMTP(self.smtp, self.port)
		self.server.ehlo()
		self.server.starttls()
		self.server.login(self.host, "password")
		self.tracker_logs = {}
		self.tracker_plots = {}

	def init_mail(self, progress):
		self.msg = MIMEMultipart() 
		# storing the senders email address  
		self.msg['From'] = self.host
		# storing the receivers email address 
		self.msg['To'] = self.guest		
		# storing the subject 
		self.msg['Subject'] = "Training Update for {}: {}% Complete".format(self.modelname, progress)


	def mail(self, progress):
		self.init_mail(progress)
		msg_body = ""
		for var in self.tracker_logs.keys():
			mean = np.asarray(self.tracker_logs[var]).mean()
			last = self.tracker_logs[var][-1]
			temp_results = var + " - Current Value: {}, Mean Value: {} \r\n".format(last, mean)
			msg_body+=temp_results
		self.msg.attach(MIMEText(msg_body, 'plain'))
		text = self.msg.as_string()
		self.server.sendmail("pranaydeeps@gmail.com", "theeviltwin@protonmail.com", text)

	def track(self, obj, objname):
		####OBJ MUST BE A LIST OR A NUMPY ARRAY####
		self.tracker_logs[objname] = obj
		print(self.tracker_logs)
	def track_plot(self, plot_path, plot_name):
		self.tracker_plots[plot_name] = plot_path