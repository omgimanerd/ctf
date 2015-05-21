#include <stdio.h>
#include <stdlib.h>

char enc[40];

void encrypt(char* dec) {

  int i;

  for (i = 0; i < 40; i++) {
    char c = dec[i];
    c = c ^ (c >> 4);
    enc[i] = (char) c;
  }

}

int main(int argc, char** argv) {

  char ip[40], enc[40];
  fgets(ip, 41, stdin);
  encrypt(ip);
  printf("%s\n", ip);
  return 0;

}

