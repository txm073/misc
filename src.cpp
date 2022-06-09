#include "Windows.h"
#include <string>
#include <iostream>

typedef int(__cdecl* add)(int a, int b);

int main(int argc, char* argv[]) {
    HINSTANCE lib = LoadLibrary("./maths.dll");
    if (!lib) {
        std::cout << "Failed to load library\n";
        return 1;
    }

    auto csAdd = (add)GetProcAddress(lib, "add");
    if (!csAdd) {
        std::cout << "Failed to locate function\n";
        return 1;
    }

    int sum = csAdd(5, 3);
    std::cout << "Sum: " << sum << "\n";

    FreeLibrary(lib);

    return 0;
}