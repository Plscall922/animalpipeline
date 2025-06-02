from enum import Enum

class CuteAnimal(Enum):
    RED_PANDA = "red panda"
    QUOKKA = "quokka"
    OTTER = "otter"
    PENGUIN = "penguin"
    HEDGEHOG = "hedgehog"
    PIKA = "pika"
    CAPYBARA = "capybara"
    KOALA = "koala"
    BABY_ELEPHANT = "baby elephant"
    ARCTIC_FOX = "arctic fox"
    FENNEC_FOX = "fennec fox"
    SEA_OTTER = "sea otter"
    SLOW_LORIS = "slow loris"
    FLUFFY_BUNNY = "fluffy bunny"
    BABY_SEAL = "baby seal"
    POMERANIAN = "pomeranian"
    BABY_PANDA = "baby panda"
    SUGAR_GLIDER = "sugar glider"
    DUMBO_OCTOPUS = "dumbo octopus"
    CHINCHILLA = "chinchilla"
    MINIATURE_GOAT = "miniature goat"
    AXOLOTL = "axolotl"
    BABY_SLOTH = "baby sloth"
    KITTEN = "kitten"
    PUPPY = "puppy"

    @classmethod
    def list(cls):
        return [animal.value for animal in cls]
