#include<stdio.h>
#include<string.h>
main()
{
	int j,i=0;
	char s[1000][100];
	printf("declared");
	FILE *fp=fopen("x","r");
	while(fscanf(fp,"%[^\n]\n",s[i])!=EOF)
		i++;
	for(j=0;j<i;j++)
	{
		char op[100]="mv \"";
		strcat(op,s[j]);
		strcat(op,"\" \"");
		char format[5];
		format[0]='.';
		format[1]=s[j][strlen(s[j])-3];
		format[2]=s[j][strlen(s[j])-2];
		format[3]=s[j][strlen(s[j])-1];
		format[4]='\0';
		if(s[j][13]=='-')
			s[j][17]='\0';
		else s[j][13]='\0';
		strcat(op,s[j]);
		strcat(op,"[Dre@dLorD]");
		strcat(op,format);
		strcat(op,"\"");
		printf("%s\n",op);
		system(op);
	}
	printf("ended\n");
}
