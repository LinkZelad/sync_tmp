#include <bitset>
#include <iostream>
#include <vector>

// void print_vector(std::vector<int> given_numbers) {
//     for (auto i : given_numbers) {
//         std::cout << i << std::endl;
//     }
// }

int main() {
    std::vector<int> given_numbers = {};
    int number;
    while (std::cin >> number) {
        given_numbers.push_back(number);
        if (getchar() == '\n') {
            break;
        }
    }
    int n = given_numbers.size();
    std::cout << "There the total " << n << std::endl;
    // print_vector(given_numbers);
    int count = 0;
    int a_last = 0;
    int a_new = 0;
    for (int i = 0; i < (1 << n) - 1; i++) {
        a_new = 0;
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                a_new ^= given_numbers[j];
            }
        }
        if (a_new == a_last) {
            count++;
        }
        a_last = a_new;
    }

    std::cout << count << std::endl;
    std::cout << std::bitset<sizeof(count) * 4>(count) << std::endl;
    return 0;
}
