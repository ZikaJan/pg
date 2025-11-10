import sys

jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'

def read_header(file_name, header_length):
        with open(file_name, 'rb') as b:
            return b.read(header_length)

def is_jpeg(file_name):
    return read_header(file_name, 2).startswith(jpeg_header)

def is_gif(file_name):
    return read_header(file_name, 6).startswith(gif_header1) or read_header(file_name, 6).startswith(gif_header2)

def is_png(file_name):
    return read_header(file_name, 8).startswith(png_header)

def print_file_type(file_name):
    if is_jpeg(file_name):
        print(f"Soubor {file_name} je typu JPEG")
    elif is_gif(file_name):
        print(f"Soubor {file_name} je typu GIF")
    elif is_png(file_name):
        print(f"Soubor {file_name} je typu PNG")
    else:
        print(f"Soubor {file_name} je neznámého typu")

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except Exception as e:
        print(f"Nastala chyba: {e}")