#include <map>
#include <vector>
#include <string>
#include <utility>
//#include <cstdlib>

#pragma pack(0)

typedef struct {
	int a;
	int b;
	int c;
} intData;

//#pragma pack(pop)

// #define STRUCT_TO_MAP(__data, __dtype, __map, ...)                                        \
//     ({                                                                                          \
//         int memberSize = sizeof(__dtype);                                                        \
//         int nMembers = sizeof(__data) / memberSize;                                              \
//         std::vector<std::string> members = { __VA_ARGS__ } ;                                       \
//         std::map<std::string, __dtype> __map = std::map<std::string, __dtype>();                 \
//         \  
//         for (int i = 0; i < members.size(); ++i)                                                 \
//         {                                                                                        \
//             __map.insert(std::pair<std::string, __dtype>(members[i], *((__dtype*)&__data + i))); \
//         }                                                                                        \
//     });

#define STRUCT_TO_MAP(__data, __dtype, __map, ...)                                           \
    int memberSize = sizeof(__dtype);                                                        \
    int nMembers = sizeof(__data) / memberSize;                                              \
    std::vector<std::string> members = { __VA_ARGS__ };                                      \
    std::map<std::string, __dtype> __map = std::map<std::string, __dtype>();                 \
    for (int i = 0; i < members.size(); ++i) {                                               \
        __map.insert(std::pair<std::string, __dtype>(members[i], *((__dtype*)&__data + i))); \
    };


int main() 
{
	intData data;
	data.a = 5;
	data.b = 32;
	data.c = 69;

	STRUCT_TO_MAP(data, int, m, "a", "b", "c");
	printMap(m);

	return 0;
}