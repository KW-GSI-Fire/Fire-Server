from remotes import send_server

temperature = None
temperature_level = None
box_opened = None
statusUpdated = None


def writeStatus(raw, use_remote):
    global temperature
    global temperature_level
    global box_opened
    global statusUpdated

    statusUpdated = False

    data = raw.split(':')

    if data[0] == 't':
        if temperature_level != data[2]:
            statusUpdated = True
            temperature_level = data[2]

        temperature = float(data[1])

    elif data[0] == 'b':
        if box_opened != bool(int(data[1])):
            statusUpdated = True
            box_opened = bool(int(data[1]))

    else:
        pass

    # need to update if use remote server
    if use_remote:
        # if statusUpdated:
        #     send_server.updateStatusToRemote(data[0], readStatus(data[0]))
        send_server.updateStatusToRemote(data[0], readStatus(data[0]))


def readStatus(status_type):
    global temperature
    global temperature_level
    global box_opened

    if status_type == 't':
        return {"temperature": temperature, "level": temperature_level}
    
    elif status_type == 'b':
        return {"box_opened": box_opened}
    
    else:
        return None
