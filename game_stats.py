class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize statistics."""
		self.settings = ai_game.settings 
		self.reset_stats()

		# Start Alien Invasion in an inactive state.
		self.game_active = False

		# Read in the high score when initializing its value
		self.high_score = 0
		self.load_high_score()

	def load_high_score(self):
		"""Read text file to load high score at the start of the game."""
		try:
			with open("highscore.txt") as file_object:
				contents = file_object.read()
				self.high_score = int(contents)
		except FileNotFoundError:
			with open("highscore.txt", 'w') as file_object:
				file_object.write("0")

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1