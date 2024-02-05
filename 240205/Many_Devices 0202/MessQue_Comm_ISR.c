#include <mqueue.h>
#include <stdio.h>
#include <wiringPi.h>

mqd_t mfd;

volatile int led_state = LOW;
void buttonPressed(void) {
	struct mq_attr attr = {
		.mq_maxmsg = 10,
		.mq_msgsize = 4,
	};
	
	led_state = (led_state == LOW) ? HIGH : LOW ;
	mq_send(mfd, (char *)&led_state, attr.mq_msgsize, 1);
}

int main(void) {
	const int button_pin = 3;
        	const int led_pin = 1;

	wiringPiSetup();

	pinMode(led_pin, OUTPUT);

	struct mq_attr attr = {
		.mq_maxmsg = 10,
		.mq_msgsize = 4,
	};
	int led_state;    

	mq_unlink("/msg_q");
	mfd = mq_open("/msg_q", O_RDWR | O_CREAT, 0666, &attr);
	if (mfd == -1) {
		perror("open error");
		return -1;
	}

	wiringPiISR(button_pin, INT_EDGE_RISING, buttonPressed);

	while(1) {
		mq_receive(mfd, (char *)&led_state, attr.mq_msgsize, NULL);
		
		printf("Led State %s\n", (led_state == LOW) ? "LOW" : "HIGH");
		digitalWrite(led_pin, led_state);
	}
} 