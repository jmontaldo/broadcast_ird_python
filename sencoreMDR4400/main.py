from sintonizar import sintonizar
import os, json, subprocess

def buscar(value) -> str:

    dir = os.path.dirname(os.path.abspath(__file__))
    file_path = dir + r"\señales.json"
    with open(file_path, "r") as file:
        datos = json.load(file)
    drm = value
    for data in datos:
        if  drm == data["DRM"]:
            multicast = data["Multicast"]
            interface = data["Interface"]
            puerto = data["Puerto"]
            orion = data["Orion"]
            subprocess.run(["C:/Program Files/Mozilla Firefox/firefox.exe", orion])
            data = sintonizar(multicast, interface, puerto)
            found = True
            break
        else:
            found = False
            pass
    if found != True:
        return "No encontrado"
    
    print("\nSTATUS:")
    try:
        audio_value = []
        video_bitrate = int(data["val"]["groups"]["Video"]["rows"][0]["videoAverageBitrate"]) / 1000000
        audios = [data["val"]["groups"]["SelectedAudio"]["rows"][3]["selectedaudioType"], data["val"]["groups"]["SelectedAudio"]["rows"][0]["selectedaudioType"], ]
        for audio_type in audios:
            if (audio_type == "4"):
                audio_value.append('Dolby Digital')
            elif (audio_type == "9") or (audio_type == "8"):
                audio_value.append('AAC')
            elif (audio_type == '10'):
                audio_value.append('No audio')
            else:
                audio_value.append('PCM')
        mensaje = f"""Service Name: {data["val"]["groups"]["SelectedService"]["rows"][0]["selectedserviceServiceName"]}
        \nVideo PID: {data["val"]["groups"]["SelectedService"]["rows"][0]["selectedserviceVideoPid"]}
        \nVideo Format: {data["val"]["groups"]["Video"]["rows"][0]["videoWidth"]} x {data["val"]["groups"]["Video"]["rows"][0]["videoHeight"]}i
        \nVideo Bitrate: {video_bitrate} Mbps
        \nAudio 1 PID: {data["val"]["groups"]["SelectedAudio"]["rows"][3]["selectedaudioPid"]}
        \nAudio 2 PID: {data["val"]["groups"]["SelectedAudio"]["rows"][0]["selectedaudioPid"]}
        \nAudio 1 type: {audio_value[0]}
        \nAudio 2 type: {audio_value[1]}"""
    except KeyError:
        mensaje = "Sin status/No encontrado"
    return mensaje