import os


def func():
    try:
        os._exit(0)  # Success
        # return 0 False
        # exit() False
    finally:
        print('Doing important cleanup')


func()
