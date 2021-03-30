import time
from sps30_driver import sps30


device_port = "/dev/ttyUSB0"
startup_time = 8
samples_per_measurement = 30
results = []
dates = []
timestamps = []


def main():
    try:
        # INIT SENSOR CLASS AND ESTABLISHING PORT CONNECTION.
        sensor_sps30 = sps30.Sps30(device_port)

        # STARTING UP SPS30 SENSOR. GOING FROM IDLE MODE TO MEASUREMENT MODE.
        # MIN STARTUP TIME IS 8 SECONDS, MAX IS 30 SECONDS.
        sensor_sps30.start_measurement(start_up_time=startup_time)

        # PERFORMING MEASUREMENTS. SENSOR CAN PERFORM MAX 1 MEASUREMENT PER SECOND, HENCE 1 SECOND SLEEP.
        for i in range(samples_per_measurement):
            dates.append(time.strftime('%Y-%m-%d'))
            timestamps.append(time.strftime('%H:%M:%S'))
            results.append(sensor_sps30.read_measured_values())
            time.sleep(1)

        # TURNING OFF MEASUREMENT MODE. RETURNING TO IDLE MODE.
        sensor_sps30.stop_measurement()

        # CLOSE PORT CONNECTION.
        sensor_sps30.close_port()

        # PRINTING DATA TO CONSOLE. CHANGE CODE BELOW ACCORDING TO YOUR NEEDS. MAYBE SAVE DATA TO SQLITE?
        for i in range(samples_per_measurement):
            print(dates[i], timestamps[i], results[i])

    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()


