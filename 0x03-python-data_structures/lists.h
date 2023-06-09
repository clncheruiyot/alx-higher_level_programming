#ifndef LIST_H
#define LIST_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next:point to the next node
 *
 * Description: singly linked listnode structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodint_end(listint_t **head, const int n);
int is_palindrome(listint_t **head);

endif /* LIST_H */
