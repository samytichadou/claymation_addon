import bpy

from ..global_variables import claymation_prefix, claymation_print
from ..return_claymation_keys import return_claymation_keys


class CLAYMATION_OT_create_frame(bpy.types.Operator):
    """Create Claymation Frame"""
    bl_idname = "claymation.create_frame"
    bl_label = "Create Frame"
    bl_options = {'REGISTER','UNDO'}


    @classmethod
    def poll(cls, context):
        if context.object.type in {"MESH", "CURVE"}:
            try:
                context.object.data.shape_keys.key_blocks[claymation_prefix + str(context.scene.frame_current)]
                return False
            except (AttributeError, KeyError):
                return True


    def execute(self, context):

        scn = context.scene
        obj = context.object

        if scn.claymation_debug: print(claymation_print + "Creating Claymation Frame for " + obj.name) #debug

        # create basis frame if needed
        try:
            obj.data.shape_keys.key_blocks
            if scn.claymation_debug: print(claymation_print + "Creating Base Shape Keys") #debug
        except AttributeError:
            basis_sk = obj.shape_key_add(name='Basis')

        # create new frame
        sk_name = claymation_prefix + str(scn.frame_current)
        new_sk = obj.shape_key_add(name=sk_name)

        for sk in return_claymation_keys(obj):
            sk[0].value = 0

        new_sk.value = 1
            
        obj.active_shape_key_index = len(obj.data.shape_keys.key_blocks)-1

        if scn.claymation_debug: print(claymation_print + "Claymation Frame Created") #debug

        return {'FINISHED'}