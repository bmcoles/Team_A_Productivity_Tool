//Some of these are unecessary as of now
//Will likely be used later, though
#include "shell.h"
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/select.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stddef.h>
#include <stdbool.h>
#include <time.h>

int child_stdin;         //child will read from this
int child_stdout;        //write to this
int child_stderr;        //and this
int highest_desc = 0;    //Current highest descriptor number, needed for select() arg
int pid;                 //Child process ID
int more = 0;            //more flag
int c2pout[2];
int c2perr[2];
int p2c[2];
time_t t;

//Gets the time
const long int * getTime()
{
    t = time(NULL);
    return &t;
}

//Code for the pomodoro timer
void pomodoro()
{
    //Creates integers that hold how long the work periods are, how many work periods there are, how long the breaks in between are, and how long the last break is
    //Then, it asks the user for values for these, and gets the input
    int work, breaks, breakTime, lBreakTime;
    printf("Please enter how long you would like to spend on the work intervals (Recommended 25 minutes)\n\n>>>>");
    scanf("%d", &work);
    printf("Enter how many work sessions you want to take before a long break (Recommended 4 pomodoros)\n\n>>>>");
    scanf("%d", &breaks);
    printf("Enter how long you want your small breaks between pomodoros to be (Recommended 3-5 minutes)\n\n>>>>");
    scanf("%d", &breakTime);
    printf("How long do you want the final long break to be before resuming work (Recommended 15-30)\n\n>>>>");
    scanf("%d", &lBreakTime);
    
    //This actually runs the timer, going for the amount of times the user wants
    for(int i = 1; i <= breaks; i++)
    {
        //Uses the sleep command to stop the program from running until time is up
    	printf("Please begin work. This is work session %d of %d\n", i, breaks);
        sleep(work * 60);
        
        //If this is the last run, it tells them and runs the long break timer
        if(i == breaks)
        {
            printf("Time is up! Please take a long break. This break will be %d minutes long. When the time is up, you can run the pomodoro command again to do another session\n", lBreakTime);
            sleep(lBreakTime * 60);
            printf("Break time is over! Thank you for using the pomodoro timer\n\n");
        }
        
        //Otherwise, runs the short break timer. Then, it repeats until it is done
        else
        {
            printf("Time is up! Please take a short break before beginning with the next pomodoro. This short break will be %d minutes long\n", breakTime);
            sleep(breakTime * 60);
            printf("Break time is over, back to work!\n");
        }
        
    } 
}

/*
 *  Take in shell input and format it correctly for execvp system call
 */
void  format(char *input, char **cmd) {

     while (*input != '\0') {    
          while (*input == ' ' || *input == '\t' || *input == '\n')
               *input++ = '\0';
          *cmd++ = input;
          while (*input != '\0' && *input != ' ' && 
                 *input != '\t' && *input != '\n') 
               input++;
     }
     *cmd = '\0';
}



// Shell execution entry point
int main(int argc, char** argv) {

    printf("Welcome to Productivity Shell Version 0.0.0.0.0.0.0.1\n");
    printf("Type \'tutorials\' for user guides\n");
    printf("Type \'help\' for usage\n");
    printf("Type \'time\' for the current date and time\n");
    printf("Type \'pomodoro\' to utilize the pomodoro timer\n\n");

    //Sets up Nodes used for the table of commands
    struct Node* first = NULL; //Initallizes the Nodes
    struct Node* second = NULL;
    struct Node* third = NULL;
    struct Node* fourth = NULL;
    struct Node* end = NULL;
    
    first = (struct Node*) malloc(sizeof(struct Node)); //Gives them space
    second = (struct Node*) malloc(sizeof(struct Node));
    third = (struct Node*) malloc(sizeof(struct Node));
    fourth = (struct Node*) malloc(sizeof(struct Node));
    end = (struct Node*) malloc(sizeof(struct Node));
    
    //Sets up each node with a command that will be checked against, the output that goes with each command, and links the nodes
    first->command = "help\n\0";
    first->display = "If you want to get the date and time, type 'time'\n\n\0";
    first->next = second;
    
    second->command = "tutorials\n\0";
    second->display = "Type Ctrl + C to close out of the tool\n\n\0";
    second->next = third;
    
    third->command = "time\n\0";
    third->display = NULL;
    third->next = fourth;
    
    fourth->command = "pomodoro\n\0";
    fourth->display = NULL;
    fourth->next = end;
    
    //This node is the last one, and if it is reached, the command was invalid
    end->command = NULL;
    end->display = "Invalid Command\n\n\0";
    end->next = NULL;
    /*
     * This is our main loop which drives the shell
     *  
     * Main Process: print shell line, wait for input
     * Child Process: fork, set up pipes, execve the python program
     *
     *
     * Child Process must have ability to be killed from stdin input
     *
     */
    while(1) {

        printf(">>>> ");
        //Creates a location for a string input to be placed
        char input[100] = "\0";
        
        //Takes in user input. This function with scanf allows for spaces to be scanned in addition to normal input
        fgets(input, 99, stdin);
        
        //Checks to see if the input is for a python module
        //TODO: Replace this with check for external command names
        char* check = strtok(input, " ");
        if(!strcmp(check, "python3")) {
            char* cmd[128];
            format(input, cmd);
            entry_point(cmd);
            continue;
        }

        //Starts by making the typed command all lowercase for comparisons
        for(int i = 0; input[i] != '\0'; i++)
        {
            if(input[i] >= 'A' && input[i] <= 'Z')
            {
                input[i] = input[i] + 32;
            }
        }

          

        //Starts from the first command, checks to see if the typed command matches any command listed.
        struct Node* n = first;
        
        //Checks to see if a command was not entered in. If no command was entered, the command handler skips the execution
        if(strlen(input) == 1)
        {
            continue;
        }
        
        while(n != NULL)
        {
            //If either the last node is checked, which means the command does not exist, or a command is found, prints out what should be printed
            if(n->next == NULL || !strcmp(input, n->command))
            {
                //If the command is for the pomodoro timer, it runs that
                if(!strcmp(input, "pomodoro\n\0"))
                {
                    pomodoro();
                }
                
                else
                {
                    //This makes sure the shell can tell the time when the time command is entered
                    char temp[256];
                    strcpy(temp, "The current time is ");
                    third->display = strcat(temp, asctime(localtime(getTime())));
                    third->display = strcat(temp, "\n");
                    printf("%s", n->display);
                }
                break;
            }
            
            //Otherwise, moves on
            else
            {
            	n = n->next;
            }
        }

    }
}

void call_internal(char* command) {
    //    switch(command):
    //        case "help"
}


void entry_point(char** cmd) {

    //Python Modules, need process forking
     int w;
     pid_t childPID = fork();

     //Child process
     if (childPID == 0) {
          execvp(*cmd, cmd);
          printf("Something went wrong with child process\n");
          perror("exec");
          exit(-1);

     }
     //Main process, wait for child to finish
     else {
         while (wait(&w) != childPID);
     }
}


//TODO: Think about modularity, don't dump a bunch of code in main
//      Figure out how to close a child and disassociate all pipes after execution
//      Figure out how to re-fork after closing a child process
//
