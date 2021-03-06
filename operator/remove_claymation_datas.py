import bpy

from ..global_variables import claymation_prefix, claymation_print


class CLAYMATION_OT_remove_datas(bpy.types.Operator):
    """Remove Claymation Datas"""
    bl_idname = "claymation.remove_datas"
    bl_label = "Remove Datas"
    bl_options = {'REGISTER','UNDO'}


    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj.type in {"MESH", "CURVE"}:
            try:
                for sk in obj.data.shape_keys.key_blocks:
                    if sk.name.startswith(claymation_prefix):
                        return True
            except (AttributeError):
                return False


    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


    def draw(self, context):

        layout = self.layout

        layout.label(text="All Claymation Datas will be lost", icon="ERROR")
        layout.label(text="Continue ?")


    def execute(self, context):

        scn = context.scene
        obj = context.object

        if scn.claymation_debug: print(claymation_print + "Removing Claymation Datas for " + obj.name) #debug

        try:
            for sk in obj.data.shape_keys.key_blocks:
                if sk.name.startswith(claymation_prefix):
                    obj.shape_key_remove(sk)

        except AttributeError:
            pass

        if scn.claymation_debug: print(claymation_print + "Claymation Datas for %s Removed" % obj.name) #debug

        return {'FINISHED'}