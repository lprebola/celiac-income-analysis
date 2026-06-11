import pandas as pd

# Load celiac data
celiac = pd.read_excel('data/raw/Celiac_Prevalence_by_Country.xlsx')
celiac = celiac[['Country', 'Celiac Disease Prevalence (2016)']]
celiac.columns = ['Country', 'Celiac_Prevalence']
celiac = celiac.dropna(subset=['Country', 'Celiac_Prevalence'])
celiac = celiac[~celiac['Country'].str.startswith('Source')]
celiac = celiac[~celiac['Country'].str.startswith('⚠')]

name_fixes = {
    'Yemen': 'Yemen, Rep.',
    'Syria': 'Syrian Arab Republic',
    'Turkey': 'Turkiye',
    'Iran': 'Iran, Islamic Rep.',
    'Egypt': 'Egypt, Arab Rep.'
}
celiac['Country'] = celiac['Country'].replace(name_fixes)

# Load GDP data
gdp = pd.read_excel('data/raw/GDP_per_capita.xlsx')
gdp = gdp[['Country Name', '2016 [YR2016]']]
gdp.columns = ['Country', 'GDP_per_capita_2016']
gdp = gdp[gdp['GDP_per_capita_2016'] != '..']
gdp = gdp.dropna(subset=['GDP_per_capita_2016'])

# Merge on country name
merged = pd.merge(celiac, gdp, on='Country', how='inner')
print(merged.shape)
print(merged)


#Save cleaned dataset
merged.to_csv('data/cleaned/master_clean.csv', index=False)