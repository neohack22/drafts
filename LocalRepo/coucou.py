#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request
app = Flask(__name__)

@app.route('/sdsdsds')
def dire_coucou():
    return 'Coucou !'


@app.route('/')
def racine():
    return "Le chemin de 'racine' est : " + request.path

@app.route('/la')
def ici():
    return "Le chemin de 'ici' est : " + request.path

@app.route('/contact', methods=['GET'])
def contact_formulaire():
    #afficher le formulaire
    return "if"

@app.route('/contact', methods=['POST'])
def contact_traiter_donnees():
    # traiter les données reçues
    # afficher : "Merci de m'avoir laissé un message !"
    return "else"

if __name__ == '__main__':
    app.run(debug=True)