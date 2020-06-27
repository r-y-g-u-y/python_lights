#include "led.h"

void init_light_struct(char* command, s_light* dest){
    dest->red_1     = command[2];
    dest->green_1   = command[3];
    dest->blue_1    = command[4];
    dest->red_2     = command[5];
    dest->green_2   = command[6];
    dest->blue_2    = command[7];
    dest->command   = command[8];
}