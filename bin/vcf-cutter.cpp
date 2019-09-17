#include <string>
#include <iostream>

using namespace std;

int main() {

  char buf[4096];

  while(cin.getline(buf, 4096)) {
    if(buf[0] == '#') {
      cout << buf << "\n";
      continue;
    }

    int tabs = 0;
    int ch = 0;

    while(tabs != 4) {
      if(buf[ch] == '\t') tabs++;
      ch++;
    }

    if(buf[ch] != '.') {
      cout << buf << "\n";
    }
  }
  return 0;
}
