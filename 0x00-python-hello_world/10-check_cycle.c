#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current;
	if (list == NULL)
		return(0);
	current = list;
	while (current != NULL && current->next != NULL)
	{
		if (current->id == 'A')
			return(1);
		current->id = 'A';
		current = current->next;
	}
	return (0);
}
