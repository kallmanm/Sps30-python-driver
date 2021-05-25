import time
from sps30_driver import sps30

device_port = "/dev/ttyUSB0"
startup_time = 8


def main():
    try:
        # INIT SENSOR CLASS AND ESTABLISHING PORT CONNECTION.
        sensor_sps30 = sps30.Sps30(device_port)

        # STARTING UP SPS30 SENSOR. GOING FROM IDLE MODE TO MEASUREMENT MODE.
        # MIN STARTUP TIME IS 8 SECONDS, MAX IS 30 SECONDS.
        sensor_sps30.start_measurement(start_up_time=startup_time)

        # EXECUTES FAN CLEANING COMMAND
        result = sensor_sps30.start_fan_cleaning()
        # 11s GIVES THE SENSOR ENOUGH TIME TO RUN CLEAING PROCESS
        time.sleep(11)

        # TURNING OFF MEASUREMENT MODE. RETURNING TO IDLE MODE.
        sensor_sps30.stop_measurement()

        # CLOSE PORT CONNECTION.
        sensor_sps30.close_port()

        # PRINTING DATA TO CONSOLE.
        print(result)

    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
