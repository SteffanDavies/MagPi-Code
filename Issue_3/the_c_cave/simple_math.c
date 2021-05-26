#include <stdio.h>

int main()
{
	/* Declare three integer variables */
	int x, y, z;
	printf("enter two whole numbers, separated by a space: ");
	/* Read two values from the keyboard */
	scanf("%d %d", &x, &y);
	/* add the two values together and place the result in z */
	z = x + y;
	printf("%d + %d = %d\n", x, y, z);
	/* multiply x by 10 and then assign the result to x */
	x = x * 10;
	printf("%d + %d = %d", x, y, x+y);
	return 0;
}