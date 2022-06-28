#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current;
	int i = 2;
	
	current = list;
	while (current != NULL)
	{
		if (current->id == 2)
			return(1);
		else
			current->id = i;
		
		current = current->next;
	}
	return (0);
}
