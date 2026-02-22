# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: paapahid <paapahid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 22:10:38 by paapahid          #+#    #+#              #
#    Updated: 2026/02/18 22:28:05 by paapahid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	day = 1
	harvest = 0
	while day < 4:
		harvest = harvest + int(input("Day " + str(day) + " harvest: "))
		day += 1
	print("Total harvest:", harvest)
