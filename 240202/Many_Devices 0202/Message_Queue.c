#include <mqueue.h>
#include <stdio.h>

int main() {
        mqd_t mqd;
        struct mq_attr attr = {
                .mq_maxmsg = 10,
                .mq_msgsize = 4,
        };

        mq_unlink("/msg_q");
        mqd = mq_open("/msg_q", O_RDWR | O_CREAT,  0666, &attr);
        if (mqd == -1) {
                perror("open error");
                return -1;
        }

        return 0;
}

// $ ls /dev/mqueue/
// $
// $ gcc –o mq_create mq_create.c –lrt –lwiringPi
// $ ./mq_create
// $ ls /dev/mqueue/