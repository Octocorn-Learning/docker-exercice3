from app import app

from app.controller.BeerController import BeerController

@app.route('/api/beers')
def getBeers():
    return BeerController().getBeers()

@app.route('/api/ca-fab')
def getCAByFabricant():
    return BeerController().getCAByFabricant()

@app.route('/api/variation')
def getVariation():
    return BeerController().getVariation()

@app.route('/')
def home():
    return BeerController().doc()