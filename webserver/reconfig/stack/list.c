# include <stdio.h>
# include <stdlib.h>
# include "config.h"

/* external representation of stack, just defines globally so is volatile */
# include "xtern.h"

/* internal representation of stack */
/* initial node is throwaway so we can do pointer magic... */
struct istack {
	  int item;
	  struct istack *next;
	} fake;

struct istack * create()
{
	struct istack *t;
	t = (struct istack *) malloc( sizeof fake );
	t-> next = (struct istack *) NULL;
	return t;
}

int
empty(s)
struct istack *s;
{
	/* we're obviously not doing much sanity checking of parameter */
	return (s->next == NULL);
}

int
full(s)
struct istack *s;
{	int i;

	for (i=0, s=s->next ; s != NULL; s = s->next, i++ )
	return (i>=STKSIZE);   /* probably off by one or two ... */
}

push(s,j)
struct istack *s;  
int j;
{	struct istack *t;

	t = (struct istack *)malloc(sizeof(struct istack));
	t->item = j;
	t->next = s->next;
	s->next = t;
}

int
pop(s)
struct istack *s; /* stack must be non-empty!!! */
{
	int item;
	struct istack *t;

	if (empty(s)){
		printf("Error: stack is empty.\n");
		return(-1); /* bleah */
	}
	t = s->next;
	item = t->item;
	s->next = t->next;
	return item;
}

show(s)
struct istack *s;
{

	if (empty(s)) {
		printf("Stack is empty\n");
		fflush(stdout);
	}
	else {
		s = s->next;
		printf(":top: ");
		while (s != NULL) {
			printf(" %d", s->item);
			s = s->next;
		}
		printf(" :bottom:\n");
		fflush(stdout);
	}
}

struct istack *
internalize()
{
	int i;
	struct istack *s = create();

	for (i = 1; i <= extern_s[0]; i++) {
		push(s,extern_s[i]);   /* or maybe needs to be in reverse order? */
	}
	return s;
}

externalize(s)
struct istack *s;
{
	int i;
	struct istack *t;

	for ( i=1, t=s->next; t != (struct istack *) NULL; i++, t=t->next){
		extern_s[i] = t->item;
	}
	extern_s[0] = i-1;

#ifdef DEBUG
i--;
printf("XX size is %d\n",i);
 {
  int j;
  for(j=1;j<=i;j++){ printf(" %d",extern_s[j]); } printf("\n");
 } 
#endif
}

