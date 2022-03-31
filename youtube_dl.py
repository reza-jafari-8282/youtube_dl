from pytube import YouTube

class Youtube_dl:
	def __init__(self,url):
		self.url = url

	def video(self):
		print("downloading...")
		YouTube(url).streams.filter(res="720p").first().download()

	def audio(self):
		print("downloading...")
		YouTube(url).streams.filter(only_audio=True).first().download()

url = input("Enter the url : ")
media_type = input("video(1) or audio(2) : ")

if media_type == "1":
	Youtube_dl.video(url)
elif media_type == "2":
	Youtube_dl.audio(url)
