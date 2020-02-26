#include <stdio.h>

/**
 * match_expression - Function that checks whether two strings are
 * an exact match
 * @str1: The first string to match
 * @str2: The second string to match
 * Return: 1 if match, 0 otherwise
 * Description: Matches two strings. If a period is found, it is considered
 * a match as a period can be replaced with any single character.
 * If an asterisk is found, it is considered a match if the character
 * before it matches the second string's character, and continues
 * until the second string produces a character that is no longer a match
 */
int match_expression(char *str1, char *str2)
{
	//i and count are both incrementing pointers for the for loop.
	//The reason they are declared separately is to keep the
	//two pointers separate for the two strings
	int i, count = 0;

	for (i = 0; str1[i] != '\0' && str2[count] != '\0'; i++, count++)
	{
		//If chars do not match, check for period and asterisk
		//If neither, return false. The two strings do not match
		if (str1[i] != str2[count])
		{
			if (str1[i] != '.' && str1[i] != '*')
				return false;
		}

		if (str1[i] == '.')
			continue;

		//If asterisk is found, check previous char in str1
		//Then find the first nonmatch char in str2
		if (str1[i] == '*')
		{
			i--;
			while (str1[i] == str2[count])
				count++;

			//Decrement count. The nonmatch here can match str1's next char
			i++, count--;
		}
	}

	//Do one last check to make sure both strings are actually a match
	if (str1[i] != str2[count])
		return 0;
	else
		return 1;
}

int main(int argc, char *argv[])
{
	//Replace string1 and string2 with desired strings
	//Note: Only string1 should contain the period or asterisk
	char *string1 = "ray*d";
	char *string2 = "rayyyyyyyyyyyyyd";
	int output = 0;

	output = match_expression(string1, string2);
	if (output == 1)
		printf("%s %s: match found\n", string1, string2);
	else
		printf("%s %s: no match\n", string1, string2);

	return 0;
}
