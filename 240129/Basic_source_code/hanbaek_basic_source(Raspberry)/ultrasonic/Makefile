PROJECT_NAME	= main
COMPILER	= $(CROSS_COMPILE)$(CC)

FLAG=
ifneq ($(CROSS_COMPILE),)
	FLAG	= CROSS_COMPILE=$(CROSS_COMPILE)
endif
CFLAGS 		=  -O2 
LDFLAGS		=  -lwiringPi 
ARCHIVER	= ar rvs

all: $(PROJECT_NAME)
$(PROJECT_NAME): main.o
	$(COMPILER) -o $@ $^ $(LDFLAGS)
	
main.o: main.c
	$(COMPILER) $(CFLAGS) -c -o $@ $<

.PHONY: clean
clean:
	-rm $(PROJECT_NAME) *.o
