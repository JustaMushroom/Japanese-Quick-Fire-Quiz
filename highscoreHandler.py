from pathlib import Path
from json import load, dump

class HighscoreHandler:
	contents: dict = {}

	def __init__(self, highscore_filename: str="high.scores", highscore_directory: Path=Path.cwd()):
		highscorelocation = Path(highscore_directory, highscore_filename)
		self.fileLocation = highscorelocation
		if not Path.exists(highscore_directory / highscore_filename):
			highscorelocation.touch()
			self.contents = {}
			with open(highscorelocation, "w") as file:
				file.write("{}")
		else:
			with open(highscorelocation, "r") as highscoreFile:
				self.contents = load(highscoreFile)

	def getScores(self) -> dict:
		return self.contents

	def updateScore(self, key, value):
		if key not in self.contents.keys():
			raise KeyError("Invalid Score!")
		else:
			self.contents[key] = value

	def addNewScore(self, key, Type):
		try:
			self.contents[key] = Type()
		except Exception:
			raise TypeError("Non-constructable type detected!")

	def saveHighScores(self, highscores: dict = None):
		if highscores is None:
			highscores = self.contents

		with open(self.fileLocation, "w") as file:
			dump(highscores, file)

	def generateContents(self, keys: list, types: list):
		cIndex = 0
		for key in keys:
			try:
				self.contents[key] = types[cIndex]()
			except Exception:
				print("Non-constructable type found!")
			cIndex += 1

	def getScoreString(self) -> str:
		scores = self.contents
		returnstr = ""
		for key in scores:
			value = scores[key]
			returnstr += "{}: {}\n".format(key, value)

		return returnstr
