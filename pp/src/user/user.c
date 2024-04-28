#include "user/user.h"
#include "tools/info.h"

#include <stdio.h>
#include <string.h>

static User users[MAX_USER];
static int totalUser = 0;

static char *filePath = "../../data/user.txt";
static const char *header =
    "|ID         |Name       |Contact    |Address    |Balance    |";
static const char *divide =
    "+-----------+-----------+-----------+-----------+-----------+";

void pullUsers() {
    totalUser = 0;
    FILE *pf = fopen(filePath, "r");
    if (pf) {
        while (fscanf(pf, "%s %s %s %s %s %lf", users[totalUser].id,
                      users[totalUser].name, users[totalUser].passwd,
                      users[totalUser].contact, users[totalUser].address,
                      &users[totalUser].balance) != EOF) {
            totalUser++;
        }
        fclose(pf);
    }
}

void pushUsers() {
    FILE *pf = fopen(filePath, "w");
    if (pf) {
        for (int i = 0; i < totalUser; i++) {
            fprintf(pf, "%s %s %s %s %s %.1lf\n", users[i].id, users[i].name,
                    users[i].passwd, users[i].contact, users[i].address,
                    users[i].balance);
        }
        fclose(pf);
    }
}

User *getUser(int idex) {
    idex = idex - 1;
    if (idex < 0 || idex > totalUser) {
        printf("用户不存在\n");
        return NULL;
    }
    // return &users[idex];
    return users + idex;
}

void userInfo(int i) {
    i = i - 1;
    if (i < 0 || i > totalUser) {
        printf("用户不存在\n");
    } else {
        printf("Id:       | %s\n", users[i].id);
        printf("Name:     | %s\n", users[i].name);
        printf("Contact:  | %s\n", users[i].contact);
        printf("Address:  | %s\n", users[i].address);
        printf("Balance:  | %.1f\n", users[i].balance);
    }
}

static int searchUserName(const char *name) {
    for (int i = 0; i < totalUser; i++) {
        if (strcmp(users[i].name, name) == 0) {
            return i;
        }
    }
    return -1;
}
int addUser(User *u) {
    if (totalUser == MAX_USER) {
        return 0;
    }
    if (searchUserName(u->name) != -1) {
        return 0;
    }
    genID(u->id, 'U');
    users[totalUser++] = *u;
    return 1;
}

static int searchUserId(const char *id) {
    for (int i = 0; i < totalUser; i++) {
        if (strcmp(users[i].id, id) == 0) {
            return i;
        }
    }
    return -1;
}
int deleteUser(const char *id, const char *who) {
    if (who)
        return 0;
    int idx = searchUserId(id);
    if (idx == -1) {
        return 0;
    }
    for (int i = idx; i < totalUser - 1; i++) {
        users[i] = users[i + 1];
    }
    totalUser--;
    return 1;
}

void printUsers() {
    print_header;
    for (int i = 0; i < totalUser; i++) {
        printf("|%-10s |%-10s |%-10s |%-10s |%-10.1f |\n", users[i].id,
               users[i].name, users[i].contact, users[i].address,
               users[i].balance);
        print_divide;
    }
}

int checkpass(const char *name, const char *passwd, int *idx) {
    *idx = searchUserName(name);
    if (*idx == -1) {
        return 0;
    }
    return strcmp(users[*idx].passwd, passwd) == 0;
}

int userTopup(const char *id, double m) {
    int idx = searchUserId(id);
    if (idx == -1) {
        return 0;
    }
    users[idx].balance += m;
    return 1;
}
