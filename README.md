# P4 - Meu Carrinho

O **P4 - Meu Carrinho** é uma aplicação web intuitiva projetada para dar ao consumidor controle total e em tempo real sobre seus gastos de supermercado.

## O Problema e a Solução

**Público-Alvo:** Consumidores do dia a dia que desejam manter o controle rigoroso do orçamento enquanto realizam suas compras.

Durante as idas ao supermercado, é comum o uso de calculadoras ou anotações em papel para somar os valores. Esse processo manual geralmente esbarra em três problemas:
1. **Lentidão:** Perda de tempo realizando cálculos e anotações a cada item adicionado.
2. **Falta de Previsibilidade:** Ausência de um feedback visual e instantâneo de quanto a compra está custando no total.
3. **Desorganização:** Dificuldade em rastrear rapidamente o nome dos itens para saber quais produtos estão pesando mais no orçamento final.

O aplicativo resolve essas dores centralizando a experiência em uma interface de fácil uso pelo celular. O usuário simplesmente insere o nome, valor e unidade do produto, e o sistema entrega um acompanhamento dinâmico, transparente e livre de erros matemáticos.

## Principais Funcionalidades

* **Visibilidade Financeira ao Vivo:** Atualização instantânea do valor total da compra a cada novo item adicionado ou editado.
* **Motor de Promoções em Lote:** Suporte nativo e simplificado para ofertas complexas de mercado (ex: "Leve 3 por R$ 4,50"). O sistema calcula o rateio automaticamente sem exigir matemática mental do usuário.
* **Gestão Ágil:** Edição e remoção de itens em tempo real, com o recálculo do subtotal e totalizador acontecendo instantaneamente.
* **Privacidade *By Design*:** Sem necessidade de logins ou banco de dados. A aplicação roda diretamente na sessão do navegador, garantindo que os dados do usuário permaneçam 100% privados e sejam descartados ao fechar a aba.

## Como executar localmente

1. Clone este repositório para a sua máquina.
2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, utilize: venv\Scripts\activate
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicie o servidor do aplicativo:
    ```bash
    streamlit run app.py
    ```

## Stack Tecnológico

* Python 3
* Stremalit