import b_AthleteClass as ac

generic_athlete = ac.Athlete(6, 220, 0.2)

quarterback = ac.Football_Player(6.2, 250, 0.15, 'quarterback', 'offense')


print("The height for the generic athlete is:", generic_athlete.get_ht())

# print("The team of the generic athlete is:",generic_athlete.get_team())
# this wont work because the get team method is not in Athlete superclass

print("The weight for the football player is:", quarterback.get_wt())

print("The position of the football player is:", quarterback.get_position())
