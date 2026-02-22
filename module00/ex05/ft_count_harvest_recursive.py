# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: paapahid <paapahid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 22:38:54 by paapahid          #+#    #+#              #
#    Updated: 2026/02/18 22:47:43 by paapahid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(days=None, current=1):
	if days is None:
		days = int(input("Days until harvest: "))
	if current > days:
		print("Harvest time!")
		return
	print("Day", current)
	ft_count_harvest_recursive(days, current + 1)

ft_count_harvest_recursive()