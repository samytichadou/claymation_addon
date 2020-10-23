import bpy


class CLAYMATION_PT_object_gui(bpy.types.Panel):
    bl_label = "Claymation"
    bl_idname = "CLAYMATION_PT_object_gui"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"


    @classmethod
    def poll(cls, context):
        return context.object.type in {"MESH", "CURVE"}


    def draw(self, context):
        layout = self.layout

        scn = context.scene
        obj = context.object

        row = layout.row()
        row.prop(scn, 'claymation_debug')
        row.prop(scn, 'claymation_update_toggle')

        row = layout.row()
        row.prop(obj.data, 'claymation_mesh')

        row = layout.row()
        row.operator('claymation.create_frame')
        row.operator('claymation.remove_frame')
        row.operator('claymation.remove_datas')