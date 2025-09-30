from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# DICIONÁRIO GIGANTE PARA UM CARDÁPIO DE RESTAURANTE > ENTRADAS, PRATOS PRINCIPAIS, BEBIDAS, DRINKS E SOBREMESA

cardapio = {
    "entradas": [
        {"nome": "Bruschetta Tradicional", "descricao": "Pão italiano, tomate, manjericão fresco, azeite de oliva e alho", "preco": 18.90},
        {"nome": "Bolinho de Bacalhau", "descricao": "Bacalhau desfiado, batata, salsa e temperos da casa", "preco": 24.50},
        {"nome": "Anéis de Cebola", "descricao": "Cebolas empanadas e fritas, acompanhadas de molho barbecue", "preco": 19.90},
        {"nome": "Cesta de Pães", "descricao": "Variedade de pães artesanais com manteiga de ervas", "preco": 15.00},
        {"nome": "Carpaccio de Carne", "descricao": "Finíssimas fatias de carne bovina com parmesão e rúcula", "preco": 32.00},
        {"nome": "Tábua de Frios", "descricao": "Queijos, salames, presunto parma e azeitonas", "preco": 45.00},
        {"nome": "Mini Quiches", "descricao": "Quiches variados: queijo, espinafre e frango", "preco": 22.90},
        {"nome": "Salada Caprese", "descricao": "Tomate, mussarela de búfala, manjericão e azeite", "preco": 26.90},
        {"nome": "Croquete de Carne", "descricao": "Carne bovina moída temperada e frita", "preco": 21.00},
        {"nome": "Batata Rústica", "descricao": "Batatas assadas com alecrim e sal grosso", "preco": 17.90}
    ],
    "prato principal": [
        {"nome": "Pizza de Calabresa", "descricao": "Massa artesanal, queijo mussarela, cebola e calabresa fatiada", "preco": 45.90},
        {"nome": "Pizza Margherita", "descricao": "Massa artesanal, queijo mussarela, tomate e manjericão", "preco": 42.00},
        {"nome": "Filé à Parmegiana", "descricao": "Filé empanado, molho de tomate, queijo gratinado e arroz com fritas", "preco": 59.90},
        {"nome": "Lasanha Bolonhesa", "descricao": "Massa fresca recheada com molho de carne e queijo", "preco": 55.00},
        {"nome": "Frango Grelhado", "descricao": "Filé de frango grelhado com legumes salteados", "preco": 39.90},
        {"nome": "Peixe ao Molho de Maracujá", "descricao": "Filé de peixe grelhado com molho agridoce de maracujá", "preco": 62.00},
        {"nome": "Risoto de Cogumelos", "descricao": "Arroz arbóreo cremoso com cogumelos frescos", "preco": 58.00},
        {"nome": "Strogonoff de Carne", "descricao": "Tiras de filé mignon ao molho cremoso com arroz e batata palha", "preco": 47.90},
        {"nome": "Hambúrguer Artesanal", "descricao": "Pão brioche, hambúrguer bovino, queijo cheddar, bacon e salada", "preco": 36.90},
        {"nome": "Churrasco Misto", "descricao": "Carne bovina, frango e linguiça servidos com farofa e vinagrete", "preco": 75.00}
    ],
    "bebidas": [
        {"nome": "Refrigerante Lata", "descricao": "Coca-Cola, Guaraná ou Sprite (350ml)", "preco": 6.50},
        {"nome": "Suco Natural", "descricao": "Suco de laranja ou limão espremido na hora (300ml)", "preco": 8.90},
        {"nome": "Água Mineral", "descricao": "Com ou sem gás (500ml)", "preco": 4.50},
        {"nome": "Chá Gelado", "descricao": "Chá preto gelado com limão", "preco": 7.90},
        {"nome": "Água de Coco", "descricao": "Servida gelada (300ml)", "preco": 9.00},
        {"nome": "Suco Detox", "descricao": "Couve, limão, maçã e gengibre", "preco": 11.90},
        {"nome": "Suco de Morango", "descricao": "Suco natural de morango (300ml)", "preco": 10.50},
        {"nome": "Suco de Abacaxi com Hortelã", "descricao": "Refrescante e natural", "preco": 10.90},
        {"nome": "Refrigerante 600ml", "descricao": "Coca-Cola, Guaraná ou Fanta", "preco": 9.90},
        {"nome": "Limonada Suíça", "descricao": "Limão batido com gelo e leite condensado", "preco": 12.00}
    ],
    "drinks": [
        {"nome": "Caipirinha", "descricao": "Cachaça, limão fresco, açúcar e gelo", "preco": 19.90},
        {"nome": "Mojito", "descricao": "Rum, hortelã, limão, açúcar, água com gás e gelo", "preco": 21.90},
        {"nome": "Piña Colada", "descricao": "Rum, leite de coco, suco de abacaxi e gelo", "preco": 23.00},
        {"nome": "Margarita", "descricao": "Tequila, licor de laranja e limão", "preco": 25.00},
        {"nome": "Negroni", "descricao": "Gin, vermute e campari", "preco": 28.00},
        {"nome": "Aperol Spritz", "descricao": "Aperol, prosecco e água com gás", "preco": 27.90},
        {"nome": "Gin Tônica", "descricao": "Gin, tônica e limão siciliano", "preco": 26.00},
        {"nome": "Cosmopolitan", "descricao": "Vodka, licor de laranja, suco de cranberry e limão", "preco": 24.50},
        {"nome": "Bloody Mary", "descricao": "Vodka, suco de tomate, limão e especiarias", "preco": 22.00},
        {"nome": "Whisky Sour", "descricao": "Whisky, limão e açúcar", "preco": 29.00}
    ],
    "sobremesa": [
        {"nome": "Petit Gateau", "descricao": "Bolo de chocolate com recheio cremoso e sorvete de creme", "preco": 22.90},
        {"nome": "Pudim de Leite", "descricao": "Clássico pudim de leite condensado com calda de caramelo", "preco": 14.90},
        {"nome": "Torta de Limão", "descricao": "Massa crocante, creme de limão e merengue", "preco": 18.50},
        {"nome": "Cheesecake de Frutas Vermelhas", "descricao": "Cheesecake com calda de frutas vermelhas", "preco": 21.00},
        {"nome": "Brownie com Sorvete", "descricao": "Brownie de chocolate acompanhado de sorvete de creme", "preco": 19.90},
        {"nome": "Banoffee", "descricao": "Torta de banana, doce de leite e chantilly", "preco": 23.00},
        {"nome": "Mousse de Maracujá", "descricao": "Sobremesa cremosa de maracujá", "preco": 16.00},
        {"nome": "Pavê de Chocolate", "descricao": "Camadas de creme, biscoito e chocolate", "preco": 17.90},
        {"nome": "Gelato Italiano", "descricao": "Sorvete artesanal em diversos sabores", "preco": 20.00},
        {"nome": "Creme Brûlée", "descricao": "Creme de baunilha com crosta de açúcar caramelizado", "preco": 24.00}
    ]
}

@app.route("/")
def menu():
    return render_template("cardapio.html", cardapio=cardapio)

if __name__ == '__main__': 
    app.run(debug=True)