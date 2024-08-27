import curses
from datetime import datetime
from curses import wrapper



import curses

def start_screen(stdscr):
    # Clear the screen
    stdscr.clear()

    # Display welcome message
    stdscr.addstr("Welcome to the WPM TEST")
    stdscr.addstr("\nPress any key to begin")

    # Refresh the screen to show the text
    stdscr.refresh()

    stdscr.getch()
    # Wait for user input

def handle_wpm(stdscr,target_text,current_type):
    stdscr.addstr(target_text+"\n")
    for i,char in enumerate(current_type):
        if target_text[i] == char:
            stdscr.addstr(0,i,char,curses.color_pair(1))
        else :
            stdscr.addstr(0,i,target_text[i],curses.color_pair(2))


def calculateTimeSpan(start_time,end_time,wpm_values,current_input):
    timeSpan = (end_time-start_time).total_seconds()
    wpm = (len(current_input) / 5) / (timeSpan / 60)
    wpm_values.append(wpm)

def display_wpm(stdscr):
    target_text = "In ancient times, storytellers would gather around the fire to recount tales of heroism"
    current_type = []
    start_timing = None
    current_input = ""
    wpm_values = []
    while True:
        stdscr.clear()
        handle_wpm(stdscr,target_text,current_type)
        stdscr.refresh()
        if start_timing == None:
            start_timing = datetime.now()
        key  = stdscr.getkey()
        current_input += key
        end_time = datetime.now()
        if key == '\n':
            break
        elif key in ("KEY_BACKSPACE",'\b',"\x7f"):
            if(len(current_type) > 0):
                current_type.pop()
        else:
            if(len(current_type) < len(target_text)):
                calculateTimeSpan(start_timing,end_time,wpm_values,current_input)
                current_type.append(key)
    avg_wpm = sum(wpm_values) / len(wpm_values)
    stdscr.addstr(1, 0, f"Average WPM: {avg_wpm:.2f}")
    stdscr.refresh()
    stdscr.getkey()

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    start_screen(stdscr)
    display_wpm(stdscr)

# Initialize curses and run the main function
curses.wrapper(main)





