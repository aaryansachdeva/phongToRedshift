import hou

texture_path_note = hou.ui.selectFile(title="select dir" file_type = houfileType.Directory)
texture_path = hou.expandString(texture_path_note)

print texture_path

materials = hou.selectedNodes()[0]
materials_name - materials.name()

# get all the shaders 

redShaders = materials.parent().createNode('matnet')
redShaders.moveToGoodPosition()

for shd in shaders:
    shd_type = shd.type()name()
    if shd_type == 'material':
        redVopNet = redShaders.createNode('redshift_vopnet', shd.name())
        redMatOutput = redVopNet.children()[0]
        redMat = redVopNet.createNode('redshift::Material')

        # Connect Nodes

        redMatOutput.setInput(0, redMat)

        fbx_shader = shd.glob('* ^suboutput')[0]

        # get texture
        texture = fbx_shader.evalParm('map1')
        texture_name = texture.split("Textures")[1][1:]

        redMat.parm('refl_roughness').set(1)

        if texture != '':
            texture_name = texture.split("Testures")[1][1:]

            rsTex = redVopNet.createNode('redshift::TextureSampler')
            rsTex.parm('tex0').set(texture_path + texture_name)
            redMat.setInput(0, rsTex)

        redVopNet.layoutChildren()
        redShaders.layoutChildren()

redShaders.setName('new_'+materials_name)
update_node = hou.ui.selectNode()

sel_update_node = hou.node(update_node)
num_mats = sel_update_node.parm('num_materials').eval()

for i in range(num_mats):
    i = i+1
    old_path = sel_update_node.evalParm('shop_materialpath%d' %i)
    new_path = old_path.replace("materials", 'new_' + materials_name)
    print old_path, new_path