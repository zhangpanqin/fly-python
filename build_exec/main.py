import os
import pathlib

if __name__ == '__main__':
    folder = pathlib.Path(__file__).parent.resolve()
    print(folder)
    client_secret_path = os.path.join(folder,"secret", "client_secret.json")
    with open(client_secret_path) as file:
        print(file.read())