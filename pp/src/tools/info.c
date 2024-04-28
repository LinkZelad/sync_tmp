#include "tools/info.h"

#include <stdio.h>
#include <time.h>

static const char *filePath = "../../data/id.txt";

void genID(char *dest, char type) {
    int uid, gid, oid = 0;
    FILE *pf = fopen(filePath, "r");
    if (pf) {
        fscanf(pf, "%d%d%d", &uid, &gid, &oid);
        fclose(pf);
    }
    int id = 0;
    switch (type) {
    case 'U':
        id = uid++;
        break;
    case 'G':
        id = gid++;
        break;
    case 'O':
        id = oid++;
        break;
    }
    sprintf(dest, "%c%05d", type, id);
    pf = fopen(filePath, "w");
    fprintf(pf, "%d %d %d\n", uid, gid, oid);
    fclose(pf);
}

void getDate(char *dest) {
    time_t current_date;
    time(&current_date);
    struct tm *date = localtime(&current_date);
    sprintf(dest, "%d-%d-%d", date->tm_year + 1900, date->tm_mday,
            date->tm_mon + 1);
}
