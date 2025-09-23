import webbrowser

url = 'https://docs.python.org/'

is_session_already_open = False

# Open URL in a new tab, if a browser window is already open.
try:
    is_session_already_open = webbrowser.open_new_tab(url)
except ValueError:
    print("It seems like we dont support your browser")

# Open URL in new window, raising the window if possible.
if is_session_already_open == False:
    try:
        webbrowser.open_new(url)
    except ValueError:
        print("It seems like we dont support your browser")
