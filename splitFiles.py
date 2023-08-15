import os


def split(file_in, file_out, size):
    file_size = os.path.getsize(file_in)
    chunk_num = 1
    with open(file_in, "rb") as f:
        while True:
            chunk = f.read(size)
            if not chunk:
                break
            chunk_file = os.path.join(
                file_out, str(chunk_num) + "_" + os.path.basename(file_in)
            )
            with open(chunk_file, "wb") as chunk_file:
                chunk_file.write(chunk)
            chunk_num += 1


file_in = "C:\\Python\\files\\20230619.zip"
file_out = "C:\\Python\\splited\\" + (file_in).rsplit("\\", 1)[1].split(".")[0]
size = 5000000  # Byte

if not os.path.exists(file_out):
    os.makedirs(file_out)

split(file_in, file_out, size)
