import bpy

from .global_variables import claymation_prefix, claymation_print


class CLAYMATION_OT_create_frame(bpy.types.Operator):
    """Create Claymation Frame"""
    bl_idname = "claymation.create_frame"
    bl_label = "Create Frame"
    bl_options = {'REGISTER'}


    @classmethod
    def poll(cls, context):
        return context.object.type in {"MESH", "CURVE"}


    def execute(self, context):

        scn = context.scene
        obj = context.object

        if scn.claymation_debug: print(claymation_print + "Creating Claymation Frame for " + obj.name) #debug

        if not obj.data.claymation_mesh:
            obj.data.claymation_mesh = True

        try:
            obj.data.shape_keys.key_blocks
            if scn.claymation_debug: print(claymation_print + "Creating Base Shape Keys") #debug
        except AttributeError:
            basis_sk = obj.shape_key_add(name='Basis')

        sk_name = claymation_prefix + str(scn.frame_current)
        try:
            obj.data.shape_keys.key_blocks[sk_name]
            if scn.claymation_debug: print(claymation_print + "Claymation Frame already exists") #debug
        except (AttributeError, KeyError):
            new_sk = obj.shape_key_add(name=sk_name)
            new_sk.value = 1
            if scn.claymation_debug: print(claymation_print + "Claymation Frame Created") #debug

        return {'FINISHED'}