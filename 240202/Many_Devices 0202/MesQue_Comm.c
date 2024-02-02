#include <mqueue.h>
#include <stdio.h>
#include <wiringPi.h>

mqd_t mfd;

PI_THREAD(t1) {
        struct mq_attr attr = {
                .mq_maxmsg = 10,
                .mq_msgsize = 4,
        };
        int value = 0;

        while(1) {
                value ++;
                mq_send(mfd, (char *)&value, attr.mq_msgsize, 1);

                delay(100);
        }
}

int main() {
        struct mq_attr attr = {
                .mq_maxmsg = 10,
                .mq_msgsize = 4,
        };
        int value;

        mq_unlink("/msg_q");
        mfd = mq_open("/msg_q", O_RDWR | O_CREAT, 0666, &attr);
        if (mfd == -1) {
                perror("open error");
                return -1;
        }

        piThreadCreate(t1);

        while(1) {
                mq_receive(mfd, (char *)&value, attr.mq_msgsize, NULL);

                printf("Read Data %d\n", value);
        }
}