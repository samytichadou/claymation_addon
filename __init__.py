'''
Copyright (C) 2018 Samy Tichadou (tonton)
samytichadou@gmail.com

Created by Samy Tichadou (tonton)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {  
 "name": "Claymation",  
 "author": "Samy Tichadou (tonton)",  
 "version": (0, 1, 0),  
 "blender": (2, 83, 7), 
 "location": "Properties Editor > Object Data",  
 "description": "Utilities to create and use per frame Shape Keys",  
 "wiki_url": "https://github.com/samytichadou/claymation_addon/blob/master/README.md",  
 "tracker_url": "https://github.com/samytichadou/claymation_addon/issues/new",
 "category": "Animation",
 "warning": "Beta version, use at your own risks"
 }


import bpy


# IMPORT SPECIFICS
##################################

from .gui import CLAYMATION_PT_object_gui

from .frame_change_handler import claymation_frame_change

from .op_create_claymation_frame import CLAYMATION_OT_create_frame
from .op_remove_claymation_frame import CLAYMATION_OT_remove_frame

# register
##################################

classes = (

            CLAYMATION_PT_object_gui,
            CLAYMATION_OT_create_frame,
            CLAYMATION_OT_remove_frame,
        )

def register():

    ### OPERATORS ###
    from bpy.utils import register_class
    for cls in classes :
        register_class(cls)

    ### PROPERTIES ###
    bpy.types.Scene.claymation_debug = \
        bpy.props.BoolProperty(name="Debug")

    bpy.types.Scene.claymation_update_toggle = \
        bpy.props.BoolProperty(name="Update")

    bpy.types.Mesh.claymation_mesh = \
        bpy.props.BoolProperty(name="Claymation Mesh")

    bpy.types.Curve.claymation_mesh = \
        bpy.props.BoolProperty(name="Claymation Curve")

    ### HANDLER ###
    bpy.app.handlers.frame_change_post.append(claymation_frame_change)


def unregister():
   
    ### OPERATORS ###
    from bpy.utils import unregister_class
    for cls in reversed(classes) :
        unregister_class(cls)

    ### PROPERTIES ###
    del bpy.types.Scene.claymation_debug
    del bpy.types.Scene.claymation_update_toggle
    del bpy.types.Mesh.claymation_mesh
    del bpy.types.Curve.claymation_mesh

    ### HANDLER ###
    bpy.app.handlers.frame_change_post.remove(claymation_frame_change)
