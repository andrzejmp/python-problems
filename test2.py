import pymsteams

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard("<Microsoft Webhook URL>")

myTeamsMessage.title("This is my message title")

# Add text to the message.
myTeamsMessage.text("this is my text")


myTeamsMessage.addLinkButton("This is the button Text", "https://github.com/rveachkc/pymsteams/")


myTeamsMessage.printme()

# send the message.
myTeamsMessage.send()


git remote add origin https://github.com/andrzejmp/python-problems.git