from twython import Twython
import os
import random
from colormap import rgb2hex
from ConfigParser import SafeConfigParser
class User():
	def __init__(self, app_key, app_secret, oauth_token, oauth_secret):
		self.app_key = app_key
		self.app_secret = app_secret
		self.oauth_token = oauth_token
		self.oauth_secret = oauth_secret
		self.twitter = self.Authenticate()

	def Authenticate(self):
		#Login to Twitter
		t = Twython(self.app_key, self.app_secret, self.oauth_token, self.oauth_secret)
		return t

	def changeAvatar(self, img):
		#Changes Users avatar
		self.twitter.update_profile_image(image = img, offset_top=10)

	def changeBackground(self, img):
		#Changes User's banner image
		self.twitter.update_profile_banner_image(banner = img, offset_top = 100)

class Image():
	def __init__(self):
		self.images = self.collectImages()
		self.avatars = self.images[0]
		self.banners = self.images[1]

	def collectImages(self):
		avatars = []
		banners = []
		for img in os.listdir('/home/tom/AviPython/Avatars'):
			avatars.append(img)
		for img in os.listdir('/home/tom/AviPython/Banners'):
			banners.append(img)
		return [avatars, banners]

	def randProfile(self):
		avatar = self.avatars[random.randint(0, len(self.avatars) - 1)]
		banner = self.banners[random.randint(0, len(self.banners) - 1)]
		return [avatar, banner]

#Authentication Keys
parser = SafeConfigParser()
parser.read("config.ini")

access_key = parser.get("twitter", "ACCESS_KEY")
access_token = parser.get("twitter", "ACCESS_TOKEN")
consumer_key = parser.get("twitter", "CONSUMER_KEY")
consumer_token = parser.get("twitter", "CONSUMER_TOKEN")

if __name__ == '__main__':
	Tom = User(consumer_key, consumer_token, access_key, access_token)
	image = Image()
	newProf = image.randProfile()
	Tom.changeAvatar(open('/home/tom/AviPython/Avatars/' + newProf[0], 'rb'))
	#Tom.changeBackground(open('/home/tom/AviPython/Banners/' + newProf[1], 'rb'))
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	randHex = rgb2hex(r, g, b).replace("#", "")
	#Tom.updateColors(randHex)
