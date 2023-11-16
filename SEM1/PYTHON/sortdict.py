my_dict={'one':1,'Three':3,'Five':5,'Two':2,'Four':4}
sorted_dict_asc=dict(sorted(my_dict.items()))
print("Dictionary in ascending order by keys:",sorted_dict_asc)
sorted_dict_desc=dict(sorted(my_dict.items(),reverse=True))
print("Dictionary in descending order by keys:",sorted_dict_desc)
sorted_dict_asc_values=dict(sorted(my_dict.items(),key=lambda item:item[1]))
print("Dictionary in ascending order by values:",sorted_dict_asc_values)
sorted_dict_desc_values=dict(sorted(my_dict.items(),reverse=True))
print("Dictionary in descending order by keys:",sorted_dict_desc_values)


