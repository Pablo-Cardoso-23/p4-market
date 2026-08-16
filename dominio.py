import streamlit as st
from dataclasses import dataclass, field
from typing import List, Optional
import uuid


@dataclass
class ItemCarrinho:
    nome: str
    quantidade: float
    preco_unitario: float = 0.0
    qtd_pacote_promo: Optional[float] = None
    preco_pacote_promo: Optional[float] = None
    
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    @property
    def subtotal(self) -> float:
        """
        Calcula o subtotal. Se houver regra de pacote promocional, 
        calcula quantos pacotes fechados existem e soma o valor dos itens avulsos.
        """
        if self.qtd_pacote_promo and self.preco_pacote_promo:
            lotes = self.quantidade // self.qtd_pacote_promo
            avulsos = self.quantidade % self.qtd_pacote_promo
            
            return (lotes * self.preco_pacote_promo) + (avulsos * self.preco_unitario)
        
        return self.quantidade * self.preco_unitario
    

class CarrinhoDeCompras:
    """
    Encapsula a lista de itens e as operações permitidas no carrinho.
    Isso impede que a interface manipule a lista diretamente.
    """
    def __init__(self):
        self._itens: List[ItemCarrinho] = []

    def adicionar_item(self, item: ItemCarrinho) -> None:
        self._itens.append(item)

    def remover_item(self, item_id: str) -> None:
        self._itens = [item for item in self._itens if item.id != item_id]
        
    def listar_itens(self) -> List[ItemCarrinho]:
        return self._itens

    def buscar_item(self, item_id: str) -> Optional[ItemCarrinho]:
        return next((item for item in self._itens if item.id == item_id), None)

    def atualizar_item(self, item_id: str, item_atualizado: ItemCarrinho) -> None:
        """Substitui os dados de um item existente, mantendo sua identidade (ID)."""
        for i, item in enumerate(self._itens):
            if item.id == item_id:
                item_atualizado.id = item.id
                self._itens[i] = item_atualizado
                break

    @property
    def total_geral(self) -> float:
        return sum(item.subtotal for item in self._itens)
    

def inicializar_estado_carrinho() -> CarrinhoDeCompras:
    """
    Garante que exista uma única instância do CarrinhoDeCompras 
    na sessão do usuário. (Padrão Singleton de Sessão)
    """
    if 'carrinho' not in st.session_state:
        st.session_state.carrinho = CarrinhoDeCompras()
    return st.session_state.carrinho
