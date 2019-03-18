# include <stdio.h>
# include <stdlib.h>
# include "config.h"

/* external representation of stack, just defines globally so is volatile */
# include "xtern.h"

/* internal representation of stack */
struct istack {
	int size;
	int item[STKSIZE];
} really;


struct istack * create()
{
	struct istack *s = (struct istack *) malloc( sizeof (really) );
	s->size = 0;
}

int
empty(s)
struct istack *s;
{
	return (s->size==0);
}

int
full(s)
struct istack *s;
{
	return (s->size==STKSIZE);
}

void push(s,j)
struct istack *s;
int j;
{
	/* okay, so, we're not checking size right now... */
	/* this also cheats since we ignore the zero array entry, 
	   which helps us keep it straight when we copy over in 
	   intern/externalize  */
	int sz = s->size;
	s->item[sz+1] = j;
	s->size = s->size + 1;
}

int
pop(s)
struct istack *s; /* stack must be non-empty!!! */
{
	int sz = s->size;
	if ( empty(s) ){ 
		printf("Error: stack is empty.\n");
		return (-1); /* bleah */
	}
	s->size = sz - 1 ;
	return s->item[sz];
}

show(s)
struct istack *s;
{	int i;

	if (empty(s)) printf("Stack is empty.\n");
	else {
		printf(" :top: ");
		for (i=s->size; i>0; i--) printf(" %d",s->item[i]);
		printf(" :bottom:\n");
	}
}

/* internalize  - return stack using whatever is in volatile externalize buffer */
struct istack * internalize()
{
	int i;
	struct istack *s = create();
	for (i=extern_s[0]; i>0; i--) push(s,extern_s[i]);
	return s;
}

/* externalize - destructively write over the volatile externalize buffer */
externalize (s)
struct istack *s;
{
	int i;
	for (i=1; i<=s->size; i++) extern_s[i] = s->item[i];
	extern_s[0] = --i;
}

