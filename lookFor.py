import os


def find_texts(path, texts):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, "r") as f:
                    file_content = f.read()
                    for text in texts:
                        if text in file_content:
                            matches.append((root + "/" + filename, text))
            except:
                pass
    return matches


# itens
text = ["PT0002000084164711TD", "PT0002000202190256SL", "PT0002000202178607SJ"]

# diretório
matches = find_texts("C:/Users/elpessoa/desktop/20230621", text)

if len(matches) <= 0:
    print("Nenhum arquivo encontrado.")
elif len(matches) == 1:
    print(str(len(matches)) + " arquivo encontrado.")
else:
    print(str(len(matches)) + " arquivos encontrados.")

# output
for match in matches:
    print(match[0], match[1])
