# include <stdio.h>
# include <stdlib.h>
# include "config.h"
# include "xtern.h"

main(argc,argv)
int argc;
char **argv;
{
	int             i;

	/* with the right packager around, you needn't see this at all ... */
	if (  mh_init(&argc,&argv,NULL,NULL) < 0 ){
	    exit(1);
	}

	/* this just goes right to the externalized form ... */
	extern_s[0] = 0;
	mh_write("outport", "v", NULL, NULL, 1, extern_s);
	mh_shutdown(1,0,"Init process is silently leaving");
}
