# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: paapahid <paapahid@student.42madrid.c>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 01:16:45 by paapahid          #+#    #+#              #
#    Updated: 2026/02/22 18:24:58 by paapahid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

def create_plants():
	plants = [
		("Oxalis versicolor", 12, 43),
		("Anguloa uniflora", 9, 16),
		("Diphylleia grayi", 5, 7),
		("Moriviví", 5, 23),
		("Cuerno de Alce", 1, 1)
	]
	for plant in plants:
		plant = Plant(plant[0], plant[1], plant[2])
		print("Created:", plant.name, "(" + str(plant.height) + "cm,", 
			str(plant.age) + " days" + ")")

if __name__ == "__main__":

	print("=== Plant Factory Output ===")
	plants = create_plants()
	print("\nTotal plants created:", str(len(plants)))