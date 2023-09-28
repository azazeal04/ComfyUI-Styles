from .Aesthetic_Styler.Aesthetic_Styler import *
from .Anime_Styler.Anime_Styler import *
from .Fantasy_Styler.Fantasy_Styler import *
from .Gothic_Styler.Gothic_Styler import *
from .Line_Art_Styler.Line_Art_Styler import *
from .Movie_Poster_Styler.Movie_Poster_Styler import *
from .Punk_Styler.Punk_Styler import *
from .Travel_Poster_Styler.Travel_Poster_Styler import *

NODE_CLASS_MAPPINGS = {
    "Aesthetic Styler": AestheticStyler,
    "Anime Styler": AnimeStyler,
    "Fantasy Styler": FantasyStyler,
    "Gothic Styler": GothicStyler,
    "Line Art Styler": LineArtStyler,
    "Movie Poster_Styler": MoviePosterStyler,
    "Punk Style": PunkStyler,
    "Travel Poster Styler": TravelPosterStyler,
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

print("\033[34mAzaeal: \033[92mLoaded\033[0m")