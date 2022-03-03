import sys
import traceback
import time


def get_exception_info():
    try:
        exception_type, exception_value, exception_traceback = sys.exc_info()
        file_name, line_number, procedure_name, line_code = traceback.extract_tb(
            exception_traceback)[-1]
        exception_info = ''.join('[Time Stamp]: ' + str(time.strftime('%d-%m-%Y %I:%M:%S %p')) + '' + '[File Name]: ' + str(file_name) + ' ' + '[Procedure Name]: ' + str(procedure_name) + ' ' + '[Error Message]: ' + str(exception_value) + ' '
                                 + '[Error Type]: ' +
                                 str(exception_type) + ' '
                                 + '[Line Number]: ' +
                                 str(line_number) + ' '
                                 + '[Line Code]: ' + str(line_code))
    except:
        pass
    return exception_info


def division_by_zero():
    try:
        division = 1/0
    except:
        exception_info = get_exception_info()
        print(exception_info)
    finally:
        pass


def main():
    # a = "Java"
    # if a != "Python":
    #     raise Exception("a is not equal Python")

    division_by_zero()


if __name__ == '__main__':
    main()
