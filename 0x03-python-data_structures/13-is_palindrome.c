#include "lists.h"
int check_palindrome(int idx_top, int idx_bottom, int list_len, listint_t *head)
{
	listint_t *top_n = head;
	listint_t *bottom_n = head;
	int i= 0, j = 0;

	while(i < idx_top)
	{
		top_n = top_n->next;
		i++;
	}

	while(j < idx_bottom)
	{
		bottom_n = bottom_n->next;
		j++;
	}

	if(bottom_n->n == top_n->n)
	{
		if(idx_top == (list_len / 2) - 1)
			return(1);
		return(check_palindrome(idx_top + 1, idx_bottom - 1, list_len, head));
	}
	return(0);
}

/**
* listint_len - returns the number of elements in a linked list
* @h: head pointer
*
* Return: Number of elements
*/
int listint_len(listint_t *h)
{
int count = 0;
listint_t *now;

if (h == NULL)
{
	return (0);
}
now = h;
while (now)
{
	count++;
	now = now->next;
}
return (count);
}

int is_palindrome(listint_t **head)
{
	int list_len = listint_len(*head);
	int i_bottom = list_len - 1;
	int i_top = 0;
	return(check_palindrome(i_top, i_bottom, list_len, *head));

}
