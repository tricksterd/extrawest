temp_str = 'козявко Rеонід DdD'
temp_str = temp_str.replace(temp_str.split(' ')[2], 'Олександрович')
temp_str = temp_str.replace('R', 'Л')
temp_str = temp_str.split(' ')[0].capitalize() + ' ' + temp_str.split(' ')[1].capitalize() \
           + ' ' + temp_str.split(' ')[2].capitalize()
print(temp_str)
