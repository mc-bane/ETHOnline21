from flask import Flask, render_template
import os
import logging
import string

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
    
def index():
    return render_template("index.html")


@app.route('/command')


def command():
    app.logger.info('Processing default request')
    os.system("brownie run ./scripts/number_collectible/mint_and_make_data.py --network rinkeby")
    return "You did it!"
    #return print(os.system("brownie run ./scripts/number_collectible/mint_and_make_data.py --network rinkeby"))
    #return os.system("brownie run ./scripts/number_collectible/create_collectible.py --network rinkeby;brownie run ./scripts/number_collectible/create_metadata.py --network rinkeby;brownie run ./scripts/number_collectible/set_tokenuri.py --network rinkeby")
    #return os.system("brownie run ./scripts/number_collectible/create_collectible.py --network rinkeby;if ($LASTEXITCODE -eq 0) { brownie run ./scripts/number_collectible/create_metadata.py --network rinkeby};if ($LASTEXITCODE -eq 0) { brownie run ./scripts/number_collectible/set_tokenuri.py --network rinkeby} ") 

if __name__ == "__main__":
    app.run()