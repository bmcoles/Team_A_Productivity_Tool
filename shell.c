//Some of these are unecessary as of now
//Will likely be used later, though
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/select.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stddef.h>

int child_stdin;         //child will read from this
int child_stdout;        //write to this
int child_stderr;        //and this
int highest_desc = 0;    //Current highest descriptor number, needed for select() arg
int pid;                 //Child process ID
int more = 0;            //more flag
int c2pout[2];           //child/parent io
int c2perr[2];           //child/parent io
int p2c[2];

struct Node //Nodes used for the command table
{
    char* command;
    char* display;
    struct Node* next; 
};

// TODO: We need two tables which hold the C-based commands and one which
// holds valid python module commands. Best way to store? Array of Structs?

// Shell execution entry point
int main(int argc, char** argv) {

    printf("Welcome to Productivity Shell Version 0.0.0.0.0.0.0.1\n");
    printf("Type \'tutorials\' for user guides\n");
    printf("Type \'help\' for usage\n\n");
    
    // Create process communication pipes
    pipe(c2pout);
    pipe(p2c);
    
    highest_desc = p2c[1];

    // Set up I/O control variables
    fd_set rfds;     // Set of read file descriptors
    fd_set stdoutfd; // Set of output file descriptors
    int r, n;        // Syscall return variables   

    //Sets up Nodes used for the table of commands
    struct Node* first = NULL; //Initallizes the Nodes
    struct Node* second = NULL;
    struct Node* end = NULL;
    
    first = (struct Node*) malloc(sizeof(struct Node)); //Gives them space
    second = (struct Node*) malloc(sizeof(struct Node));
    end = (struct Node*) malloc(sizeof(struct Node));
    
    //Sets up each node with a command that will be checked against, the output that goes with each command, and links the nodes
    first->command = "help\0";
    first->display = "A helpful message of sorts\n\n\0";
    first->next = second;
    
    second->command = "tutorials\0";
    second->display = "This is a tutorial\n\n\0";
    second->next = end;
    
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
        char input[100];
        
        //Takes in user input. This function with scanf allows for spaces to be scanned in addition to normal input
        scanf("%[^\n]%*c", input);
        
        //Checks to see if the input is a premade command. If it is, it outputs what is requested. Otherwise, for now, it prints an error message
        
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
        while(n != NULL)
        {
            //If either the last node is checked, which means the command does not exist, or a command is found, prints out what should be printed
            if(n->next == NULL || !strcmp(input, n->command))
            {
                printf("%s", n->display);
                break;
            }
            
            //Otherwise, moves on
            else
            {
            	n = n->next;
            }
        }
        
        
        // Use named pipes?
        //
        // //C defined instructions, check the master C command table
        /* if (validInternal)
         
         * //Python Modules, check the master Python Module command table
         * else if (validExternal)
         *     if (childPID == 0) {
         
         *          close(c2pout[0]); close(c2perr[0]); close(p2c[1]);
         *          dup2(p2c[0], STDIN_FILENO);
                    dup2(c2pout[1], STDOUT_FILENO);
                    dup2(c2perr[1], STDERR_FILENO);
                    close(c2pout[1]);
                    close(c2perr[1]);
                    close(p2c[0]);

                    //This should be calling exec
                    child_process(argc, argv);
                    printf("post child something happend\n");
                    perror("exec");
                    exit(-1);

         *     }
         *     else {
         *         close(c2pout[1]); close(p2c[0]);
         *          
         *         main_process(argc, argv);
         *         // After this function returns the pipes must be closed
         *         // and buffers must be cleared
         *         reset();
         *         continue;
         *
         *     }
         */
    
    }
}

void main_process(int argc, char* argv[]) {
    char buf[100];  //Read buffer
    fd_set rfds;    //Set of read-from file descriptors
    fd_set stdoutfd;//Needed for nested select
    int r;          //select() return value
    int n;          //read() return value
    //printf("I am the main process\n");

    child_stdout = c2pout[0];
    child_stderr = c2perr[0];
    while(1) {
       //TODO: Figure out when child process is done executing so we can return from this
       //function and close all pipes and reset. Call a close and reset function? Probably.

       FD_ZERO(&rfds);

       //Main process reads from stdin, child_stdout, child_stderr
       //Add stdin and child_stderr to rfds in all modes
       FD_SET(0, &rfds);
       FD_SET(child_stderr, &rfds);

       r = select(highest_desc + 1, &rfds, 0, 0, NULL);
       //printf("select has unblocked\n");

       if(FD_ISSET(0, &rfds)) {
           //Input waiting on stdin
           n = read(0, buf, sizeof(buf));

           //Write to child stdin
           write(p2c[1], buf, n);
       }

       //Child has written something to its stdout
       //Will only ever trigger here in I/O mode
       if(FD_ISSET(child_stderr, &rfds)) {
           char ch;
           while(read(child_stderr, &ch, 1) == 1) {
               write(2, &ch, 1);
           }
       }
    }
}

/*
 *  Generic driver for python module execution
 */
void child_process(int argc, char* argv[]) {
    char buf[64];
    char* cmd[argc];
    
    //Format the command for execvp
    for(int i = 0; i <= argc; i++) {
        if(i+1 == argc) {
            cmd[i] = NULL;
            break;
        }
        cmd[i] = argv[i+1];
    }

    execvp(cmd[0], cmd);
    //If this is reached, execvp didn't run properly
    exit(0);
}



//TODO: Think about modularity, don't dump a bunch of code in main
//      Figure out how to close a child and disassociate all pipes after execution
//      Figure out how to re-fork after closing a child process
//


// From here on functions should be defined for handling each C-based command (help, tutorial, etc)
