from django.utils.translation import ugettext_lazy as _

DIAL_CHOICES = (
    ('none', _('None')),
    ('din 41091.1', _('Dial with minute and hour markers (DIN 41091, Sect. 1)')),
    ('din 41091.3', _('Dial with hour markers (DIN 41091, Sect. 3)')),
    ('din 41091.4', _('Dial with hour numerals (DIN 41091, Part 4)')),
    ('swiss', _('Dial with minute and hour markers (Bauhaus)')),
    ('austria', _('Dial with minute and hour markers (Austria)')),
    ('points', _('Dial with hour dots')),
)

HOUR_HAND_CHOICES = (
    ('none', _('None')),
    ('din 41092.3', _('Pointed, bar-shaped hand (DIN 41092, Sect. 3)')),
    ('german', _('Blunt, bar-shaped hand (German Rail)')),
    ('siemens', _('Heart-shaped hand (Siemens)')),
    ('swiss', _('Blunt, javelin-shaped hand (Austria)')),
)

MINUTE_HAND_CHOICES = (
    ('none', _('Without minute hand')),
    ('din 41092.3', _('Pointed, bar-shaped hand (DIN 41092, Sect. 3)')),
    ('german', _('Blunt, bar-shaped hand (German Rail)')),
    ('siemens', _('Serpentine hand (Siemens)')),
    ('swiss', _('Blunt, javelin-shaped hand (Austria)')),
)

SECOND_HAND_CHOICES = (
    ('none', _('Without second hand')),
    ('din 41071.1', _('Javelin-shaped hand (DIN 41071, Sect. 1)')),
    ('din 41071.2', _('Perforated pointer hand (DIN 41071, Sect. 2)')),
    ('german', _('Modern perforated pointer hand (German Rail)')),
    ('swiss', _('Disc-end hand (Switzerland)')),
)

MINUTE_HAND_MOVEMENT_CHOICES = (
    ('stepping', _('Stepping minute hand')),
    ('sweeping', _('Sweeping minute hand')),
)

SECOND_HAND_MOVEMENT_CHOICES = (
    ('stepping', _('Stepping second hand')),
    ('sweeping', _('Sweeping second hand')),
    ('swinging', _('Oscillating second hand')),
)
