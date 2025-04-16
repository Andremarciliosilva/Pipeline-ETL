<h4> Pipeline-ETL </h4>

Análise de Vendas de Produtos 

Objetivo: Dado três arquivos CSV's contendo dados de vendas de produtos, o desafio consiste em ler os dados, concatenar os arquivos, processá-los em um dicionário para análise e, por fim, calcular e reportar as vendas totais por categoria de produto.

<div align="center"> <h3>Fluxograma<h3> </div>

<div align="center"> 
<img src="fluxograma.png" alt="Fluxograma">
</div>



<h4> Tarefas: </h4>

<li>Ler o arquivo CSV e carregar os dados. </li>
<li>Processar os dados em um dicionário, onde a chave é a categoria, e o valor é uma lista de dicionários, cada um contendo informações do produto (Produto, Quantidade, Venda).</li>
<li>Calcular o total de vendas (Quantidade * Venda) por categoria.</li><br>


Os resultados foram:

O total de vendas de cada produto é:
{'Meia': 23220.9, 'Camiseta': 73734.9, 'Mochila': 95402.1, 'Boné': 58674.9, 'Tênis': 68992.8, 'Calça': 73947.6, 'Jaqueta': 47664.1}