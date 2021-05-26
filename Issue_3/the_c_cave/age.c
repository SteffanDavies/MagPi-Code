#include <stdio.h>

int main()
{
	/* Declare a variable to hold a number */
	int age;
	/* Ask for an input */
	printf("How old are you? ");
	/* Read a number from the keyboard */
	scanf("%d", &age);
	/* Echo the age */
	printf("You are %d years old.\n", age);
	return 0;
}