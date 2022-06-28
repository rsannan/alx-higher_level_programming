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

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;

	while (current != NULL)
	{
		if (current->n > new->n)
		{
			*head = new;
			new->next = current;
			break;
		}
		current = current->next;
		next = current->next;
		if (next->n > new->n || next == NULL)
		{
			current->next = new;
			new->next = next;
			break;
		}
	}
	return (new);
}
