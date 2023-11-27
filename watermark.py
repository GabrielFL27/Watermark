from PIL import Image
import os

def add_watermark(watermark_path, input_folder, output_folder):
    watermark = Image.open(watermark_path)
    watermark = watermark.resize((1000,1000)) # ajustar o tamanho da marca d'água conforme necessário

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'): # verifica o formato da imagem
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            image.paste(watermark, (image.width - watermark.width, image.height - watermark.height), watermark)
            image.save(os.path.join(output_folder, filename))

# substitir 'caminho_para_a_marca_dagua', 'caminho_para_a_pasta_de_entrada' e 'caminho_para_a_pasta_de_saida' pelos caminhos apropriados
add_watermark('C:\\Users\\Gabriel\\Documents\\Infinity Temporada\\Imagens\\InfinityLogo.png',
              'C:\\Users\\Gabriel\\Documents\\Infinity Temporada\\Imagens\\Watermark\\Verano',
              'C:\\Users\\Gabriel\\Documents\\Infinity Temporada\\Imagens\\Watermark\\VeranoWM')
