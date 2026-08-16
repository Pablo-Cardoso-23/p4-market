import streamlit as st
from dominio import ItemCarrinho, CarrinhoDeCompras

st.set_page_config(
    page_title="Meu Carrinho App", 
    layout="centered"
)

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = CarrinhoDeCompras()

if 'id_em_edicao' not in st.session_state:
    st.session_state.id_em_edicao = None

carrinho: CarrinhoDeCompras = st.session_state.carrinho

item_em_edicao = None
if st.session_state.id_em_edicao:
    item_em_edicao = carrinho.buscar_item(st.session_state.id_em_edicao)

st.title("P4 - Meu Carrinho")
st.markdown("Acompanhe seus gastos no mercado em tempo real.")

titulo_expander = "Editar Produto" if item_em_edicao else "Adicionar Novo Produto"

with st.expander(titulo_expander, expanded=True):
    form_key = f"form_item_{st.session_state.id_em_edicao if item_em_edicao else 'novo'}"
    
    with st.form(form_key, clear_on_submit=True):
        col1, col2 = st.columns([3, 1])
        
        nome = col1.text_input(
            "Nome do Produto (ex: Whey Protein)", 
            value=item_em_edicao.nome if item_em_edicao else ""
        )
        quantidade = col2.number_input(
            "Qtd Levada", 
            min_value=0.1, 
            value=float(item_em_edicao.quantidade) if item_em_edicao else 1.0, 
            step=1.0
        )
        
        preco_unitario = st.number_input(
            "Preço Unitário Normal (R$)", 
            min_value=0.0, 
            value=float(item_em_edicao.preco_unitario) if item_em_edicao else 0.0, 
            step=0.1, 
            format="%.2f"
        )
        
        st.markdown("---")
        st.markdown("**Regra de Promoção (Opcional)**")
        st.caption("Ex: Leve 3 por R$ 5,60")
        
        col3, col4 = st.columns(2)
        
        val_qtd_promo = float(item_em_edicao.qtd_pacote_promo) if (item_em_edicao and item_em_edicao.qtd_pacote_promo) else 0.0
        qtd_pacote_promo = col3.number_input(
            "Qtd do Pacote (O 'Leve X')", 
            min_value=0.0, 
            value=val_qtd_promo, 
            step=1.0
        )
        
        val_preco_promo = float(item_em_edicao.preco_pacote_promo) if (item_em_edicao and item_em_edicao.preco_pacote_promo) else 0.0
        preco_pacote_promo = col4.number_input(
            "Preço do Pacote (O 'Por R$ Y')", 
            min_value=0.0, 
            value=val_preco_promo, 
            step=0.1, 
            format="%.2f"
        )
        
        col_submit, col_cancel = st.columns(2)
        label_btn = "Salvar Alterações" if item_em_edicao else "Adicionar ao Carrinho"
        
        submit = col_submit.form_submit_button(label_btn, use_container_width=True)
        
        cancelar = False
        if item_em_edicao:
            cancelar = col_cancel.form_submit_button("Cancelar Edição", use_container_width=True)
        
        if cancelar:
            st.session_state.id_em_edicao = None
            st.rerun()
            
        elif submit:
            if not nome.strip():
                st.error("Por favor, insira o nome do produto.")
            else:
                q_promo = qtd_pacote_promo if qtd_pacote_promo > 0 else None
                p_promo = preco_pacote_promo if preco_pacote_promo > 0 else None
                
                item_montado = ItemCarrinho(
                    nome=nome.strip(),
                    quantidade=quantidade,
                    preco_unitario=preco_unitario,
                    qtd_pacote_promo=q_promo,
                    preco_pacote_promo=p_promo
                )
                
                if item_em_edicao:
                    carrinho.atualizar_item(st.session_state.id_em_edicao, item_montado)
                    st.session_state.id_em_edicao = None
                    st.success("Produto atualizado com sucesso!")
                else:
                    carrinho.adicionar_item(item_montado)
                    st.success("Produto adicionado com sucesso!")
                    
                st.rerun()

st.header("Seus Itens")

itens = carrinho.listar_itens()

if not itens:
    st.info("Seu carrinho está vazio. Adicione o primeiro item acima.")
else:
    col_n, col_q, col_p, col_s, col_acao = st.columns([3, 1, 2, 2, 2])
    col_n.caption("Produto")
    col_q.caption("Qtd")
    col_p.caption("Preço")
    col_s.caption("Subtotal")
    col_acao.caption("Ações")
    st.divider()

    for item in itens:
        col_nome, col_qtd, col_preco, col_sub, col_botoes = st.columns([3, 1, 2, 2, 2])
        
        col_nome.markdown(f"**{item.nome}**")
        col_qtd.write(f"{item.quantidade}x")
        
        if item.qtd_pacote_promo is not None:
            col_preco.write("Promoção")
        else:
            col_preco.write(f"R$ {item.preco_unitario:.2f}")
            
        col_sub.write(f"**R$ {item.subtotal:.2f}**")
        
        btn_edit, btn_del = col_botoes.columns(2)
        
        if btn_edit.button("Editar", key=f"edit_{item.id}"):
            st.session_state.id_em_edicao = item.id
            st.rerun()
            
        if btn_del.button("Remover", key=f"del_{item.id}"):
            if st.session_state.id_em_edicao == item.id:
                st.session_state.id_em_edicao = None
            carrinho.remover_item(item.id)
            st.rerun()
            
    st.divider()
    
    total = carrinho.total_geral
    
    st.metric(label="Valor Total da Compra", value=f"R$ {total:.2f}")