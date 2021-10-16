from os import popen



def get_sink_id_by_name(snk_name):

    sink_ids   = popen("pactl list sinks | grep 'Sink '").read().split("\n")
    sink_names = popen("pactl list sinks | grep Name").read().split("\n")
    n_sinks =   len(sink_ids)

    sink_id_by_name = {}
    
    for sink in range(n_sinks-1):
        sink_id =   sink_ids[sink].split("#")[1]
        sink_name = sink_names[sink].split(":")[1].strip()
        sink_id_by_name[sink_name] = sink_id

    return sink_id_by_name[snk_name]


def get_source_id_by_name(src_name):

    source_ids   =   popen("pactl list sources | grep 'Source '").read().split("\n")
    source_names =   popen("pactl list sources | grep  Name").read().split("\n")
    n_sources = len(source_ids)

    
    source_id_by_name = {}
    
    for source in range(n_sources-1):
        source_id =   source_ids[source].split("#")[1]
        source_name = source_names[source].split(":")[1].strip()
        source_id_by_name[source_name] = source_id

    
    return source_id_by_name[src_name]




