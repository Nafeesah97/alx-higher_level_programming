#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head:  singly linked list
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *prev = NULL;
	listint_t *slow;
	listint_t *next_node;
	listint_t *left;
	listint_t *right;

	current = *head;
	slow = (*head)->next;
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (current->next != NULL && current->next->next != NULL)
	{
		slow = slow->next;
		current = current->next->next;
	}

	while (slow != NULL)
	{
		next_node = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next_node;
	}
	(*head)->next = prev;

	left = *head;
	right = slow;
	while (right != NULL)
	{
		if (left->n != right->n)
		{
			return (0);
		}
		left = left->next;
		right = right->next;
	}
	return (1);
}
