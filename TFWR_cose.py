it = [Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Sunflower, Entities.Carrot, Entities.Carrot, Entities.Grass, Entities.Grass, Entities.Sunflower, Entities.Tree, Entities.Tree]


def bek():
	while True:
		if get_pos_x() != 0:
			move(West)
		if get_pos_y() != 0:
			move(South)
		if get_pos_x() == 0 and get_pos_y() == 0:
			break

def posadka(it):
	for i in range(get_world_size()):
		u = get_pos_x()
		for f in range(get_world_size()):
			if get_ground_type() == Grounds.Grassland:
				till()
			if u == 10 or u == 11:
				use_item(Items.Water)
				use_item(Items.Fertilizer)
				use_item(Items.Fertilizer)
			plant(it[u])
			move(North)

		move(East)

def trech():
	bek()
	for d in range(get_world_size()):
		for i in range(get_world_size()):
			harvest()
			move(North)
		move(East)

trech()
while True:
	bek()
	posadka(it)
	for d in range(15000):
		pass
	trech()
