writer_info = 'Leo Tolstoy*1828-08-28*1910-11-20'

lst = writer_info. split('*')
writer_name = lst[0]
birthday = lst[1]
deathday = lst[2]

birthday_split = birthday. split('-')
deathday_split = deathday. split('-')
birth_year = int(birthday_split[0])
death_year = int(deathday_split[0])
writer_age = death_year - birth_year
print('%s, %d' %(writer_name, writer_age))