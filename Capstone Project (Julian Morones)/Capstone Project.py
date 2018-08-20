#Biodiversity Project
import codecademylib
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

species = pd.read_csv('species_info.csv')

print(species.head())
species.info()

species_count = species.scientific_name.nunique()
species_type = species.category.unique()
conservation_statuses = species.conservation_status.unique()

category_counts = species.groupby("category").scientific_name.nunique().reset_index()
print category_counts

conservation_counts = species.groupby("conservation_status").scientific_name.nunique().reset_index()
print(conservation_counts)

species.fillna('No Intervention', inplace = True)
conservation_counts_fixed = species.groupby("conservation_status").scientific_name.nunique().reset_index()
print(conservation_counts_fixed)

protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')


#Plotting Conservation Status by Species
plt.figure(figsize=(10,4))
ax = plt.subplot()
plt.bar(range(len(protection_counts.conservation_status)),protection_counts.scientific_name)
ax.set_xticks(range(len(protection_counts.conservation_status)))
ax.set_xticklabels(protection_counts.conservation_status)
plt.ylabel("Number of Species")
plt.title("Conservation Status by Species")
plt.show()

#Plotting Conservation Status by Species excluding those with No Intervention status

species2 = species[species.conservation_status != "No Intervention"]

print(species2.head())
species2.info()

print(species2.scientific_name.nunique())

protection_counts2 = species2.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')

plt.figure(figsize=(10,4))
ax = plt.subplot()
plt.bar(range(len(protection_counts2.conservation_status)),protection_counts2.scientific_name)
ax.set_xticks(range(len(protection_counts2.conservation_status)))
ax.set_xticklabels(protection_counts2.conservation_status)
plt.ylabel("Number of Species")
plt.title("Conservation Status by Species")
plt.show()

#Investigating Endangered Species
species['is_protected'] = species.conservation_status != 'No Intervention'

protected = lambda x: True \
	if x != "No Intervention" \
	else False

species["is_protected"]=species.conservation_status.apply(protected)

category_counts = species.groupby(["category","is_protected"]).scientific_name.nunique().reset_index()
print category_counts.head()

category_pivot = category_counts.pivot(columns='is_protected',
                      index='category',
                      values='scientific_name')\
                      .reset_index()
  
category_pivot.columns = ["category","not_protected","protected"]

category_pivot["percent_protected"] =  category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)*100
print category_pivot


#Chi-Squared Test for Significance
contingency_BM = [[30,146],[75,413]]

chi2,pval_bird_mammal,dof,expected=chi2_contingency(contingency_BM)
print pval_bird_mammal

contingency_RM=[[30,146],[5,73]]

chi2,pval_reptile_mammal,dof,expected=chi2_contingency(contingency_RM)
print pval_reptile_mammal

contingency_1=[[7,72],[75,413]]
contingency_2=[[7,72],[11,115]]
contingency_3=[[7,72],[30,146]]
contingency_4=[[7,72],[5,328]]
contingency_5=[[7,72],[5,73]]
contingency_6=[[7,72],[46,4216]]
contingency_7=[[75,413],[11,115]]
contingency_8=[[75,413],[30,146]]
contingency_9=[[75,413],[5,328]]
contingency_10=[[75,413],[5,73]]
contingency_11=[[75,413],[46,4216]]
contingency_12=[[11,115],[30,146]]
contingency_13=[[11,115],[5,328]]
contingency_14=[[11,115],[5,73]]
contingency_15=[[11,115],[46,4216]]
contingency_16=[[30,146],[5,328]]
contingency_17=[[30,146],[5,73]]
contingency_18=[[30,146],[46,4216]]
contingency_19=[[5,328],[5,73]]
contingency_20=[[5,328],[46,4216]]
contingency_21=[[5,73],[46,4216]]


chi2_1,pval_1,dof_1,expected_1=chi2_contingency(contingency_1)
chi2_2,pval_2,dof_2,expected_2=chi2_contingency(contingency_2)
chi2_3,pval_3,dof_3,expected_3=chi2_contingency(contingency_3)
chi2_4,pval_4,dof_4,expected_4=chi2_contingency(contingency_4)
chi2_5,pval_5,dof_5,expected_5=chi2_contingency(contingency_5)
chi2_6,pval_6,dof_6,expected_6=chi2_contingency(contingency_6)
chi2_7,pval_7,dof_7,expected_7=chi2_contingency(contingency_7)
chi2_8,pval_8,dof_8,expected_8=chi2_contingency(contingency_8)
chi2_9,pval_9,dof_9,expected_9=chi2_contingency(contingency_9)
chi2_10,pval_10,dof_10,expected_10=chi2_contingency(contingency_10)
chi2_11,pval_11,dof_11,expected_11=chi2_contingency(contingency_11)
chi2_12,pval_12,dof_12,expected_12=chi2_contingency(contingency_12)
chi2_13,pval_13,dof_13,expected_13=chi2_contingency(contingency_13)
chi2_14,pval_14,dof_14,expected_14=chi2_contingency(contingency_14)
chi2_15,pval_15,dof_15,expected_15=chi2_contingency(contingency_15)
chi2_16,pval_16,dof_16,expected_16=chi2_contingency(contingency_16)
chi2_17,pval_17,dof_17,expected_17=chi2_contingency(contingency_17)
chi2_18,pval_18,dof_18,expected_18=chi2_contingency(contingency_18)
chi2_19,pval_19,dof_19,expected_19=chi2_contingency(contingency_19)
chi2_20,pval_20,dof_20,expected_20=chi2_contingency(contingency_20)
chi2_21,pval_21,dof_21,expected_21=chi2_contingency(contingency_21)

print pval_1,pval_2,pval_3,pval_4,pval_5,pval_6,pval_7,pval_8,pval_9,pval_10,pval_11,pval_12,pval_13,pval_14,pval_15,pval_16,pval_17,pval_18,pval_19,pval_20,pval_21


#Chi-Squared Test against population
contingency_22=[[179,5363],[7,72]]
contingency_23=[[179,5363],[75,413]]
contingency_24=[[179,5363],[11,115]]
contingency_25=[[179,5363],[30,146]]
contingency_26=[[179,5363],[5,328]]
contingency_27=[[179,5363],[5,73]]
contingency_28=[[179,5363],[46,4216]]

chi2_22,pval_22,dof_22,expected_22=chi2_contingency(contingency_22)
chi2_23,pval_23,dof_23,expected_23=chi2_contingency(contingency_23)
chi2_24,pval_24,dof_24,expected_24=chi2_contingency(contingency_24)
chi2_25,pval_25,dof_25,expected_25=chi2_contingency(contingency_25)
chi2_26,pval_26,dof_26,expected_26=chi2_contingency(contingency_26)
chi2_27,pval_27,dof_27,expected_27=chi2_contingency(contingency_27)
chi2_28,pval_28,dof_28,expected_28=chi2_contingency(contingency_28)

print pval_22,pval_23,pval_24,pval_25,pval_26,pval_27,pval_28

#Chi-Squared Test Plants vs. Animals

contingency_final=[[128,819],[51,4544]]
chi2_29,pval_29,dof_29,expected_29=chi2_contingency(contingency_final)
print pval_29