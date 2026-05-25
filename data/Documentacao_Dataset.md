# Documentação - Dataset

Os documentos abaixo compõem a base de conhecimento do JARVIS Acadêmico, indexados via RAG (*Retrieval-Augmented Generation*) com embeddings e armazenados no banco vetorial ChromaDB. Todos os arquivos estão na pasta `data/documentos/pdfs/`.

## Estratégia de Chunking

Todos os documentos passam pelo mesmo pipeline de processamento:

1. **Extração de texto:** via `pypdf` (`PdfReader`), página por página.
2. **Divisão em chunks:** realizada pela função `chunk_text()` em `app/rag/chunking.py`.
3. **Geração de embeddings:** via `sentence-transformers`.
4. **Indexação:** armazenados no ChromaDB em `data/chroma/`.

### Parâmetros do chunking:
* **Tamanho do Chunk (`chunk_size`):** 500 caracteres por chunk
* **Sobreposição (`overlap`):** 100 caracteres de sobreposição entre chunks consecutivos
* **Estratégia:** *Sliding window* (janela deslizante), sem divisão semântica.

---

## Documentos

### 1. Camada de Transporte - Primeira parte.pdf
* **Origem:** Slides de aula - Disciplina de Redes de Computadores
* **Tipo:** Slides de aula (PDF exportado de apresentação)
* **Tamanho:** 1,7 MB
* **Conteúdo:** Introdução à camada de transporte do modelo OSI/TCP-IP. Aborda os conceitos de multiplexação, demultiplexação, comunicação processo a processo, e os protocolos TCP e UDP em linhas gerais.
* **Limitações:**
  * Cobre apenas a primeira parte do conteúdo sobre camada de transporte (sem controle de congestionamento, handshake detalhado, etc.).
  * Slides podem conter texto fragmentado ou em tópicos curtos, reduzindo a qualidade dos chunks.
  * Imagens e diagramas não são extraídos pelo `pypdf`.

### 2. Chamadas bloqueantes em sockets.pdf
* **Origem:** Slides de aula - Disciplina de Redes de Computadores
* **Tipo:** Slides de aula (PDF exportado de apresentação)
* **Tamanho:** 92 KB
* **Conteúdo:** Explica o comportamento de chamadas bloqueantes e não bloqueantes em sockets, modelo cliente-servidor com sockets TCP e UDP, e exemplos práticos de comunicação em rede.
* **Limitações:**
  * Documento curto, gera poucos chunks, limitando a profundidade das respostas.
  * Exemplos de código em slides podem ser extraídos de forma fragmentada.
  * Sem cobertura de sockets assíncronos ou I/O não bloqueante avançado.

### 3. Comunicação entre processos (2).pdf
* **Origem:** Slides de aula - Disciplina Redes de Computadores
* **Tipo:** Slides de aula (PDF exportado de apresentação)
* **Tamanho:** 706 KB
* **Conteúdo:** Aborda os mecanismos de comunicação entre processos (IPC), incluindo pipes, filas de mensagens, memória compartilhada e sockets como forma de comunicação.
* **Limitações:**
  * Diagramas e figuras não são processados pelo extrator de texto.
  * Pode haver sobreposição temática com o documento de chamadas bloqueantes.

### 4. Slides 1 Filas de Prioridade.pdf
* **Origem:** Slides de aula - Disciplina de Estruturas de Dados
* **Tipo:** Slides de aula (PDF exportado de apresentação)
* **Tamanho:** 1,1 MB
* **Conteúdo:** Introdução às filas de prioridade, definição, operações básicas (inserção, remoção do mínimo/máximo), e implementação via heap binário.
* **Limitações:**
  * Conteúdo em formato de tópicos, chunks podem capturar frases incompletas.
  * Pseudocódigos e algoritmos podem ser extraídos de forma fragmentada.
  * Sem exemplos de aplicações reais de filas de prioridade.

### 5. Slides 2 Tabelas Hash.pdf
* **Origem:** Slides de aula - Disciplina de Estruturas de Dados
* **Tipo:** Slides de aula (PDF exportado de apresentação)
* **Tamanho:** 1,0 MB
* **Conteúdo:** Conceito de tabelas hash, funções de hash, tratamento de colisões (encadeamento e endereçamento aberto), e análise de complexidade das operações.
* **Limitações:**
  * Exemplos numéricos e tabelas visuais não são extraídos fielmente como texto.
  * Fórmulas matemáticas podem ser mal interpretadas na extração.
  * Não cobre implementações específicas em linguagens de programação.

### 6. Slides 3 Árvores.pdf
* **Origem:** Slides de aula - Disciplina de Estruturas de Dados
* **Tipo:** Slides de aula (PDF exportado de apresentação)
* **Tamanho:** 2,1 MB
* **Conteúdo:** Conceitos fundamentais de árvores: terminologia (raiz, folha, altura, grau), árvores genéricas, representação e percursos (pré-ordem, in-ordem, pós-ordem).
* **Limitações:**
  * Arquivo grande com muitas imagens, grande parte do conteúdo visual não é extraída.
  * Diagramas de árvores são a principal forma de explicação nos slides e não são processados.
  * Chunks podem conter apenas os textos dos títulos e tópicos, sem os exemplos visuais.

### 7. Slides 4 Árvores Binárias de Busca.pdf
* **Origem:** Slides de aula - Disciplina de Estruturas de Dados
* **Tipo:** Slides de aula (PDF exportado de apresentação)
* **Tamanho:** 418 KB
* **Conteúdo:** Definição e propriedades das árvores binárias de busca (BST), operações de busca, inserção e remoção, e análise de complexidade no melhor e pior caso.
* **Limitações:**
  * Exemplos de remoção envolvem diagramas visuais que não são extraídos.
  * Conteúdo de análise de complexidade pode ser insuficiente para perguntas aprofundadas.

### 8. Slides 5 Árvores AVL.pdf
* **Origem:** Slides de aula - Disciplina de Estruturas de Dados
* **Tipo:** Slides de aula (PDF exportado de apresentação)
* **Tamanho:** 571 KB
* **Conteúdo:** Introdução às árvores AVL, conceito de balanceamento, fator de balanceamento, e rotações simples (direita e esquerda) para rebalanceamento.
* **Limitações:**
  * Rotações são explicadas principalmente por diagramas não extraídos pelo `pypdf`.
  * Cobre apenas rotações simples (rotações duplas estão no documento seguinte).
  * Pseudocódigos dos algoritmos de rotação podem aparecer fragmentados.

### 9. Slides 6 Árvores AVL Parte 2.pdf
* **Origem:** Slides de aula - Disciplina de Estruturas de Dados
* **Tipo:** Slides de aula (PDF exportado de apresentação)
* **Tamanho:** 579 KB
* **Conteúdo:** Continuação do conteúdo de AVL: rotações duplas (esquerda-direita e direita-esquerda), algoritmo completo de inserção com rebalanceamento, e exemplos passo a passo.
* **Limitações:**
  * Continuação direta do documento anterior, pode haver perda de contexto se consultados separadamente pelo RAG.
  * Exemplos passo a passo dependem fortemente de diagramas visuais.

### 10. Slides 8 Busca Digital.pdf
* **Origem:** Slides de aula - Disciplina de Estruturas de Dados
* **Tipo:** Slides de aula (PDF exportado de apresentação)
* **Tamanho:** 365 KB
* **Conteúdo:** Estruturas de busca digital, incluindo tries (árvores de prefixo), Patricia trees, e aplicações em busca de strings e dicionários digitais.
* **Limitações:**
  * Conteúdo mais avançado: respostas do RAG podem ser insuficientes para perguntas muito específicas.
  * Exemplos de aplicação dependem de contexto visual não extraído.
  * Slide 7 não está presente na base: pode haver lacuna no conteúdo sequencial da disciplina.

---

## Resumo Estatístico do Dataset

| ID | Documento | Disciplina | Chunks Estimados |
| :---: | :--- | :--- | :---: |
| 1 | Camada de Transporte - Primeira parte | Redes de Computadores | 60 |
| 2 | Chamadas bloqueantes em sockets | Redes de Computadores | 8 |
| 3 | Comunicação entre processos | Sistemas Operacionais / Redes | 25 |
| 4 | Slides 1 Filas de Prioridade | Estruturas de Dados | 40 |
| 5 | Slides 2 Tabelas Hash | Estruturas de Dados | 38 |
| 6 | Slides 3 Árvores | Estruturas de Dados | 75 |
| 7 | Slides 4 Árvores Binárias de Busca | Estruturas de Dados | 15 |
| 8 | Slides 5 Árvores AVL | Estruturas de Dados | 20 |
| 9 | Slides 6 Árvores AVL Parte 2 | Estruturas de Dados | 21 |
| 10 | Slides 8 Busca Digital | Estruturas de Dados | 13 |

> **Nota:** Os chunks estimados foram calculados de forma aproximada com base no tamanho do arquivo, considerando `chunk_size = 500` e `overlap = 100`. O número real indexado depende exclusivamente da densidade de texto limpo que a biblioteca `pypdf` consegue extrair.
