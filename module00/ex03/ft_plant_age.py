# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: paapahid <paapahid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 22:24:47 by paapahid          #+#    #+#              #
#    Updated: 2026/02/18 22:28:01 by paapahid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	age = int(input("Enter plant age: "))
	if age > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
