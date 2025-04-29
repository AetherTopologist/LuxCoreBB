import bpy
from bpy.props import FloatProperty, BoolProperty
from ..base import LuxCoreNodeTexture
from ...utils import node as utils_node


class LuxCoreNodeTexBlackbody(LuxCoreNodeTexture, bpy.types.Node):
    bl_label = "Blackbody"
    bl_width_default = 200

    temperature: FloatProperty(update=utils_node.force_viewport_update, name="Temperature", description="Blackbody Temperature in Kelvin",
                               default=6500, min=0, soft_max=13000, step=100, precision=0)

    normalize: BoolProperty(update=utils_node.force_viewport_update, name="Normalize", default=True,
                            description="Bring output from 0-89159.6 to 0-1 range")
    
    def init(self, context):
        self.outputs.new("LuxCoreSocketColor", "Color")

    def draw_buttons(self, context, layout):
        layout.prop(self, "temperature", slider=True)
        layout.prop(self, "normalize")

    def sub_export(self, exporter, depsgraph, props, luxcore_name=None, output_socket=None):
        definitions = {
            "type": "blackbody",
            "temperature": self.temperature,
            "normalize": self.normalize,
        }       
        
        return self.create_props(props, definitions, luxcore_name)
