#ifndef LED_H
#define LED_H

#ifdef __cplusplus
extern "C"{
#endif

#define CMD_OFF         0x00
#define CMD_SOLID       0x01
#define CMD_GRADIENT    0x02

//.5 sec
#define DELAY_MIN       5

//5 sec
#define DELAY_MAX       50f

typedef struct leds{
    unsigned char     command;
    unsigned char     red_1;
    unsigned char     green_1;
    unsigned char     blue_1;
    unsigned char     red_2;
    unsigned char     green_2;
    unsigned char     blue_2;
    unsigned char     speed;
    
} s_light;

void init_light_struct(char* command, s_light* dest);

#ifdef __cplusplus
}
#endif

#endif //LED_H