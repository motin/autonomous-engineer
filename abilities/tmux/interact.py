import libtmux

def send_echo_hello_world():
    server = libtmux.Server()
    session = server.sessions.get(session_id="$0")
    session.windows[0].panes[0].send_keys('echo hello world', enter=False)
    return "I sent a command to the terminal! Press Enter there if you want to run it"

def split_pane_vertically():
    server = libtmux.Server()
    session = server.list_sessions()[0]
    # Split pane vertically
    session.split_window(vertical=True, attach=False)
    return "Pane split vertically"

def split_pane_horizontally():
    server = libtmux.Server()
    session = server.list_sessions()[0]
    # Split pane vertically
    session.split_window(vertical=False, attach=False)
    return "Pane split horizontally"
