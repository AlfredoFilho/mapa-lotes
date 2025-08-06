# Reimportar bibliotecas necessárias após reset
from xml.etree import ElementTree as ET

# Caminho do novo SVG de alta qualidade
svg_input_path = "lotes_cropped.svg"

# Parsear o SVG
tree = ET.parse(svg_input_path)
root = tree.getroot()

# Contador de lotes
lote_id = 1

# Adicionar atributos interativos aos elementos gráficos
for elem in root.iter():
    tag = elem.tag.split('}')[-1]
    if tag in ['rect', 'path', 'polygon']:
        elem.set('class', 'lote')
        elem.set('data-info', f"Lote {lote_id:03d}")
        elem.set('id', f"lote_{lote_id:03d}")
        lote_id += 1

# Caminho para o novo SVG modificado
svg_output_path = "lotes.svg"
tree.write(svg_output_path)

svg_output_path
