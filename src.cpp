#include <iostream>
#include <string>
#include <vector>
#include <cmath>

#define MAX_BUFSIZE 1024

std::vector<std::string> split(std::string s, std::string delim) {
    std::vector<std::string> splits = {};
    size_t start = 0U;
    size_t end = s.find(delim);
    while (end != std::string::npos)
    {
        splits.push_back(s.substr(start, end - start));
        start = end + delim.length();
        end = s.find(delim, start);
    }
    splits.push_back(s.substr(start, end));
    return splits;
}

int truncateMessage(size_t dataLen) {
    int nChunks = (int)floor(dataLen / MAX_BUFSIZE); 
    int chunkSize, nBytes = 0, status;
    std::cout << dataLen << ", " << MAX_BUFSIZE << "\n";
    if (dataLen % MAX_BUFSIZE != 0) {
        nChunks++;
    }
    return nChunks;
}

int main() {
    std::cout << truncateMessage(1366 * 768 - 512) << "\n";

    return 0;
}