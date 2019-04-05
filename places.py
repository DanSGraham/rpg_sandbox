# Defines all the places objects.

place_types = ['grassland', 'plains', 'forrest', 'tundra', 'jungle', 'swamp', 'lake', 'ocean', 'coast', 'desert', foothills', 'mountain', 'desolation', 'city', 'town', 'ice']

place_modifiers = ['snow', 'flooded', 'burnt']

weather = ['temperate', 'raining', 'stormy', 'heat wave', 'blizzard', 'snowing', 'foggy', 'fire']

season = ['spring', 'summer', 'fall', 'winter']

Terrain_types = ['rocky', 'hilly', 'mountain']


class Fortificaiton:
    pass

class Settlement:
    pass

class Terrain:
    pass

class Structures:
    pass

class World:

    def __init__(self, height, width, days_per_season):
        #Height and width are in terms of hexes.
        self.height = height
        self.width = width
        self.days_per_season = days_per_season
        self.curr_day = 0
        self.tiles = []

    def advance_time(self, days_to_advance):
        self.curr_day += days_to_advance

class Tile:

    weather = ['sunny', 'cloudy', 'precipitation', 'stormy', 'foggy']

    def __init__(self, neighbor_tiles, weather=None):
        self.occupants = {}
        self.weather = weather
        self.neighbor_tiles = neighbor_tiles
        self.temp = 0

    def add_occupant(self, occupant):
        self.occupants[occupant.id] = occupant

    def remove_occupant(self, occupant):
        self.occupants.pop(occupant.id)

    def set_tempearture(self, new_temp):
        self.temp = new_temp

class WaterTile(Tile):

    def __init__(self):
        pass

#Sea water and lake water have different creatures and contribute differently to fertility of surrounding lands.
class SeaWaterTile(WaterTile):
    pass
class LakeWaterTile(WaterTile):
    pass 

class LandTile(Tile): 

    terrain_featuers = ['rocky', 'hilly', 'mountanous']
    land_modifiers = ['snow', 'flood', 'burnt']
    weather = Tile.weather + ['fire']

    def __init__(self):
        self.population = None
        self.has_river = False
        self.terrain_features = None
        self.modifiers = None

    def update_population(self, population):
        self.pop = population

    def add_river(self):
        self.has_river = True

    def remove_river(self):
        self.has_river = False

    def add_road(self):
        self.has_road = True

    #Based on if there is a river or lake in an adjacent tile and what kind of terrain featuers are present.
    def calculate_soil_fertility(self):
        pass

    #Reduces population and output.
    def flood_tile(self):
        pass

    #Reduces population and output.
    def burn_tile(self):
        pass

#Each land type has a probability modifier for certain weather an population. for Ex
# A desert tile has a low baseline probability for precipitation/fog/storms during the summer. However, 
# The desert tile has a much wider range for storm liklihood allowing for flash floods. Also Desert has basically 0
# fire risk, but the plains has a high baseline that increases as it goes days without water. 

# The things to allow modifications based on season:
# 1. Level of precipitation.
# 2. Temperature range.

# Things dependent on precipitation and temperature range:
# 1. Liklihood of fire.
# 2. Liklihood of flood.

#Low liklihood of fire
#High liklihood of flood
#High fertility
#Movement penalty
#Disease Penalty
class SwampTile(LandTile):
    pass
#moderate liklihood of fire.
#moderate liklihood of flood.
#moderate fertility
class ForrestTile(LandTile):
    pass
#highliklihood of fire.
#moderate liklihood of flood.
#high fertility
class PlainsTile(LandTile):
    pass
#Low liklihood of fire.
#High liklihood of flood.
#low fertility unless near lake. 
#Population penalty.
class DesertTile(LandTile):
    pass
#Low liklihood of fire.
#Low liklihood of flood.
#low fertility.
class TundraTile(LandTile):
    pass
#Low liklihood of fire.
#Low liklihood of flood.
#High fertility.
#Movement penalty.
#Disease Penalty.
class JungleTile(LandTile):
    pass
#Low liklihood of fire.
#High liklihood of flood.
#low fertility.
#High Disease Penalty.
class DesolationTile(LandTile):
    pass

