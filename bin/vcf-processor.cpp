#include <string>
#include <iostream>

using namespace std;

int main() {
  char* str[10000];
  char buf[4096];
  int count;
  count = 0;

  while(cin.getline(buf, 4096)) {
    if(buf[0] == '#') {
      cout << buf << "\n";
      str[count] = buf;
      count++;
      continue;
    }

    int tabs = 0;
    int ch = 0;

    while(tabs != 4) {
      if(buf[ch] == '\t') tabs++;
      ch++;
    }

    if(buf[ch] != '.') {
      cout << count << buf[ch-1] << "--" << buf[ch] << "\n";
      str[count] = buf;
      count++;
    }
  }
  cout << "VCF string length = " << count-1 << "\n";
  return 0;
}
