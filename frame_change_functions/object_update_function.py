import bpy

from ..global_variables import claymation_prefix, claymation_print
from ..return_claymation_keys import return_claymation_keys


def claymation_update_object(object):
    
    context = bpy.context
    scn = context.scene
    current_frame = scn.frame_current

    try:
        object.data.shape_keys.key_blocks
    except AttributeError:
        if scn.claymation_debug: print(claymation_print + "No Shape Keys")
        return False


    sk_list = return_claymation_keys(object)

    idx = -1

    for sk in sk_list:
        if sk[1] == current_frame:
            idx = sk[2]
            if scn.claymation_debug: print(claymation_print + "Toggling On  : " + sk[0].name)
            sk[0].value = 1
        else:
            if scn.claymation_debug: print(claymation_print + "Toggling Off : " + sk[0].name)
            sk[0].value = 0

    if idx == -1:
        for sk in reversed(sk_list):
            if sk[1] < current_frame:
                idx = sk[2]
                if scn.claymation_debug: print(claymation_print + "Toggling On  : " + sk[0].name)
                sk[0].value = 1
                break

    object.active_shape_key_index = idx
