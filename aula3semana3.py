produtos = ['tv', 'geladeira', 'fogão', 'microondas', 'liquidificador']
estoque = [10, 5, 8, 15, 20]
produto = input('Digite o nome do produto: ')
if produto in produtos:
    i=produtos.index(produto)
    qtde_estoque = estoque[i]
    print('Temos {} unidades do produto {} em estoque.'.format(qtde_estoque, produto))
else:
    print('Produto não encontrado no estoque.')