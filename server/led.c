#include "led.h"

void init_light_struct(char* command, s_light* dest){
    dest->command   = command[2];
    dest->speed     = command[9];
    dest->red_1     = command[3];
    dest->green_1   = command[4];
    dest->blue_1    = command[5];
    dest->red_2     = command[6];
    dest->green_2   = command[7];
    dest->blue_2    = command[8];
    
}