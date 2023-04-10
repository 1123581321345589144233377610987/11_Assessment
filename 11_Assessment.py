class Creature:
    def __init__(self, type_of_creature, friendly, position, image):
        # type_of_creature is a short string
        self.type_of_creature = type_of_creature
# friendly should have a True/False value
        self.friendly = friendly
# The position should be a tuple like (x, y, z) where x, y, z are integers
        self.position = position
# The image should be a string holding an image name
        self.image = image
# mutators (setters)

    def set_type_of_creature(self, type_of_creature):
        self.type_of_creature = type_of_creature

    def set_friendly(self, friendly):
        self.friendly = friendly

    def set_position(self, position):
        self.position = position

    def set_image(self, image):
        self.image = image

# accessors (getters)
    def get_type_of_creature(self):
        return self.type_of_creature

    def get_friendly(self):
        return self.friendly

    def get_position(self):
        return self.position

    def get_image(self):
        return self.image

# return a string describing the creature
    def __str__(self):
        if self.friendly:
            description = f"This friendly {self.type_of_creature} is located at "
        else:
            description = f"This unfriendly {self.type_of_creature} is located at "
        return description + str(self.position) + " and uses the image asset: " + self.image + "\n"


class Orc(Creature):
    def __init__(self, position, image, weapon, mhp, chp):
        Creature.__init__(self, "Orc", False, position, image)
        self.weapon = weapon
        self.mhp = mhp
        self.chp = chp

    def set_weapon(self, weapon):
        self.weapon = weapon

    def set_mhp(self, mhp):
        self.mhp = mhp

    def set_chp(self, chp):
        self.chp = chp

    def get_weapon(self):
        return self.weapon

    def get_mhp(self):
        return self.mhp

    def get_chp(self):
        return self.chp

    def __str__(self):
        return f"This Orc uses a(n) {self.weapon} and has HP {self.chp}/{self.mhp}.\n" + Creature.__str__(self)


class OrcBoss(Orc):
    def __init__(self, position, image, weapon, mhp, chp, name, special_move):
        Orc.__init__(self, position, image, weapon, mhp, chp)
        self.name = name
        self.special_move = special_move

    def set_name(self, name):
        self.name = name

    def set_special_move(self, special_move):
        self.special_move = special_move

    def get_name(self):
        return self.name

    def get_special_move(self):
        return self.special_move

    def __str__(self):
        return f"{self.name} is an Orc boss with {self.special_move} as a special move.\n" + Orc.__str__(self)


creature = Creature("rabbit", True, (10, 250, 10), "bunny.gif")
orc = Orc((-100, 200, 50), "orc.gif", "axe spray", 150, 42)
orc_boss = OrcBoss((300, 150, 35), "OrcBoss.gif", "not-so-greatsword", 355, 113, "Jelz", "Recitation of Poetry")
print(creature)
print(orc)
print(orc_boss)
