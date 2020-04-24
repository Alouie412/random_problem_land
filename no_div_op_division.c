#include <stdio.h>
#include <stdlib.h>

/**
 * no_op_div - Function that replicates the division
 * operator. Note that because we are dividing integers,
 * any remainders are ignored
 * @a: The first number to be divided
 * @b: The second number to divide by
 * Return: The resulting quotient
 */
int no_op_div(int a, int b)
{
	int count = 0;

	/* The entire premise of this block is taking advantage
	 * of the fact that division is simply repeated subtraction,
	 * much like how multiplication is simply repeated addition
	 * Count is used to keep track of how many times subtraction
	 * is done, which also happens to be the resulting quotient
	 */
	while (a - b >= 0)
	{
		a -= b;
		count++;
	}

	return (count);
}

/**
 * main - Main file for doing division
 * @argc: Number of command line arguments
 * @argv: Array of arguments passed in
 * Return: Failure if not enough arguments or division by 0
 * Else, success
 */
int main(int argc, char* argv[])
{
	int a;
	int b;
	int result = 0;

	if (argc < 3)
	{
		printf("Usage: ./a.out NUM1 NUM2\n");
		return (EXIT_FAILURE);
	}

	a = atoi(argv[1]);
	b = atoi(argv[2]);

	if (b == 0)
	{
		printf("Error. Division by 0\n");
	 	return (EXIT_FAILURE);
	}

	printf("Now dividing %d by %d\n", a, b);
	result = no_op_div(a, b);
	printf("Result: %d\n", result);

	return (EXIT_SUCCESS);
}
