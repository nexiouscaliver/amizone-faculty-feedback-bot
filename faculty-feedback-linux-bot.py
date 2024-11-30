import pyautogui
import time

def goto_selection(value):
    if value == "neutral":
        pyautogui.moveTo(1469, 804, duration=0.5)
    elif value == "agree":
        pyautogui.moveTo(1368, 804, duration=0.5)
    elif value == "disagree":
        pyautogui.moveTo(1579, 804, duration=0.5)
    elif value == "strongly-disagree":
        pyautogui.moveTo(1708, 804, duration=0.5)


def click_radio_buttons():
    pyautogui.click()
    time.sleep(1)

def scroll_next_section():
    pyautogui.scroll(-205)  
    time.sleep(.5)  

def scroll_next_box():
    pyautogui.scroll(-62)
    time.sleep(.5)  

def scroll_to_top():
    pyautogui.scroll(1000)
    time.sleep(.5)


#main:
def main():
    sel = ['agree' , 'neutral' , 'disagree' , 'strongly-disagree']
    selection = input("Enter your selection (agree , neutral , disagree , strongly-disagree): ")
    if selection not in sel:
        print("Invalid selection. Retry and use the correct selection from given options.")
        main()
    else:
        print("You have 5 seconds to move your mouse to the Amizone website...")
        time.sleep(5)
        scroll_to_top()
        goto_selection(selection)
        for i in range(0,3):
            click_radio_buttons()
            scroll_next_box() 
        click_radio_buttons()    
        scroll_next_section()
        for i in range(0,6):
            click_radio_buttons()
            scroll_next_box()
        click_radio_buttons()
        scroll_next_section()
        for i in range(0,5):
            click_radio_buttons()
            scroll_next_box()
        click_radio_buttons()
        scroll_next_section()
        for i in range(0,3):
            click_radio_buttons()
            scroll_next_box()
        click_radio_buttons()
        scroll_next_section()
        for i in range(0,3):
            click_radio_buttons()
            scroll_next_box()
        click_radio_buttons()
        print("Feedback submitted successfully!")

#call main
main()
