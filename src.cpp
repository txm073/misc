#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>

#define UNLEN 128

int main(const int argc, const char** argv)
{
    Sleep(3000);
    printf("%d, %d\n", SetCursorPos(100, 200), GetLastError());

    return 0;
}