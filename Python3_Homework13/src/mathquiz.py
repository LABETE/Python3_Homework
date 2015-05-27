from random import randint
from datetime import datetime, timedelta

def seconds_counter(start_time_seconds, now_time_seconds):
    """
    Take two times in seconds and return the difference 
    """
    if start_time_seconds > now_time_seconds:
        delta_seconds = timedelta(seconds=60)
        now_time_seconds = now_time_seconds + delta_seconds.seconds
    seconds = now_time_seconds - start_time_seconds
    return seconds

def quiz(in1=None, in2=None):
    questions_dict = {}
    total_seconds = 0
    for num_question in range (1, 6):
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        start_time = datetime.now()
        try:
            if in1 and in2:
                return int(in1+in2)
            else:
                answer = int(input("what is the sum of {0} and {1}? ".format(num1, num2)))
        except ValueError:
            raise "Input should be integer"
        now = datetime.now()
        seconds = seconds_counter(start_time.second, now.second)
        expected = num1 + num2
        if answer == expected:
            questions_dict[num_question] = (seconds, "right")
            print("{0} is right!".format(answer))
        else:
            questions_dict[num_question] = (seconds, "wrong")
            print("{0} is wrong!".format(answer))
    for key, val in questions_dict.items():
        print("Question #{0} took about {1} seconds to complete and was {2}.".format(key, val[0], val[1]))
        total_seconds += val[0]
    average_time = total_seconds / 5
    print("You took {0} seconds to finish the quiz".format(total_seconds))
    print("Your average time was {0} seconds per question".format(average_time))    

if __name__ == "__main__":
    pass
    #quiz()