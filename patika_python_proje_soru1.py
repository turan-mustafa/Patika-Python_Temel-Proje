# patika.dev - python temel egitimi proje sorusu 1
"""
Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, 
non-scalar verilerden de oluşabilir. 

Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

Flatten Multi-Level Lists

"""
#initializing the data and empty list
data = [ [1,"a", ["cat"], 2], [ [ [3] ],"dog"], 4, 5 ]
flat_list = []

# function
def flatten_list(data):
    # iterating over the data
    for element in data:
        # checking for list
        if type(element) == list:
            # calling the same function with current element as new argument
            flatten_list(element)
        else:
            flat_list.append(element)

# flattening the given list
flatten_list(data)

# printing the flat_list
print(flat_list)
