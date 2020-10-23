import bpy

from .global_variables import claymation_prefix


def return_claymation_keys(obj):

    scn = bpy.context.scene

    claymation_keys = []

    try:
        for sk in obj.data.shape_keys.key_blocks:
            if sk.name.startswith(claymation_prefix):
                claymation_keys.append(sk)
    except AttributeError:
        pass

    return claymation_keys