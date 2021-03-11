# Documento de Visão do Projeto
## Histórico de Revisão
| Data   | Versão | Modificação  | Autor  |
| :-- | :-- | :-- | :-- |
| 11/02/2021 | 0.1 | Criação da estrutura do documento |  Flavio Vieira |
| 18/02/2021 | 0.2 | Primeira versão documento de visão |  Flavio Vieira, Joao Paulo e Paulo Henrique|
| 06/03/2021 | 0.3 | Revisão do documento pós feedbacks | Paulo Henrique, João Paulo, Flávio Vieira|  
 06/03/2021 | 0.4 | Revisão gerenciamento de riscos | Paulo Henrique, João Paulo, Flávio Vieira|
    

## Sumário
    1. INTRODUÇÃO    
        1.1.	Problema 
        1.2.	Declaração do Problema  
        1.3.	Objetivos do Projeto
    2. STAKEHOLDERS  
    3. VISÃO GERAL DO PRODUTO  
        3.1.	Declaração de Posição do Produto  
        3.2.	Mínimo Produto Viável (MVP)
    4. VISÃO GERAL DO PROJETO  
        4.1.	Organização do Projeto  
    5. FERRAMENTAS, AMBIENTE E INFRA-ESTRUTURA  
        5.1.	Hardware  
        5.2.	Software
    6. PROCESSO DE GERÊNCIA DE PROJETO  
        6.1.	Planejamento das Fases e Iterações do Projeto  
        6.2.	Processo de Desenvolvimento e Mensuração  
        6.3.	Milestones e Objetivos do Projeto  
        6.4.	Matriz de Comunicação  
        6.5.	Escalabilidade do Projeto  
        6.6.	Gerenciamento de Riscos  
        6.7.	Critérios de Replanejamento  
    7. LIÇÕES APRENDIDAS
    8. REFERÊNCIAS

## Visão do Projeto
### 1. Introdução  
#### 1.1. Declaração do Problema
| Questionamento | Resposta |
| :--: | :--: |
| O problema  | Pessoas que possuem alguma renda e não conseguem e/ou querem *insights* sobre seus gastos |
| Afeta | Idosos, adultos e adolescentes  |
| Cujo impacto é | Desequilibrio nos gastos que pode gerar endividamento |
| Uma solução de sucesso seria | Geração de relatórios de gastos e investimentos, exibição de métricas via dashboard interativo |  

#### 1.2. Objetivos do Projeto
Plataforma virtual que visa auxiliar na gestão e visão dos gastos de pessoas, famílias e/ou grupos para tomadas decisão a fim de controlar a saúde financeira dos mesmos. A plataforma fornecerá visões, a partir de métricas, sobre organização financeira dos usuários.

### 2. Stakeholders
| Nome | Descrição | Responsabilidade |
| :--: | :--: | :--: |  
| Usuário comum (indivudual) | Usuário que deseja controlar seus gastos pessoais |  Monitorar e fazer o lançamento dos gastos na plataforma|
| Equipe de desenvolvimento | Planejamento, desenvolvimento e manutenção da plataforma de acordo com as premissas e regras de negócio dos investidores |Executar o projeto dentro do prazo estipulado com base no escopo de engenharia de requisitos previamente definido|
| Investidores | Zelam pela execução do projeto para que este tenha o resultado esperado e obtenham retorno sobre o investimento | Manter o padrão de qualidade e financiar o desenvolvimento do projeto | 

### 3. Visão Geral do Produto  
#### 3.1. Declaração de Posição do Produto
| Para | Quem | O **Equilibrium** | Que | Ao contrário | Nosso produto|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Qualquer pessoa que possua renda | Tem dificuldade com o controle de seus gastos e investimentos | Plataforma *web* de controle financeiro | Captar, tratar e gerar indicadores financeiros que possam auxiliar nas tomadas de decisões financeiras | Tradicional pĺanilha de gastos | Faz a gestão e exibição interativa de sua renda e gastos, seja em escopo individual ou em grupo |

#### 3.2. Mínimo Produto Viável (MVP)
* Registro do(s) usuário(s) na plataforma;
* Cadastro e armazenamento do histórico de movimentações financeiras;
* Tratamento e exibição interativa dos dados;

### 4. Visão Geral do Projeto  
#### 4.1. Organização do Projeto
| Papel | Atribuições | Responsável | Participantes |
|:----:|:----:|:----:|:----:|
|*Product Owner*| Responsável pelos interesses dos investidores; Define e pondera quais funcionalidades possuem prioridade de execução; | Paulo | João, Flávio |
| *Scrum Master* | Reposável por monitorar as práticas scrum; Motivar a equipe; Entrega contínua de valor ao produto; | João | Flávio, Paulo|
| Desenvolvedor | Executar o projeto com base no escopo predefinido pela Engenharia de Requisitos| Paulo, Flávio, João | Paulo, Flávio, João |
| Mentor | Avaliar a qualidade do proejto criado | George Marsicano | Paulo, Flávio, João |

### 5. Ferramentas, Ambiente e Infra-Estrutura
#### 5.1. Hardware  
| Perfil | Tipo de Hardware | Configurações | Qtd. PLanejada | Prazo Estimado | Observação |
|:----:|:----:|:----:|:----:|:----:|:----:|
| Desenvolvedor | Computador | Intel I3; 4gb RAM; | 03 | 18/02/21 | - |

#### 5.2. Software  
| Perfil | Tipo de Software | Nome da Ferramenta | Versão | Qtd. Licensas | Prazo Estimado | Observação |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| Desenvolvedor | Gerenciador de versionamento e repositórios | GitHub | - | Free | Satisfeito | - |
| Desenvolvedor | Editor de texto | VSCode | - | Free | Satisfeito | - |
| Desenvolvedor | Deploy | Azure | - | Free | 05/04/2021 | - |
| *Product Owner*, *Scrum Master* e Desenvolvedores | Comunicação | Microsoft Teams | - | 03 licenças de estudantes UnB | Satisfeito | - | 

### 6. Processo de Gerência de Projeto  
O **Equilibrium** utilizará como premissa organizacional de projeto de desenvolvimento de software o modelo ágil *Lean Kanbam*. Estrutura que permite uma entrega rápida, contínua e flexível de valor ao produto. Por se espelhar em uma cultura *Kanbam*, um quadro de Backlog será alimentado e cada história terá sua prioridade diante das demais.

#### 6.1 Planejamento das Fases e Iterações do Projeto  
| Sprint | Início | Fim | Proposta |
| :---: | :---: | :---: | :---: |
| 01 | 05/02/2021 | 11/02/2021 | Definição do Projeto |
| 02 | 12/02/2021 | 18/02/2021 | Criação do Documento de Visão |
| 03 | 19/02/2021 | 25/02/2021 | Tranferência de conhecimentos técnicos | 
| 04 | 26/03/2021 | 04/03/2021 | Documentação do projeto e revisões |
| 05 | 05/03/2021 | 11/03/2021 | Definição de Backlog do Produto; Organização estrutural dos requisitos; Definição do Backlog da Sprint 06|
| 06 | 12/03/2021 | 18/03/2021 | Implementação Backlog Sprint 06; Revisão de Sprint; Definição do Backlog da Sprint 07; |
| 07 | 19/03/2021 | 25/03/2021 | Implementação Backlog Sprint 07; Revisão de Sprint; Definição do Backlog da Sprint 08;|
| 08 | 26/03/2021 | 01/04/2021 | Implementação Backlog Sprint 08; Revisão de Sprint; |
| 09 | 02/04/2021 | 08/04/2021 | Revisão de código; Homologação; Entrega de Release 1.0; |
| 10 | 09/04/2021 | 15/04/2021 | Grooming de Backlog; Priorização de histórias; Definição do Backlog da Sprint 11 |
| 11 | 16/04/2021 | 22/04/2021 | Implementação Backlog Sprint 11; Revisão de Sprint; Entrega de Release 1.1; Definição do Backlog da Sprint 12; |
| 12 | 23/04/2021 | 29/04/2021 | Implementação Backlog Sprint 12; Revisão de Sprint; Entrega de Release 1.2; Definição do Backlog da Sprint 13; |
| 13 | 30/04/2021 | 06/05/2021 | Revisão de código; Revisão dos documentos; Homologação; Entrega de Release 2.0; |
| 14 | 07/05/2021 | 13/05/2021 | Testes de usabilidade; Revisões gerais do projeto; |

#### 6.2 Processo de Desenvolvimento e Mensuração   
* Grooming de ideias
* Sprint Backlog
* Sprint Planning
* Sprint Review
* Daily Meetings
* Homologação
* Testes de usabilidade
    
#### 6.3 Matriz de Comunicação  

| Descrição | Área/Envolvidos | Periodicidade | Produtos Gerados |
| :----: | :----: | :----: | :----: |
| Sprint | Todos da equipe | Semanal | Atividades propostas para a semana |
| Planejamento | Todos da equipe | Definido na seção 6.1 | Planejamento de Backlog para a próxima Sprint |
| Revisão | Todos da equipe | Definido na seção 6.1 | Revisão das entregas propostas pelo plajamento de Sprint |
| Grooming | Todos da equipe | Definido na seção 6.1 | *Brainstorm* de requisitos do produto |
| Homologação | Todos da equipe | Definido na seção 6.1 | Conferência das entregas frente ao proposto no MVP |

#### 6.4 Escalabilidade do Projeto  
Como proposta de escalabilidade do projeto **Equilibrium** definiu-se como hierarquia de decisões:

| Função | Prioridade nas decisões |
| :---: | :---: |
| *Product Owner* | Regras de negócio |
| *Scrum Master* | Relativas à execução, planejamento e revisão das Sprints |
| Mentor | Consultor com prioridade máxima em todas as áreas |

#### 6.5 Gerenciamento de Riscos  

O gerenciamento de risco tem como objetivo descrever e acompanhar quais são os riscos do projeto, com uso de indicadores de gestão de risco para avaliar a probabilidade e os impactos dessas ameaças ao projeto.


| Risco | Descrição |  Mitigação | Probabilidade | Impacto |
| :---- | :-- | :-- | :---- | :---- |  
| R1 | Limitação técnica de membros da equipe| Ajuda dos membros da equipe e Sprint de treinamentos e tranferência de conhecimentos técnicos| alta | baixo |  
| R2 | Falta de comprometimento da equipe com o projeto| Envolver e motivar os membros da equipe relembrando a missão do projeto| baixa | muito alto |  
| R3 | Planejamento ineficiente|  Melhorar o Planejamento prévio |  moderada | alto |
| R4 | Dependência de um ou mais membros do time para o andanmento do projeto| Fazer parementos dos membros mais experientes com os menos experientes| alta | baixo |
| R5 |Falha comunicação entre os membros da equipe| Deixar claro todos os canais de comunicação e dar mairo abertura para todos os membros| alta | moderada |
| R6 | Membros atarefados em outras disciplinas| informar com atecedencia para redistribuião da tarefa|  alta | baixo |
| R7 | Erros de Priorização | Reavaliar a cada sprint a priorização e o MVP |  moderada | alto |
| R7 | Desistência de membros | Realocação das tarefas |  baixo | muito alto |
| R7 | Desistência de membros | Realocação das tarefas |  alta | baixo |

&nbsp;
### **Analise qualitativa**  


| Probabilidade / Impacto | Peso|
| :---- | :---- |
| Muito alta | 0,9 |
| Alta | 0,7 |
| Moderada | 0,5 |
| Baixa| 0,3 |
| Muito baixa| 0,1 |

&nbsp;
### **Matriz de probabilidades X Impacto**
| Probabilidade / Impacto | Muito baixa | Baixa | Moderada | Alta | Muito alta |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Muito alta | Risco elevado | Risco elevado | Risco elevado | Risco extremo | Risco extremo |
| Alta | Risco moderado | Risco elevado | Risco elevado | Risco extremo | Risco extremo |
| Moderada | Risco baixo | Risco moderado | Risco elevado | Risco extremo | Risco extremo |
| Baixa| Risco baixo | Risco baixo | Risco moderado | Risco elevado| Risco extremo |
| Muito baixa| Risco baixo | Risco baixo | Risco moderado | Risco elevado | Risco elevado |  

&nbsp;  
O monitoramento dos riscos será feito utilizando o Burndown de riscos de e matriz de probabilidades e impactos dos riscos no projeto, que estará presente na documentação dos resultados de cada sprint.

#### 6.6 Critérios de Replanejamento  

* Desistência de membros da equipe;
* Mudança no escopo do projeto;
* Mudança de arquitetura do projeto;
* Erro de priorização;
* Queda de produtividade;
* Problemas relacionados com saúde de algum membro;
* Nao aceitação, pelo professor, de ponto de controle;
* Solução não atender as expectativas do usuário.;


    
### 7. Lições Aprendidas
* Feito é melhor que perfeito
* Entrega contínua gera valor
* Todos são capazes
* Se o problema é de ninguem, ele é seu!  

### 8. Referências 
1. [Texto descritivo sobre a estrutura e objetivo dos tópicos do documento de visão](https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html.) - Acessado em 11/02/2021

2. [Scrum  é  uma  metodologia  ágil  para  gestão  e  planejamento  de  projetos  de software]( https://www.desenvolvimentoagil.com.br/scrum/) - Acessado 11/02/2021
