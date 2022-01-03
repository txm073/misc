#include <iostream>

int main()
{
    return 0;
}

extern "C" {
    void greet() {
        std::cout << "Hello from C++!" << std::endl;
    };
}
