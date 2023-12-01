def stop_story():
    global step
    step = 0


while step > 0:
    if step == 1:
        print("Вы пришли к развилке ")
        print("куда идти")
        print("направо 0")
        print("налево 1")
        answer = int(input())
        if answer == 0:
            print("Вы пошли направо")
            step = 2
        if answer == 1:
            print("вы пошли налево")
            step = 3
    if step == 2:
        print("Вы пришли к развилке")
        print("Куда идти")
        print("направо 0")
        print("налево 1")
        answer = int(input())
        if answer == 0:
            print("Вы пошли направо")
            print("Вы умерли")
            raise SystemExit
        if answer == 1:
            print("вы пошли налево")
            step = 3
