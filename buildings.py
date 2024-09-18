class Buildings:
    def __init__(self, width, height, length, pos, build_type):
        self.width = width
        self.height = height
        self.length = length
        self.pos = pos
        self.build_type = build_type

    def building(self):
        if self.build_type == 'Заготовка дома':
            self.box()
        else:
            print('Такого типа постройки нет')

    def box(self):
        x, y, z = self.pos
        mc.setBlocks(x, y, z,
                     x + self.width, y + self.height,
                     z + self.length, 4)
        mc.setBlocks(x + 1, y + 1, z + 1,
                     x + self.width - 1, y + self.height - 1,
                     z + self.length - 1, 0)

    def clear(self):
        x, y, z = self.pos
        mc.setBlocks(x, y, z,
                     x + self.width, y + self.height,
                     z + self.length, 0)
