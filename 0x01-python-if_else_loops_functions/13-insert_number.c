#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"
/**
* insert_node - inserts a number into a sorted singly linked list
* @head: head node
* @number: number to add
*
* Return: address of new node otherwise NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *next;

	current = *head;
	next = current->next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (current->n > new->n)
	{
		*head = new;
		new->next = current;
	}

	while (next != NULL)
	{
		if (next->n > new->n)
		{
			current->next = new;
			new->next = next;
			return(new);
		}
		current = current->next;
		next = current->next;
	}
	current->next = new;
	return(new);
}
