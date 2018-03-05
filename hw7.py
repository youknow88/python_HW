
american_date = '06.17.2016'
month = (american_date[:2])
day = (american_date[3:5])
year = (american_date[6:])
european_date = str(day) + str(month) + str(year)
print(european_date)