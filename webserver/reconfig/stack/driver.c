# include <stdio.h>
# include <stdlib.h>
# include "config.h"

/* global definition of volatile extern_s buffer ... */
# include "xtern.h"

char buffer[512], ID[256];



main(argc,argv)
int argc;
char **argv;
{
	int             i, k;
	char           ch;

	struct istack *s;

	/* with the right packager around, you needn't see this at all ... */
	if (  mh_init(&argc,&argv,NULL,NULL) < 0 ){
	    exit(1);
	}
	mh_identity(ID,256);
	mh_read("inport", "v", NULL, NULL, &k, &extern_s);

#ifdef DEBUG
printf("receiving vector (%d): ", extern_s[0] );
{
  int j;
  for(j=0;j<=extern_s[0];j++){ printf(" %d",extern_s[j]); } 
  printf("\n");
}
#endif

	s = (struct istack *) internalize();

	helpme();

	while (1) {

		printf("\nEnter a command: ");	fflush(stdout);

		if ( fgets(buffer, sizeof(buffer), stdin) == NULL  ) {
			terminate();
		}
		ch = buffer[0];	/* later we can be smarter ... */

		switch (ch) {
		case 'h':
			helpme();
			break;

		case 'c':
			s = (struct istack *) create();
			printf("Created a new stack.\n");
			break;

		case 'u':
			if (full(s)) {
				printf("ERROR:  stack is full\n");
			} else {
				printf("	Enter an integer: ");
				if ( fgets(buffer, sizeof(buffer), stdin) == NULL  ) {
					terminate();
				}
				if (1 != sscanf(buffer, "%d", &i)) {
					printf("Huh?\n");
				} else {
					push(s, i);
					printf("Pushed %d onto stack.\n", i);
				}
			}
			break;

		case 'p':
			if (empty(s)) {
			   printf("ERROR:  stack is empty\n");
			} else {
			   printf("Popped %d from stack.\n", pop(s));
			}
			break;

		case 'e':
			if (empty(s)) {
				printf("Stack is empty.\n");
			} else {
				printf("Stack is not empty.\n");
			}
			break;

		case 'f':
			if (full(s)) {
				printf("Stack is full.\n");
			} else {
				printf("Stack is not full.\n");
			}
			break;

		case 's':
			show(s);
			break;

		case 't':
			/* needs work */
			externalize(s);
			mh_write("outport", "v", NULL, NULL, STKSIZE, extern_s);

#ifdef DEBUG
printf("sending vector: "); fflush(stdout);
{
  int j;
  for(j=0;j<=i;j++){ printf(" %d",extern_s[j]); } 
  printf("\n");
}
#endif

			mh_read("inport", "v", NULL, NULL, &k, &extern_s);

#ifdef DEBUG
printf("receiving vector (%d): ", extern_s[0] );
{
  int j;
  for(j=0;j<=extern_s[0];j++){ printf(" %d",extern_s[j]); } 
  printf("\n");
} 
#endif 
			s = (struct istack *) internalize();
			break;

		case 'q':
			terminate();
			break;

		case 'i': /* unadvertised special ... */
			printf("%s\n",ID);
			break;
		default:
			printf("%c is not a valid command.\n", ch);
			break;
		}
	}
	/* NOT REACHED */
}


helpme()
{
   printf("\n(h)elp (c)reate p(u)sh (p)op (e)mpty (f)ull (s)how (t)ransmit (q)uit\n");
}


terminate()
{
	fflush(stdout);
	mh_shutdown(0,0,"Done!\n");
}


