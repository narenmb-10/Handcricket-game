import random
import math

selected = input("ODD or EVEN ?")

cpu_input = math.ceil(random.random()*6)
player_input = int(input("toss podra dei"))

print("TOSS : YOU : " + str(player_input))
print("TOSS : COM : " + str(cpu_input))

status = ""
if selected == "EVEN":
    if((cpu_input + int(player_input)) %2 ==0):
        status = input("bowl ah \nbat ah ??")
    else:
        choice = random.random()
        if(choice < 0.5):
            print("computer won the TOSS and choose to BAT")
            status = "BOWL"
        else:
            print("computer won the TOSS and choose to BOWL")
            status = "BAT"

if selected == "ODD":
    if((cpu_input + int(player_input)) % 2 ==1):
        status = input("bowling ah bating ah ?? (type BAT or BOWL)")
    else:
        choice = random.random()
        if(choice < 0.5):
            print("computer won the TOSS and chose to BAT")
            status = "BOWL"
        else:
            print("computer won the TOSS and chose to BOWL")
            status = "BAT"


score = 0
target = 1
innings = 1

while True:
    player_input = int(input("you : " + status +  " innings " + str(innings)))
    cpu_input = math.ceil(random.random() * 6)
    print("you : " + str(player_input))
    print("com : " + str(cpu_input))

    if(player_input == cpu_input):
        if(status == "BAT" and innings == 1):
            status = "BOWL"
            innings = 2
            print("OUTTTTTT...")
            print("TO DEFEND : " + str(score))
        elif(status == "BOWL" and innings == 1):
            status = "BAT"
            innings = 2
            print("OUTTTTTT...")
            print("TO GET : " + str(target))
        elif(status == "BAT" and innings == 2):
            print("OUTTTT... COMPUTER WON THE MATCH")
            break
        elif(status == "BOWL" and innings == 2):
            print("OUTTTT.. You WON the MATCH.. vera maarii")
            break
    else:
        if(status == "BAT" and innings == 1):
            score = score + player_input
            print("SCORE : " + str(score))
        elif(status == "BAT" and innings == 2):
            if(target - player_input > 0):
                target = target - player_input
                print("TO GET : " + str(target))
            else:
                print("You WON the MATCH..Podu mass hu..")
                break
        elif(status == "BOWL" and innings == 1):
            target = target + cpu_input
            print("SCORE : " + str(target))
        elif(status == "BOWL" and innings == 2):
            if(score - cpu_input > 0):
                score = score - cpu_input
                print("TO DEFEND : " + str(score))
            else:
                print("You LOST the MATCH . Ayyo Poachi hey (:=(")
                break
