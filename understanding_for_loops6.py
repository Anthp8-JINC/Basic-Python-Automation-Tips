# Find out how to create a match up using the teams list so that all teams have a chance to play each other.
# Make sure you don't match up a team to play against itself.

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " VS " + away_team)

# The output should look like this

# Dragons VS Wolves
# Dragons VS Pandas
# Dragons VS Unicorns
# Wolves VS Dragons
# Wolves VS Pandas
# Wolves VS Unicorns
# Pandas VS Dragons
# Pandas VS Wolves
# Pandas VS Unicorns
# Unicorns VS Dragons
# Unicorns VS Wolves
# Unicorns VS Pandas