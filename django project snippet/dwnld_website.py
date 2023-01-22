
import requests

def download(url, path, chunk=2048):    #url and path to be downloaded to as arguments
    req = requests.get(url, stream=True)    #requests the url as an argument
    if req.status_code == 200:  #status code is OK
        with open(path, 'wb') as f:     #
            for chunk in req.iter_content(chunk):
                f.write(chunk)
            f.close()
        return path
    raise Exception('Given url is return status code:{}'.format(req.status_code))

download('https://www.gutenberg.org/cache/epub/47407/pg47407.txt', r'C:\Users\kkors\guttenberg1.txt', chunk=2048)