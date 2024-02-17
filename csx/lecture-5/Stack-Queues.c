#include <stdio.h>
#include <cs50.h>

int main() {

  int list[4];
  list[0] = 1;
  list[1] = 2;
  list[2] = 3;
  list[3] = 4;
  string s = get_string("what is your name:");
  for (int i = 0; i < 4; i++) {

    printf("%i\n", list[i]);
  }
}
