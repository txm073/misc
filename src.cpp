#include "Windows.h"
#include <string>
#include <iostream>

typedef void(__cdecl* Greet)();

int main(int argc, char* argv[]) {
    HINSTANCE lib = LoadLibrary((LPCSTR)"./liblongdouble.dll");
    if (!lib) {
        std::cout << "Failed to load library\n";
        return 1;
    }
    auto greet = (Greet)GetProcAddress(lib, "greet");
    if (!greet) {
        std::cout << "Failed to locate function\n";
        return 1;
    }

    greet();
    FreeLibrary(lib);

    return 0;
}