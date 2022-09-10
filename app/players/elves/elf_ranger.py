from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname, musical_instrument, bow_level: int):
        super(ElfRanger, self).__init__(nickname, musical_instrument)
        self.__bow_level = bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}. {self.nickname} " \
               f"has bow of the {self.__bow_level} level"

    def get_rating(self):
        return 3 * self.__bow_level