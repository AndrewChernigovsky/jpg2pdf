from PIL import Image
import os
import webbrowser

images_dir = 'images'

jpg_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
jpg_files.sort(key=lambda x: int(x.split('.')[0]))
images = [Image.open(os.path.join(images_dir, file)) for file in jpg_files]
pdf_file = 'output/output.pdf'
images[0].save(pdf_file, 'PDF', save_all=True, append_images=images[1:])
print(f'Файлы преобразованы в {pdf_file}')

webbrowser.open('file://' + os.path.abspath(pdf_file))