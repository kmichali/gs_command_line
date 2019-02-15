#include <stdio.h>

int main()
{
  #ifdef DEBUG
     printf("Debug mode.\n");
  #endif

  printf("Hello world!\n");
  return 0;
}
