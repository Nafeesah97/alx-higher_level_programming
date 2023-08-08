#include "lists.h"

/**
 * check_cycle -  C that checks if a singly linked list has a cycle in it
 * @list: list to be checked
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *l, *s;

	l = list;
	s = list;
	while (l != NULL && l->next != NULL)
	{
		s = s->next;
		l = l->next->next;
		if (s == l)
			return (1);
	}
	return (0);
}
