#include <iostream>
#include <unistd.h>
#include <vector>
#include <signal.h>
#include <sys/wait.h>

int procB(void) {
    while (!std::cin.eof()) {

        std::string line;
        std::getline(std::cin, line);
        std::cout << line << std::endl;
    }

    return 0;
}


int main (int argc, char **argv) {

    int RgentoAssignment1[2];
    int Assignment1toAssignment2[2];
    pipe(RgentoAssignment1);
    pipe(Assignment1toAssignment2);
    pid_t childprocess_id;

    childprocess_id = fork();
    if(childprocess_id == 0)
    {

        dup2(RgentoAssignment1[1], STDOUT_FILENO);
        close(RgentoAssignment1[0]);
        close(RgentoAssignment1[1]);

        execv("./rgen",argv);
        }
    else{


    pid_t childprocess2_id = fork();
    if(childprocess2_id == 0)
    {
        dup2(RgentoAssignment1[0], STDIN_FILENO);
        close(RgentoAssignment1[0]);
        close(RgentoAssignment1[1]);

        dup2(Assignment1toAssignment2[1], STDOUT_FILENO);
        close(Assignment1toAssignment2[0]);
        close(Assignment1toAssignment2[1]);

        char *argv1[3];

        argv1[0] = (char *)"python";
        argv1[1] = (char *)"a1ece650.py";
        argv1[2] = nullptr;

        execvp("python", argv1);
    }
    else{
    pid_t childprocess3_id = fork();
    if(childprocess3_id == 0)
    {
        dup2(Assignment1toAssignment2[0], STDIN_FILENO);
        close(Assignment1toAssignment2[0]);
        close(Assignment1toAssignment2[1]);

        execv("a2-ece650", argv);

    }
    dup2(Assignment1toAssignment2[1], STDOUT_FILENO);
    close(Assignment1toAssignment2[0]);
    close(Assignment1toAssignment2[1]);
    int end_of_file = procB();



       int status;
        kill(childprocess_id, SIGTERM);
        waitpid(childprocess_id, &status, 0);
        kill(childprocess2_id, SIGTERM);
        waitpid(childprocess2_id, &status, 0);
        kill(childprocess3_id, SIGTERM);
        waitpid(childprocess3_id, &status, 0);

    return end_of_file;
}}}
