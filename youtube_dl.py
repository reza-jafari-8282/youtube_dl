from pytube import YouTube


url = input("Enter the url : ")
media_type = input("video(1) or audio(2) : ")


def video(url):
	resolution = input("Enter the quality you want : ")
	resolution = resolution + "p"
	print("downloading...")
	YouTube(url).streams.filter(res=resolution).first().download()


def audio(url):
	print("downloading...")
	YouTube(url).streams.filter(only_audio=True).first().download()


if media_type == "1":
	video(url)
elif media_type == "2":
	audio(url)