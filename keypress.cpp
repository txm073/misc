#include <iostream>
#include <string>
#include "windows.h"
#include "conio.h"

using namespace std;
#define DELAY 100
#pragma comment(lib, "user32.lib")


int mouseInput() {
    Sleep(DELAY);
    INPUT in[2] = {};
    ZeroMemory(in, sizeof(in));
    in[0].type = INPUT_MOUSE;
    in[0].mi.dwFlags = MOUSEEVENTF_LEFTDOWN;
    in[1].type = INPUT_MOUSE;
    in[1].mi.dwFlags = MOUSEEVENTF_LEFTUP;
    unsigned int success = SendInput(2, in, sizeof(INPUT));
    return (success != 2);
}

int keyboardInput(string str) {
    int length = str.length() * 2;
    INPUT in[length] = {};

    int i = 0;
    for (char c : str) {
        in[i].type = INPUT_KEYBOARD;
        in[i].ki.wVk = int(c);
        in[i].ki.dwFlags = KEYEVENTF_EXTENDEDKEY;

        in[i+1].type = INPUT_KEYBOARD;
        in[i+1].ki.wVk = int(c);
        in[i+1].ki.dwFlags = KEYEVENTF_KEYUP;
        i += 2;
    }

    unsigned int success = SendInput(length, in, sizeof(INPUT));
    return (success != length);
}

int main(int argc, char *argv[]) {
    cout << KEYEVENTF_EXTENDEDKEY << " " << KEYEVENTF_KEYUP << endl;

    return 0;
}
