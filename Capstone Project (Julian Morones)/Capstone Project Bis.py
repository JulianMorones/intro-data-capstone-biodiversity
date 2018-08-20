import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

#In Search of Sheep
species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

observations = pd.read_csv("observations.csv")
print(observations.head())

isheep = lambda x: False \
	if ("Sheep" in x) != True  \
	else True

species["is_sheep"]=species.common_names.apply(isheep)
print(species.head())

species_is_sheep = species[species.is_sheep == True]
print(species_is_sheep)

sheep_species = species_is_sheep[species_is_sheep.category == "Mammal"]
print(sheep_species.head())

#Merging Sheep and Observation DataFrames
sheep_observations = observations.merge(sheep_species)

print sheep_observations.head()

obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()

print obs_by_park

#Plotting Sheep Sightings
plt.figure(figsize=(16,4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park.observations)),obs_by_park.observations)
ax.set_xticks(range(len(obs_by_park.park_name)))
ax.set_xticklabels(obs_by_park.park_name)
plt.ylabel("Number of Observations")
plt.title("Observations of Sheep per Week")
plt.show()

#Foot and Mouth Reduction Effort
baseline = 15

minimum_detectable_effect = 100*5./15

sample_size_per_variant = 870

yellowstone_weeks_observing = sample_size_per_variant/507.

bryce_weeks_observing = sample_size_per_variant/250.