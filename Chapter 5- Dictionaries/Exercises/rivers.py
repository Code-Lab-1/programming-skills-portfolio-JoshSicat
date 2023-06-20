rivers ={

    'nile': 'egypt',
    'mississipi' : 'united states',
    'fraser' : 'danaca',
    'kuskowim' : 'alaska',
    'yangtze' : 'china',
}

for river, country in rivers.times():
    print(f"the{river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"-{river.title()}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"-{country.title()}")