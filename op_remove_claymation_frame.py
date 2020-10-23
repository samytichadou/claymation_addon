import bpy

from .global_variables import claymation_prefix, claymation_print


class CLAYMATION_OT_remove_frame(bpy.types.Operator):
    """Remove Claymation Frame"""
    bl_idname = "claymation.remove_frame"
    bl_label = "Remove Frame"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        if context.object.type in {"MESH", "CURVE"}:
            try:
                context.object.data.shape_keys.key_blocks[claymation_prefix + str(context.scene.frame_current)]
                return True
            except (AttributeError, KeyError):
                return False


    def execute(self, context):

        scn = context.scene
        obj = context.object

        sk_name = claymation_prefix + str(context.scene.frame_current)

        if scn.claymation_debug: print(claymation_print + "Removing Claymation Frame for " + obj.name) #debug

        obj.shape_key_remove(obj.data.shape_keys.key_blocks[sk_name])

        if scn.claymation_debug: print(claymation_print + sk_name + " Removed") #debug

        return {'FINISHED'}