import bpy

from ..global_variables import claymation_prefix, claymation_print


class CLAYMATION_OT_remove_specific_frame(bpy.types.Operator):
    """Remove Claymation Frame"""
    bl_idname = "claymation.remove_specific_frame"
    bl_label = "Remove Frame"
    bl_options = {'REGISTER','UNDO','INTERNAL'}

    frame : bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return context.object.type in {"MESH", "CURVE"}


    def execute(self, context):

        scn = context.scene
        obj = context.object

        sk_name = claymation_prefix + self.frame

        if scn.claymation_debug: print(claymation_print + "Removing Claymation Frame " + self.frame + " for " + obj.name) #debug

        obj.shape_key_remove(obj.data.shape_keys.key_blocks[sk_name])

        if scn.claymation_debug: print(claymation_print + sk_name + " Removed") #debug

        return {'FINISHED'}