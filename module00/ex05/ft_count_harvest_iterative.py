# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: paapahid <paapahid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 22:34:05 by paapahid          #+#    #+#              #
#    Updated: 2026/02/18 22:39:07 by paapahid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	i = 1
	while i <= days:
		print("Day" + i)
		i += 1
	print("Harvest time!")