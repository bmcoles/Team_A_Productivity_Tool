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

        /* TODO  -  Nick
         *
         * Wait for user input
         *
         * Grab input (I think scanf() will work)
         *
         * If input = "help" printf a helpful message of sorts
         *
         * Otherwise we don't have any commands yet so just printf "invalid command"
         *
         * Go back to waiting (just continue the loop)
         *
         * */

        
        //First we need to handle the input command


//Ignore this for now
/* 
 
        FD_ZERO(&rfds);
        FD_SET(0, &rfds);
        FD_SET(child_stderr, 

*/


    
    }
}


//TODO: Think about modularity, don't dump a bunch of code in main
//      Figure out how to close a child and disassociate all pipes after execution
//      Figure out how to re-fork after closing a child process
//

