LDFLAGS = -m32
CFLAGS = -g -m32
# LITH = ../Polylith/Bus
LITH = ../lib

all:	lstack astack init demo
# all:	lstack astack applist apparray demo ghostack

lstack: driver.o list.o
	cc -o lstack driver.o list.o ${LDFLAGS} -L${LITH} -lith

astack: driver.o array.o
	cc -o astack driver.o array.o ${LDFLAGS} -L${LITH} -lith

init:	init.o
	cc -o init init.o ${LDFLAGS} -L${LITH} -lith

# applist: application.o list.o
# 	cc -o applist application.o list.o ${LDFLAGS} -L${LITH} -lith
# 
# apparray: application.o array.o
#	cc -o apparray application.o list.o ${LDFLAGS} -L${LITH} -lith

demo:	demo.co
	csl -m -o demo demo.co

demo.co: demo.cl
	csc demo.cl

clean:
	rm -f *.o priority apparray applist astack lstack ghostack *.co demo core

install:
	@echo "There is nothing to install for this demonstration."
