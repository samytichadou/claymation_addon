import bpy

from .global_variables import claymation_prefix


# draw general GUI
def claymation_gui(layout, context):
    scn = context.scene
    obj = context.object

    row = layout.row()
    row.prop(scn, 'claymation_debug')
    row.prop(scn, 'claymation_update_toggle')

    row = layout.row()
    row.prop(obj.data, 'claymation_mesh')

    row = layout.row()
    row.operator('claymation.create_frame', icon='ADD')
    row.operator('claymation.create_frame_range', icon='PREVIEW_RANGE')
    row.operator('claymation.remove_current_frame', icon='X')
    row.operator('claymation.remove_datas', icon='CANCEL')

    # list
    box = layout.box()
    box.label(text='Claymation Frames')
    col = box.column(align=True)

    try:
        chk_fr = False

        for sk in obj.data.shape_keys.key_blocks:
            if sk.name.startswith(claymation_prefix):
                chk_fr = True
                c_frame = sk.name.split(claymation_prefix)[1]
                row = col.row(align=True)
                if str(scn.frame_current) == c_frame:
                    icon = 'RADIOBUT_ON'
                else:
                    icon = 'RADIOBUT_OFF'
                row.operator('claymation.go_to_frame', text='Frame ' + c_frame, icon=icon, emboss=False).frame=c_frame
                #row.label(text="Frame " + c_frame)
                row.operator('claymation.remove_specific_frame', text='', icon='X', emboss=False).frame=c_frame
                
        if not chk_fr:
            col.label(text="No Claymation Frame")
    except AttributeError:
        pass


class CLAYMATION_PT_mesh_gui(bpy.types.Panel):
    bl_label = "Claymation"
    bl_idname = "CLAYMATION_PT_mesh_gui"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"


    @classmethod
    def poll(cls, context):
        return context.object.type in {"MESH", "CURVE"}


    def draw(self, context):
        claymation_gui(self.layout, context)


class CLAYMATION_PT_sculpt_gui(bpy.types.Panel):
    bl_label = "Claymation"
    bl_idname = "CLAYMATION_PT_sculpt_gui"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Claymation"


    @classmethod
    def poll(cls, context):
        if context.object.type in {"MESH", "CURVE"}:
            if context.object.mode in {'SCULPT','OBJECT','EDIT'}:
                return True

    def draw(self, context):
        claymation_gui(self.layout, context)