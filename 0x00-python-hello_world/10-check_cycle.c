#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current;
	
	current = list;
	while (current != NULL && current->next !=NULL)
	{
		if (current->id == 2)
			return(1);
		current->id = 2;
		current = current->next;
	}
	return (0);
}
