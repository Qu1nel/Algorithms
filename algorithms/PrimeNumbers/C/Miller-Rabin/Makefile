LIBNAME 	:= IsPrime
TARGET 		:= lib$(LIBNAME).a

SRC_DIR     := src
INCLD_DIR 	:= include
OBJ_DIR 	:= objects

OBJECTS     := $(patsubst %.c, $(OBJ_DIR)/%.o, $(patsubst $(SRC_DIR)/%, %, $(shell find $(SRC_DIR) -type f -name '*.c' 2>/dev/null)))
DEPS 		:= $(OBJECTS:.o=.d)

CC 			:= clang
CFLAGS 		:= -std=c17 -Wall -Wextra -Werror -Wshadow -Wvla -Walloca -Wundef -Wfloat-equal \
				-Wstrict-prototypes -Wconversion -Wswitch-enum -Wswitch-default -Wimplicit-fallthrough \
				-Wunreachable-code -Wformat=2 -Wparentheses -Wmisleading-indentation -Wpedantic -pedantic -O2

CPPFLAGS 	:= -I$(INCLD_DIR) -MMD -MP
LDFLAGS 	:=
AR 			:= ar
ARFLAGS 	:= -r -c -s

RM          := rm -f
MAKEFLAGS 	+= --no-print-directory
DIR_DUP     = mkdir -p $(@D)


.PHONY: all
all: build

$(TARGET): $(OBJECTS)
	$(AR) $(ARFLAGS) $(TARGET) $(OBJECTS)
	$(info [BUILD] $@ : $(AR) $(ARFLAGS) $(TARGET) $(OBJECTS))

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	$(DIR_DUP)
	$(CC) -c $< -o $@ $(CFLAGS) $(CPPFLAGS)
	$(info [COMPILED] $@ : $(CC) -c $< -o $@ $(CFLAGS) $(CPPFLAGS))

-include $(DEPS)

.PHONY: build
build: $(TARGET)  ## Build library
	$(shell ranlib $(TARGET))
	$(info [RANLIB] $(TARGET))

.PHONY: re
re:  ## Rebuild library
	$(MAKE) fclean
	$(MAKE) all

.PHONY: clean
clean:  ## Remove all object and dep files
	$(info $(RM) $(OBJECTS) $(DEPS))
	$(RM) $(OBJECTS) $(DEPS)

.PHONY: fclean
fclean: clean  ## Remove library + all object files + dep files
	$(info $(RM) $(TARGET))
	$(RM) $(TARGET)

.PHONY: help
help:  ## Show this output, i.e. help to use the commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

info-%:
	@make --dry-run --always-make $* | grep -v "info"

print-%:
	@$(info '$*'='$($*)')


.SILENT:

