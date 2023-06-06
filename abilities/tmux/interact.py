import libtmux

def send_echo_hello_world():
    server = libtmux.Server()
    session = server.sessions.get(session_id="$0")
    session.windows[0].panes[0].send_keys('echo hello world', enter=False)
    return "I sent a command to the terminal! Press Enter there if you want to run it"
