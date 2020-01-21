import tkinter


class Application(object):

    def __init__(self):
        self.root = tkinter.Tk()

        self.welcomeLabel = tkinter.Label(text = "Welcome to Darts!")
        self.welcomeLabel.grid(row=1, column=0)

        self.playerLabel = tkinter.Label(text = ("Type in Player names!"))
        self.playerLabel.grid(row=2, column=0)

        self.playerEntry = tkinter.Entry()
        self.playerEntry.grid(row=3, column=0)

        self.playGameButton = tkinter.Button(text = "Play", command = self.game_button)
        self.playGameButton.grid(row=4, column=0)


    def game_button(self):
        self.players = []

        playerData = self.playerEntry.get()

        self.players.append(playerData)

        print (self.players)

myApp = Application()
myApp.root.mainloop()
