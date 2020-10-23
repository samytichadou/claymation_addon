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

    idx = 0

    for sh_k in return_claymation_keys(object):

        if sh_k.name == claymation_prefix + str(current_frame):
            if scn.claymation_debug: print(claymation_print + "Toggling On  : " + sh_k.name)
            sh_k.value = 1

            object.active_shape_key_index = idx

        else:
            if scn.claymation_debug: print(claymation_print + "Toggling Off : " + sh_k.name)
            sh_k.value = 0

        idx += 1