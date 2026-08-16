from dominio import ItemCarrinho, CarrinhoDeCompras

def test_calculo_subtotal_padrao():
    # Arrange (Preparar)
    item = ItemCarrinho(nome="Arroz 5kg", quantidade=2.0, preco_unitario=25.0)
    
    # Act (Agir)
    resultado = item.subtotal
    
    # Assert (Verificar)
    assert resultado == 50.0  # 2 * 25

def test_calculo_subtotal_com_promocao():
    # Arrange
    # Promoção: Leve 3 por R$ 4,50 (Ignora o preço unitário se fornecido)
    item = ItemCarrinho(
        nome="Molho de Tomate", 
        quantidade=3.0, 
        preco_unitario=2.0, # Preço normal seria 6.0
        preco_promocional_total=4.50 
    )
    
    # Act
    resultado = item.subtotal
    
    # Assert
    assert resultado == 4.50

def test_adicionar_item_no_carrinho():
    # Arrange
    carrinho = CarrinhoDeCompras()
    item = ItemCarrinho(nome="Feijão", quantidade=1.0, preco_unitario=8.0)
    
    # Act
    carrinho.adicionar_item(item)
    
    # Assert
    assert len(carrinho.listar_itens()) == 1
    assert carrinho.listar_itens()[0].nome == "Feijão"

def test_remover_item_do_carrinho():
    # Arrange
    carrinho = CarrinhoDeCompras()
    item1 = ItemCarrinho(nome="Macarrão", quantidade=2.0, preco_unitario=4.0)
    item2 = ItemCarrinho(nome="Azeite", quantidade=1.0, preco_unitario=30.0)
    
    carrinho.adicionar_item(item1)
    carrinho.adicionar_item(item2)
    
    # Act
    carrinho.remover_item(item1.id) # Usando o ID único (UUID)
    
    # Assert
    itens_restantes = carrinho.listar_itens()
    assert len(itens_restantes) == 1
    assert itens_restantes[0].nome == "Azeite"

def test_calculo_total_geral_do_carrinho():
    # Arrange
    carrinho = CarrinhoDeCompras()
    
    # Produto normal: 2 x 10 = 20.0
    item_normal = ItemCarrinho(nome="Café", quantidade=2.0, preco_unitario=10.0)
    
    # Produto em promoção: Total fechado de 4.50
    item_promo = ItemCarrinho(nome="Molho", quantidade=3.0, preco_promocional_total=4.50)
    
    carrinho.adicionar_item(item_normal)
    carrinho.adicionar_item(item_promo)
    
    # Act
    total = carrinho.total_geral
    
    # Assert
    assert total == 24.50  # 20.0 + 4.50