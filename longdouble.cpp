#include <iostream>

extern "C" {
    void greet() {
        std::cout << "Hello World!\n";
    }
}