#include <stdlib.h>
#include <stdio.h>

uint8_t rotl8(uint8_t b, int c) {
    uint8_t mask = 0xff << (8 - c); /* This gets us leading c bits set to 1*/
    uint8_t leading = b & mask;     /* This extracts the leading c bits*/
    uint8_t result = (b << c ) | (leading >> (8 - c));
    return result;
}

uint8_t sbox(uint8_t b) {
    switch(b) {
        case 0x0 : return 0x63;
        case 0x1 : return 0x7c;
        case 0x2 : return 0x77;
        case 0x3 : return 0x7b;
        case 0x4 : return ;
        case 0x5 : return ;
        case 0x6 : return ;
        case 0x7 : return ;
        case 0x8 : return ;
        case 0x9 : return ;
        case 0xa : return ;
        case 0xb : return ;
        case 0xc : return ;
        case 0xd : return ;
        case 0xe : return ;
        case 0xf : return ;
    }
}

int main(int argc , char ** argv) {
    for (int i = 0 ; i < 256; i++)
        printf("%2x -> %2x\n",i, sbox(i));
}