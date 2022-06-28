#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current;
	current = list;
	while (current != NULL && current->next != NULL)
	{
		if (current->next == list)
			return(1);

		if (current->id == 'A')
			return(1);
		current->id = 'A';
		current = current->next;
	}
	return (0);
}
