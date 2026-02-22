# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: paapahid <paapahid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/20 13:59:38 by paapahid          #+#    #+#              #
#    Updated: 2026/02/22 00:56:21 by paapahid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

if __name__ == "__main__":
	rose = Plant("Rose", 25, 30)
	sunflower = Plant("Sunflower", 80, 45)
	cactus = Plant("Cactus", 15, 120)
	plants = [rose, sunflower, cactus]
	print("=== Garden Plant Registry ===")
	for plant in plants:
		print(plant.name + ":", str(plant.height) + "cm,", str(plant.age) + " days old")