from .episodes import EpisodesResource, EpisodeByIdResource
from .guests import GuestsResource, GuestByIdResource
from .appearances import AppearancesResource, AppearanceByIdResource

all_resources = [
    (EpisodesResource, '/episodes'),
    (EpisodeByIdResource, '/episodes/<int:id>'),
    (GuestsResource, '/guests'),
    (GuestByIdResource, '/guests/<int:id>'),
    (AppearancesResource, '/appearances'),
    (AppearanceByIdResource, '/appearances/<int:id>')
]
