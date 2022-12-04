import requests

def download(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name,"wb") as ofs:
		ofs.write(get_response.content)

download("10.0.2.16/filezilla.pdf")