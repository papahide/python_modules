# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: paapahid <paapahid@student.42madrid.c>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/22 01:39:24 by paapahid          #+#    #+#              #
#    Updated: 2026/02/22 18:23:42 by paapahid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class SecurePlant:
	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

	def set_height(self, new_height):
		if new_height < 0:
			print("\nInvalid operation attempted: height", 
		 		str(new_height) + "cm [REJECTED]")
			print("Security: Negative height rejected")
		else:
			self.height = new_height
			print("Height updated:", str(new_height) + "cm [OK]")

	def set_age(self, new_age):
		if new_age < 0:
			print("\nInvalid operation attempted: age", 
		 		str(new_age) + "days [REJECTED]")
			print("Security: Negative age rejected")
		else:
			self.age = new_age
			print("Age updated:", str(new_age) + " days [OK]")

	def get_height(self):
		return self.height

	def get_age(self):
		return self.age

def create_plant(name, height, age):
	plant = SecurePlant()
	return plant	
	

if __name__ == "__main__":
	plant = create_plant("Rose", 25, 30)
	print("=== Garden Security System ===")
	print("Plant created:", plant.name)
	plant.set_height(20)
	plant.set_age(30)
	plant.set_height(-5)
	print("\nCurrent plant:", plant.name, "(" + str(plant.get_height()) + "cm,", 
			str(plant.get_age()) + " days" + ")")