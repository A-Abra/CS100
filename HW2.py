"""
Anosh Abraham
CS 100 2018S Section 004
HW 02, September 15, 2019
"""
#1
grades = ['D','A','D','B','C','B','A','F','A','C']
print(grades)
freq = [grades.count('A'),grades.count('B'),grades.count('C'),grades.count('D'),grades.count('F'),]
print(freq)

#2
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']

herding_dogs = dog_breeds[0:2]
print(herding_dogs)

tiny_dogs = dog_breeds[len(dog_breeds):]
print(tiny_dogs)

print("Persian" in dog_breeds)
