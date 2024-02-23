#include <cstring>
#include <iostream>
#include <ostream>

class Mystring {
  public:
    static int id;
    Mystring() : m_str(new char[1]) {
        m_str[0] = '\0';
        id++;
        std::cout << "call mystring()" << std::endl;
    };

    explicit Mystring(const char *s) {
        m_str = new char[strlen(s) + 1];
        strcpy(m_str, s);
        std::cout << "call mystring(const char* s)" << std::endl;
    }

    explicit Mystring(const Mystring &s)
        : m_str(new char[strlen(s.m_str) + 1]) {
        strcpy(m_str, s.m_str);
        std::cout << "call mystring(const mystring &s)" << std::endl;
    }

    Mystring &operator=(const char *s) {
        delete[] m_str;
        m_str = new char[strlen(s)];
        strcpy(m_str, s);
        std::cout << "call mystring operator=(char)" << std::endl;
        return *this;
    };

    Mystring &operator=(const Mystring &ms) {
        if (this != &ms) {
            delete[] m_str;
            m_str = new char[strlen(ms.m_str) + 1];
            strcpy(m_str, ms.m_str);
        }
        std::cout << "call mystring operator=(mystring)" << std::endl;
        return *this;
    }

    friend std::ostream &operator<<(std::ostream &out, Mystring &s) {
        out << s.m_str;
        return out;
    }

    const char *get_str() { return m_str; }

    ~Mystring() {
        delete[] m_str;
        std::cout << id << " delete now!" << std::endl;
        id--;
    }

  private:
    char *m_str;
};

int Mystring::id = 0;

int main() {
    Mystring s;
    s = "2";

    Mystring b;
    b = s;
    std::cout << b << std::endl;
    return 0;
}
