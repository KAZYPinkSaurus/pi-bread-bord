from time import sleep
from gpiozero import LED, PWMLED
from pi.utils import echo_start_end

"""
PWMLEDを用いて明るさを変えて光らせる
"""



@echo_start_end
def main():
    len = 10
    led = PWMLED(13)
    for i in range(len):
        led.value = (i+1)/len
        sleep(1)
        print((i+1)/len)


if __name__ == "__main__":
    main()
