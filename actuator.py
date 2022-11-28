from serial import Serial
from time import time
from time import sleep
from datetime import datetime
import sys

def save(start_time, end_time, act_time, length, val1):
    print(f'{start_time} ~ {end_time} {act_time}초 {val1} {length}mm')
    file = open('./activate_time.txt', 'a', encoding='UTF-8')
    file.write(f'{start_time} ~ {end_time} {act_time}초 {val1} {length}mm\n')
    file.close()

    # filepath = "./test.xlsx"
    # wb = openpyxl.load_workbook(filepath)
    # ws = wb.active
    # ws.append([start_time, end_time, act_time, val1, round(300/act_time, 5)])
    # wb.save(filepath)
    return

def sensor(val1, val2):
    #val1은 up down
    #val2는 길이
    move_input = True
    thres = 300
    is_end = None
    is_start = False
    dateformat = "%Y-%m-%d %H:%M:%S"

    if val1 == "up":
        move = "1"
        if val2 >= 300:
            second_length = 11.84792219274978
        elif val2 >= 250:
            second_length = 11.83587585481326
        elif val2 >= 200:
            second_length = 11.87335092348285
        elif val2 >= 150:
            second_length = 11.93633952254642
        elif val2 >= 100:
           second_length = 12.33766233766234
        elif val2 >= 50:
            second_length = 12.70207852193995
        else:
            second_length = 13

    elif val1 == "down":
        move = "0"
        if val2 >= 300:
            second_length = 11.76470588235294
        elif val2 >= 250:
            second_length = 11.37566137566138
        elif val2 >= 200:
            second_length = 11.92910702113156
        elif val2 >= 150:
            second_length = 11.83378500451671
        elif val2 >= 100:
           second_length = 12.06434316353887
        elif val2 >= 50:
            second_length = 11.68831168831169
        else:
            second_length = 13.739802503198966
    else:
        sys.exit()
    stop = "2"

    length = val2
    time_set = length / second_length
    print("time_set: ", time_set)

    arduino = Serial(
        port='COM6',   # Window
        baudrate=9600, # 보드 레이트 (통신 속도)
        timeout=1
    )
    sleep(3)
    while True:
        if arduino.readable():
            try:
                ma = arduino.readline().decode()
                ma = float(ma.strip('\r').strip('\n'))

                if move_input == True:
                    arduino.write(move.encode())
                    move_input = False

                if ma >= thres and not is_start:
                    start = time()
                    start_time = datetime.now().strftime(dateformat)
                    is_start = True
                    is_end = True
                
                # if ma < thres and is_end:
                #     # arduino.write(stop.encode())
                #     # end = time()
                #     act_time = round(exit_time, 2)
                #     save(start_time, end_time, act_time, final_length, val1)
                #     break

                end = time()
                exit_time = end - start
                end_time = datetime.now().strftime(dateformat)
                print(exit_time)
                if exit_time > time_set:
                    arduino.write(stop.encode())
                    final_length = exit_time * second_length
                    act_time = round(time_set, 2)
                    save(start_time, end_time, act_time, round(length, 2), val1)
                    break
            except:
                pass
        else:
            break

value1 = str(sys.argv[1])
value2 = float(sys.argv[2])
sensor(value1, value2)