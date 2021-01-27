import random
import time

from PyQt5.QtCore import pyqtSignal

from worker import Worker


class WorkerDeusExMachina(Worker):

    show_on_grid = pyqtSignal(int)
    apply_force = pyqtSignal(int)

    def __init__(self, player, player_num, grid):
        super().__init__()

        self.player = player
        self.grid = grid
        self.is_done = False
        self.player_num = player_num
        self.time_until_showing_on_grid = random.randint(4, 8)
        self.is_placed_on_grid = False
        self.place_on_grid = random.randint(1, 2)
        self.deus_ex_coords1 = [95, 300]
        self.deus_ex_coords2 = [260, 300]

        self.retList = []

    def die(self):
        """
        End notifications.
        """
        self.is_done = True
        self.thread.quit()

    def work(self):
        if self.player_num == 1:
            while not self.is_done:
                if not self.is_placed_on_grid:
                    time.sleep(self.time_until_showing_on_grid)
                    self.show_on_grid.emit(self.place_on_grid)
                    time.sleep(2)
                    self.proveri_playera_levo_desno()


                    self.time_until_showing_on_grid = random.randint(4, 8)
                    self.is_placed_on_grid = False
                else:
                    time.sleep(0.01)
        elif self.player_num == 2:
            while not self.is_done:
                if not self.proveri_enemies_levo_desno():
                    time.sleep(0.01)
                    self.killed_by_enemy.emit()
                    time.sleep(0.01)
                elif not self.proveri_dead_enemies_levo_desno():
                    time.sleep(0.01)
                else:
                    time.sleep(0.01)

    def proveri_playera_levo_desno(self):

        if self.place_on_grid == 1:
            coords = self.deus_ex_coords1
        else:
            coords = self.deus_ex_coords2

        player_2 = []

        if self.player.x() + self.player.width() <= coords[0] and (self.player.x() + self.player.width()) >= (coords[0] - 10):
            player_2.append(self.player)

        gornja_ivica_bulleta = coords[1]
        donja_ivica_bulleta = coords[1] + 32

        player_konacno = []

        for pl in player_2:
            if (pl.y() <= gornja_ivica_bulleta and ((pl.y() + pl.height()) > gornja_ivica_bulleta)) or (
                    donja_ivica_bulleta <= (pl.y() + pl.height()) and donja_ivica_bulleta >= pl.y()):
                player_konacno.append(pl)

        player_3 = []

        if self.player.x() >= (coords[0] + 32) and self.player.x() <= (coords[0] + 32) + 10:
            player_3.append(self.player)

        gornja_ivica_bulleta = coords[1]
        donja_ivica_bulleta = coords[1] + 32

        player2_konacno = []

        for pl in player_3:
            if (pl.y() <= gornja_ivica_bulleta and ((pl.y() + pl.height()) > gornja_ivica_bulleta)) or (
                    donja_ivica_bulleta <= (pl.y() + pl.height()) and donja_ivica_bulleta >= pl.y()):
                player2_konacno.append(pl)

                #self.apply_force.emit(random.randint(0, 1))
                self.apply_force.emit(0)

        return len(player_konacno) == 0 and len(player2_konacno) == 0
