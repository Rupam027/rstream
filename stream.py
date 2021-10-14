from os import popen
from mappings import * 

def get_playbacks():
    driver      = popen("pactl list sink-inputs | grep Driver").read().split("\n")
    playbackid  =  popen("pactl list sink-inputs | grep 'Sink Input '").read().split("\n")
    apps    =  popen("pactl list sink-inputs | grep application.process.binary").read().split("\n")
    
    
    n_playback = len(driver)
    playbacks = []
    app_count = 0 
    
    for playback in range(n_playback-1):
        driver_name = driver[playback].split(":")[1].strip()
        _id  = playbackid[playback].split()[2].strip("#")

        if driver_name != "module-loopback.c":
            app_name = apps[app_count].split('=')[1].strip().strip('"')
            playbacks.append((_id , app_name))
            app_count += 1 

    return playbacks


def get_recording_streams():
    
    driver      = popen("pactl list   source-outputs | grep Driver").read().split("\n")
    apps = popen("pactl list source-outputs | grep application.process.binary").read().split("\n")
    recordingid  =  popen("pactl list source-outputs | grep 'Source Output '").read().split("\n")
    apps.remove('')
    n_recording = len(driver)
    recording_streams = []
    app_count = 0

    for recording in range(n_recording-1):
        
        driver_name = driver[recording].split(":")[1].strip()
        _id  = recordingid[recording].split()[2].strip("#")

        if driver_name != "module-loopback.c":
            app_name = apps[app_count].split('=')[1].strip().strip('"')
            recording_streams.append((_id , app_name))
            app_count += 1 
            
    return recording_streams




def start_streaming(src , dest):
    V1 = get_source_id_by_name('V1.monitor')
    V2 = get_sink_id_by_name('V2')

    popen(f'pacmd move-sink-input {src} {V2}')
    popen(f'pacmd move-source-output {dest} {V1}')
        
    


def stop_streaming(src , dest):
    system_source = get_source_id_by_name('alsa_output.pci-0000_00_1f.3.analog-stereo.monitor')
    system_sink   = get_sink_id_by_name('alsa_output.pci-0000_00_1f.3.analog-stereo')

    print(system_source , system_sink)
    
    popen(f'pacmd move-sink-input {src} {system_sink}')
    popen(f'pacmd move-source-output {dest} {system_source}')
    
    

def list_streams_status(streams):

    print("Source-Instance-Id  Source-Instance-Binary Destination-Instance-Id Destination-Instance-Name Status")            

    for stream in streams:
        src  = stream["source"]
        dest = stream["destination"]
        sources , destinations = get_playbacks() , get_recording_streams()
        f1 , f2 = [] , []
        for source in sources :
            if source[1] == src:
                f1.append(source)
                

        for destination in destinations:
            if destination[1] == dest:
                f2.append(destination)


        if f1 == [] or f2 == []:
            print("-----" , src , "-----" , dest , "❌" , sep="\t\t\t")

        for s in f1:
            for d  in f2:
                print(*s , *d ,   "✅" , sep="\t\t\t")
        
        
        
            
            

if __name__ == '__main__' :

    from sys import argv
    import json 

    with open(".stream_config.json" , 'r')  as stream_file : 
        streams = json.load(stream_file)

    argument_count = len(argv)

        
    if argument_count <= 4:
        if argv[1] == "list" :
            list_streams_status(streams["streams"]) 
        elif argv[1] == "start":
            start_streaming(argv[2] , argv[3])
        elif argv[1] == "stop":
            stop_streaming(argv[2] , argv[3])
                       
    else:
        print("Invalid no. of arguments")
    

            
