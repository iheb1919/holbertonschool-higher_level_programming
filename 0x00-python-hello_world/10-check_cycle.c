#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - functoin check for loop
 * @list: list
 * Return: 0 if no loop , 1 if there is a loop
 */

int check_cycle(listint_t *list)
{
listint_t *list1 = list;
listint_t *list2 = list;
if (list == NULL)
return (0);
while (liste1 && list2 && list1->next)
{
list2 = list2->next;
list1 = list1->next->next;
if (list2 == list1)
return (1);
}
return (0);
}
