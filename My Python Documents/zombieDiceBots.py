## ZombieDiceBot 
## AI will roll 3 dices out of 13 and will try to get the highest score

import zombiedice

class MyZombie:
    def __init__(self,name):
        # All zombies must have a name
        self.name = name

    def turn(self,gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # First roll
        #roll() returns a dictionary with keys 'brain','shotgun' and 'footsteps' with how many rolls of each type there were.
        # the 'rolls' key is a list of (color,icon) tuples with the exact roll result information.
        # Example of a roll() return value:
        #{'brains':1,'footsteps':1,'shotgun':1,'rolls':[('yellow','brains), ('red','footsteps),('green','shotgun)]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        shotgun = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']

            if shotgun < 2:
                diceRollResults = zombiedice.roll() # Roll Again
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name= 'Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsOneMoreZombie(name='Stop at 2 Shotguns',minShotguns=1),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun',minShotguns=1),
    MyZombie(name="Erim Bot"),
    # Add any other zombie players here.
    )

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies,numGames=1000)
zombiedice.runWebGui(zombies=zombies,numGames=1000)

