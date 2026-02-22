# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: paapahid <paapahid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 01:16:45 by paapahid          #+#    #+#              #
#    Updated: 2026/02/22 01:38:38 by paapahid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

if __name__ == "__main__":
	plants = [
		("Oxalis versicolor", 12, 43),
		("Anguloa uniflora", 9, 16),
		("Diphylleia grayi", 5, 7),
		("Moriviví", 5, 23),
		("Cuerno de Alce", 1, 1)
	]
	print("=== Plant Factory Output ===")
	for plant in plants:
		plant = Plant(plant[0], plant[1], plant[2])
		print("Created:", plant.name, "(" + str(plant.height) + "cm,", 
			str(plant.age) + " days" + ")")
	print("\nTotal plants created:", str(len(plants)))