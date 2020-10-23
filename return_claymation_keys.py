import bpy

from .global_variables import claymation_prefix


def return_claymation_keys(obj):

    claymation_keys = []

    try:
        for sk in obj.data.shape_keys.key_blocks:
            if sk.name.startswith(claymation_prefix):
                claymation_keys.append([sk, int(sk.name.split(claymation_prefix)[1])])
    except AttributeError:
        pass
    sorted_keys = sorted(claymation_keys, key=lambda key: key[1])
    
    return sorted_keys