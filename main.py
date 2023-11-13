import pyautogui
import time

groups = ["5788619454491964", "3092811364081112" , "programming99", "learnhtmlcssandjavascript",
          '2721043967919998',"2653015128320341",'2616981278627207',"2575941032667407","devinfodarijamaroc",
          '2091890167764241',"HTML5.JavaScript.CSS3.Learn","programming.jokes","programmershub1","ElzeroWebSchool"]

time.sleep(5)

pyautogui.keyDown("ctrl")
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')




for i in range(len(groups)):
    link = "www.facebook.com/groups/" + groups[i]
    pyautogui.typewrite(link)
    time.sleep(3)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')


    print('waiting for search')
    time.sleep(10)

    pyautogui.typewrite("p")
    time.sleep(5)
    print('writing post ...')
    pyautogui.typewrite(" recorder app using javascript in arabic    : www.youtube.com/watch?v=ZfCQqDLnbRA&t")

    time.sleep(5)

  
    pyautogui.moveTo(424,648)
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(434,629)
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(434,610)
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)
    pyautogui.typewrite(["f6"])
    time.sleep(1)