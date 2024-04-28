#include "config.h"

typedef struct {
    char id[MAX_LEN];
    char name[MAX_LEN];
    char passwd[MAX_LEN];
    char contact[MAX_LEN];
    char address[MAX_LEN];
    double balance;
} User;

void pullUsers();
void pushUsers();
User *getUser(int idex);
void userInfo(int i);
int addUser(User *u);
int deleteUser(const char *id, const char *who);
void printUsers();
int checkpass(const char *name, const char *passwd, int *idx);

int userTopup(const char *id, double m);
