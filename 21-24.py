import time
from mcpi.minecraft import Minecraft
import buildings


mc = Minecraft.create()
pos = mc.player.getTilePos()
build_type = input('Задайте вид постройки: ')
build = buildings.Buildings(5, 5, 5, pos, build_type)
build.building()
time.sleep(10)
build.clear()