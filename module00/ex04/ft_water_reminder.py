# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: paapahid <paapahid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 22:29:02 by paapahid          #+#    #+#              #
#    Updated: 2026/02/18 22:31:40 by paapahid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	days = int(input("Days since last watering: "))
	if days > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")