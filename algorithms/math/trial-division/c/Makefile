TARGET	:= libIsPrime.a
CFLAGS := -std=c17 -Wall -Wextra -Werror -Wshadow -Wvla -Walloca -Wundef -Wfloat-equal	-Wstrict-prototypes -Wconversion -Wswitch-enum -Wswitch-default \
		-Wimplicit-fallthrough -Wunreachable-code -Wformat=2 -Wparentheses -Wmisleading-indentation -Wpedantic -pedantic -O2

all:  ## Build library
	@mkdir -p objects
	clang -c src/isprime.c -o objects/isprime.o -I include $(CFLAGS)
	ar -rcs $(TARGET) objects/isprime.o
	ranlib $(TARGET)

re:  ## Rebuild library
	$(MAKE) clean
	$(MAKE) all

clean:  ## Remove all
	rm -rf objects/isprime.o
	rm -rf $(TARGET)
