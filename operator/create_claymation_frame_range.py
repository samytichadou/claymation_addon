import bpy

from ..global_variables import claymation_prefix, claymation_print


class CLAYMATION_OT_create_frame_range(bpy.types.Operator):
    """Create Claymation Frame Range"""
    bl_idname = "claymation.create_frame_range"
    bl_label = "Create Range"
    bl_options = {'REGISTER','UNDO'}

    start_frame = bpy.props.IntProperty(name='Start Frame', default=1)
    end_frame = bpy.props.IntProperty(name='End Frame', default=250)


    @classmethod
    def poll(cls, context):
        return context.object.type in {"MESH", "CURVE"}


    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


    def draw(self, context):

        layout = self.layout

        layout.prop(self, 'start_frame')
        layout.prop(self, 'end_frame')


    def execute(self, context):

        scn = context.scene
        obj = context.object

        if scn.claymation_debug: print(claymation_print + "Creating Claymation Frame Range for " + obj.name) #debug

        try:
            obj.data.shape_keys.key_blocks
            if scn.claymation_debug: print(claymation_print + "Creating Base Shape Keys") #debug
        except AttributeError:
            basis_sk = obj.shape_key_add(name='Basis')

        for i in range(self.start_frame, self.end_frame):
            sk_name = claymation_prefix + str(i)
            try:
                obj.data.shape_keys.key_blocks[sk_name]
                if scn.claymation_debug: print(claymation_print + "Claymation Frame %s already exists, skippinng" % str(i)) #debug
            except (AttributeError, KeyError):
                new_sk = obj.shape_key_add(name=sk_name)

        if scn.claymation_debug: print(claymation_print + "Claymation Frame Created") #debug

        return {'FINISHED'}