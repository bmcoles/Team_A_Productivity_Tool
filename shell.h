#ifndef SHELL_H
#define SHELL_H

#include <stdbool.h>

struct Node//Nodes used for the command table
{
    char*  command;     //Command String
    char*  display;     //Help Text
    bool   internal;    //Determine if C function or python module
    struct Node* next; 
};


int main(int argc, char** argv);
void call_internal(char* command);
void entry_point(int argc, char* argv[], struct Node* cmd);
void main_process(int argc, char* argv[]);
void child_process(int argc, char* argv[]);

#endif
