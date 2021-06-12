# python-lex-yacc
Trabalho de Compialdores sobre criar um compilador para a linguagem C.

## Executando 
Utilizando o Visual Studio Code, instale o plugin "Code Runner".
Para executar o arquivo python aperte Ctrl+Alt+N e para parar a execução Ctrl+Alt+M.
Na aba "OUTPUT" terá um print de quando começa e termina a execução.

## Sobre o projeto
Quando executar o arquivo "etapaX_yacc.py", irá gerar dois arquivos chamados de "parser.out" e "parsetab.py".

### Parser.out
Este arquivo possui os estágios (stage) de cada passo a ser tomado segundo as regras ditas ao programa. Este arquivo é um "print" do que está programado no arquivo "parsetab.py".

### Parsetab.py
Este arquivo possui a configuração para gerar as regras e os passos da linguagem, este arquivo gerado não pode ser editado!
## Etapa 1
Apresente a Gramática e os analisadores léxicos e sintáticos para o reconhecimento de
declaração de variáveis no estilo da Linguagem C (leia com atenção as especificações abaixo,
não deve ser implementado nem mais, nem menos).
- Devem reconhecer os tipos: char – int – float
- O char pode ser um caractere ou uma cadeia.
- As variáveis são apenas declaradas, não sendo possível inicializar.
- Identificadores: de acordo com as regras da Linguagem C (iniciam por letras ou _, depois do
segundo caractere pode ser número, letra ou _ e o único caractere especial reconhecido é o _).
- Podes ser declarados individualmente ou por uma lista (sendo lista separados por vírgulas).
- A finalização de cada declaração será por ponto-e-vírgula (;).
- Data de entrega: 29/05/2021 (link: Trabalho Final - Compiladores (Etapa 1)). Essa etapa
contará como a Atividade Semipresencial do dia 29/05/2021.
Peso: 0.5

## Etapa 2
Apresente a Gramática e os analisadores léxicos e sintáticos para o reconhecimento dos
comandos de seleção: if e switch-case, no estilo da Linguagem C.
Comando if:
- Sintaxe: if(condição){<comandos>} else {<comandos>}
- As condições podem ser formadas por qualquer um dos operadores relacionais descritos
abaixo.
- Os comandos serão apenas matemáticos, ou seja, operações matemáticas simples: soma,
subtração, multiplicação e divisão (operadores matemáticos), que serão atribuídos, por meio
dos operadores de atribuição a uma variável.
- A finalização de cada comando será por ponto-e-vírgula (;).
- O comando else é opcional (assim, como na linguagem C)
Comando switch-case:
- Sintaxe: switch(variável){
 case1:{<comandos> break;}
 case2: {<comandos> break;}
 case3: {<comandos> break;}
 default: {<comandos>}
 }
- Mesmas informações do comando if na questão dos comandos.
- A finalização de cada comando será por ponto-e-vírgula (;).
- Os cases podem ser unitários ou até uma quantidade específica ou “livres”.
- O comando default é opcional (assim, como na linguagem C).
* As variáveis devem seguir a Gramática apresentada na declaração de variáveis
(identificadores).
- Data de entrega: 19/06/2021 (link: Trabalho Final - Compiladores (Etapa 2)). Essa etapa
contará como a Atividade Semipresencial do dia 19/06/2021.
Peso: 1.0

## Etapa 3
Apresente a Gramática e os analisadores léxicos e sintáticos para o reconhecimento dos
comandos de repetição: while e for, no estilo da Linguagem C.
Comando while:
- Sintaxe: while(condição){<comandos>}
- As condições podem ser formadas por qualquer um dos operadores relacionais descritos
abaixo.
- Os comandos serão apenas matemáticos, ou seja, operações matemáticas simples: soma,
subtração, multiplicação e divisão (operadores matemáticos), que serão atribuídos, por meio
dos operadores de atribuição a uma variável.
- A finalização de cada comando será por ponto-e-vírgula (;).
Comando for:
- Sintaxe: for(ini_variável; condição; incremento/decremento){<comandos>}
- Mesmas informações do comando while na questão dos comandos e condições.
- A inicialização será por meio de uma atribuição.
- A finalização de cada comando será por ponto-e-vírgula (;).
- As variáveis devem seguir a Gramática apresentada na declaração de variáveis
(identificadores).
- Data de entrega: 29/06/2021 (link: Trabalho Final – Compiladores (Etapa 3)).
Peso: 1.0

## Etapa 4
Entrega das Etapas 1, 2 e 3 agrupadas, com suas devidas funcionalidades.
Os analisadores devem estar operacionais, ou seja, ao inserir comando, os mesmos devem
informar as saídas léxicas e sintáticas, de acordo com cada ferramenta.
Apresentação e explicações do processo de construção do Trabalho, com horário marcado e
tempo de apresentação de 15 minutos.
Ordem de Apresentação, por inscrição, conforme planilha compartilhada com a turma:
https://docs.google.com/spreadsheets/d/1yHCjaXkMIpDOJ9hBHsfLSw_cN6POTj1FI6WYa4F8F8
k/edit?usp=sharing

Data de entrega: 06/07/2021 (link: Trabalho Final – Compiladores (AS)).
Peso: 3.5

## Fonte
- https://www.dabeaz.com/ply/ply.html#ply_nn4
- https://stackoverflow.com/questions/34594597/create-c-parser-with-ply
- https://pemtajo.medium.com/dicas-sobre-ply-python-lex-yacc-1c97519b41e5
- https://github.com/pemtajo/compiler_python