#include "config.h"

typedef enum {
    SELLING,
    SOLD,
    BANNED,
} State;

typedef struct {
    char id[MAX_LEN];
    char name[MAX_LEN];
    double price;
    char seller_id[MAX_LEN];
    State state;
    char date[MAX_LEN];
    char description[MAX_LEN];
} Good;

static Good goods[MAX_GOOD];
static int totalGood = 0;

void pullGoods();
void pushGoods();
Good *getGood(int index);
int addGood(Good *g);
