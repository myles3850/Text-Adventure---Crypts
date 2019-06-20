class Player:
    Health = 10
    Armour = 10000

    def health():
        print(Player.Health)

    def armour():
        stat = Player.Armour / 100
        print(stat)

class Mule:

    health = 5
    armour = 10000

    def health():
        print(Mule.health)

    def armour():
        print(Mule.armour/100)


class Game:
    fightswon = 0

    class Money:
        gold = 0
        silver = 0
        copper = 0
