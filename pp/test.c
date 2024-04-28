#include <stdio.h>
#include <time.h>

int main() {
    time_t current;
    time(&current);
    struct tm *timeinfo = localtime(&current);
    // printf("%d-%d-%d %d:%d:%d\n", timeinfo->tm_year + 1900,
    //        timeinfo->tm_mon + 1, timeinfo->tm_mday, timeinfo->tm_hour,
    //        timeinfo->tm_min, timeinfo->tm_sec);
    printf("%-10s%-10s", "ok", "okkkk");

    return 0;
}
