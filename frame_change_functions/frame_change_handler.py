import bpy
from bpy.app.handlers import persistent


from .frame_update_function import claymation_update_object
from ..global_variables import claymation_print

### HANDLER ###
@persistent
def claymation_frame_change(scene):

    if scene.claymation_update_toggle:
        if scene.claymation_debug: print(claymation_print + "Update") #debug

        for obj in scene.objects:
            if obj.type in {"MESH", "CURVE"}:
                if obj.data.claymation_mesh:
                    if scene.claymation_debug: print(claymation_print + "Updating " + obj.name) #debug
                    claymation_update_object(obj)