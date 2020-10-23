import bpy

from ..global_variables import claymation_prefix, claymation_print


class CLAYMATION_OT_go_to_frame(bpy.types.Operator):
    """Go To Claymation Frame"""
    bl_idname = "claymation.go_to_frame"
    bl_label = "Go To Frame"
    bl_options = {'REGISTER','UNDO','INTERNAL'}

    frame = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return context.object.type in {"MESH", "CURVE"}


    def execute(self, context):

        scn = context.scene
        
        if scn.claymation_debug: print(claymation_print + "Going to frame " + self.frame) #debug

        scn.frame_current = int(self.frame)

        return {'FINISHED'}