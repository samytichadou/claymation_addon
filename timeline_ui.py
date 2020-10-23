import bpy
import bpy
import gpu
import blf
import bgl
from gpu_extras.batch import batch_for_shader

from .return_claymation_keys import return_claymation_keys
from .global_variables import claymation_prefix


# draw shader
def drawShader(vertices, indices, color):
    BPM_shader = gpu.shader.from_builtin('2D_UNIFORM_COLOR')
    BMP_batch = batch_for_shader(BPM_shader, 'TRIS', {"pos": vertices}, indices=indices)
    BPM_shader.bind()
    BPM_shader.uniform_float("color", color)
    BMP_batch.draw(BPM_shader,)


# ui draw callback
def drawClaymationTimelineCallbackPx():

    context = bpy.context

    scn = context.scene

    obj = context.object

    region = context.region
        
    if not scn.claymation_timeline_ui: 
        return

    vertices_m = ()
    indices_m = ()
    color_m = (1, 1, 1, 1)
    n_m = 0

    sk_width = 5
    sk_height = 14

    bgl.glEnable(bgl.GL_BLEND) # enable transparency

    if obj.type in {"MESH", "CURVE"}:
        if obj.data.claymation_mesh:

            for sk in return_claymation_keys(obj):
                frame = int(sk.name.split(claymation_prefix)[1])
            
                ### COMPUTE TIMELINE ###
                x1,x2,y1,y2 = frame, frame, -200, 0

                v1r = region.view2d.view_to_region(x1, y1, clip=False)
                v2r = region.view2d.view_to_region(x2, y1, clip=False)

                v1 = v1r[0]-sk_width, 0
                v2 = v2r[0]+sk_width, 0
                v3 = v1r[0]-sk_width, sk_height
                v4 = v2r[0]+sk_width, sk_height 


                vertices_m += (v1, v2, v3, v4)
                indices_m += ((n_m, n_m + 1, n_m + 2), (n_m + 2, n_m + 1, n_m + 3))
                n_m += 4

    #shot state
    drawShader(vertices_m, indices_m, color_m)    

    bgl.glDisable(bgl.GL_BLEND)


#enable callback
cb_handle = []
def enableTimelineUICallback():
    if cb_handle:
        return

    cb_handle.append(bpy.types.SpaceDopeSheetEditor.draw_handler_add(
        drawClaymationTimelineCallbackPx, (), 'WINDOW', 'POST_PIXEL'))


#disable callback
def disableTimelineUICallback():
    if not cb_handle:
        return

    bpy.types.SpaceDopeSheetEditor.draw_handler_remove(cb_handle[0], 'WINDOW')
    cb_handle.clear()


# update function for timeline UI
def updateTimelineUI(self, context):  
    if self.claymation_timeline_ui:
        enableTimelineUICallback()
    else:
        disableTimelineUICallback()

    