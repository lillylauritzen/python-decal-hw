# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    },
    #4
    "Proxima Centauri": {
        "RA": "14h 29m 42.9s",
        "Dec": "−63° 04′ 45″",
        "Magnitude": 11.1,
        "Spectral Type": "M5.5Ve"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

#1
def print_star_names(targets):
    for star in targets:
        print(star)
print_star_names(targets)

#2
def print_spectral_types(targets):
    for star, info in targets.items():
        print(star, "-", info['Spectral Type'])
print_spectral_types(targets)

#3
def find_stars_with_magnitude():
    for star, info in targets.items():
        if info['Magnitude'] > 0.1:
            print(star)
find_stars_with_magnitude()

#5
def find_brightest_star_closest_to_20(targets):
    closest_star = None
    closest_distance = float('inf')

    for star, info in targets.items():
        dec = info['Dec']
        dec = dec.replace('−', '-')
        degrees = float(dec.split('°')[0])
        distance = abs(degrees - 20)

        if distance < closest_distance:
            closest_distance = distance
            closest_star = star

    return closest_star

print(find_brightest_star_closest_to_20(targets))

#6
print("my favorite constellation is Siris")
# my favorite constellation is Siris 