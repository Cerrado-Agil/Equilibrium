# Documento de Visão do Projeto
## Histórico de Revisão
| Data   | Versão | Modificação  | Autor  |
| :-- | :-- | :-- | :-- |
| 11/02/2021 | 0.1 | Criação da estrutura do documento |  Flavio Vieira |
| 18/02/2021 | 0.2 | Primeira versão documento de visão |  Flavio Vieira, Joao Paulo e Paulo Henrique|
| 06/03/2021 | 0.3 | Revisão do documento pós feedbacks | Paulo Henrique, João Paulo, Flávio Vieira|  
 10/03/2021 | 0.4 | Revisão gerenciamento de riscos | Paulo Henrique, Flávio Vieira|
    

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
        6.3.	Matriz de Comunicação  
        6.4.	Escalabilidade do Projeto  
        6.5.	Gerenciamento de Riscos  
    7. LIÇÕES APRENDIDAS
    8. REFERÊNCIAS

## Visão do Projeto
### 1. Introdução  
#### 1.1. Declaração do Problema
| Questionamento | Resposta |
| :--: | :--: |
| O problema  | A falta de conhecimento em relação à educação financeira |
| Afeta | Idosos, adultos e adolescentes os quais possuam algum tipo de renda  |
| Cujo impacto é | Desequilibrio nos gastos que pode gerar endividamento |
| Uma solução de sucesso seria | Apresentar informações sobre os seus gastos; Dicas de gerência; |  

&nbsp;
#### 1.2. Objetivos do Projeto
Prover uma plataforma virtual que visa auxiliar na gestão e visão dos gastos de pessoas, famílias e/ou grupos para tomadas decisão a fim de controlar a saúde financeira dos mesmos.

&nbsp;
### 2. Stakeholders
| Nome | Descrição | Responsabilidade |
| :--: | :--: | :--: |  
| Usuário comum (indivudual) | Usuário que deseja controlar seus gastos pessoais |  Monitorar e fazer o lançamento dos gastos na plataforma|
| Equipe de desenvolvimento | Planejamento, desenvolvimento e manutenção da plataforma de acordo com as premissas e regras de negócio dos investidores |Executar o projeto dentro do prazo estipulado com base no escopo de engenharia de requisitos previamente definido|
| Investidores | Zelam pela execução do projeto para que este tenha o resultado esperado e obtenham retorno sobre o investimento | Manter o padrão de qualidade e financiar o desenvolvimento do projeto | 

&nbsp;
### 3. Visão Geral do Produto  
#### 3.1. Declaração de Posição do Produto
| Para | Quem | O **Equilibrium** | Que | Ao Contrário | Nosso Produto|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Idosos, adultos e adolescente os quais possuam alguma renda | Tem dificuldade com o controle de seus gastos e investimentos | Plataforma *web* de controle financeiro | Gera indicadores e dicas que possam auxiliar nas tomadas de decisões financeiras | Tradicional pĺanilha de gastos | Faz a gestão e exibição interativa de sua renda e gastos, seja em escopo individual ou em grupo |

&nbsp;
#### 3.2. Mínimo Produto Viável (MVP)
Uma solução de sucesso para o problema analisado seria a criação de um **dashboard** interativo capaz de **exibir métricas** e **dicas de gestão** para seus usuários em forma de **relatórios**.  

&nbsp;
### 4. Visão Geral do Projeto  
#### 4.1. Organização do Projeto
| Papel | Atribuições | Responsável | Participantes |
|:----:|:----:|:----:|:----:|
|*Product Owner*| Responsável pelos interesses dos investidores; Define e pondera quais funcionalidades possuem prioridade de execução; | Paulo | João, Flávio |
| *Scrum Master* | Reposável por monitorar as práticas scrum; Motivar a equipe; Entrega contínua de valor ao produto; | João | Flávio, Paulo|
| Desenvolvedor | Executar o projeto com base no escopo predefinido pela Engenharia de Requisitos| Paulo, Flávio, João | Paulo, Flávio, João |
| Mentor | Avaliar a qualidade do proejto criado | George Marsicano | Paulo, Flávio, João |

&nbsp;
### 5. Ferramentas, Ambiente e Infra-Estrutura
#### 5.1. Hardware  
| Perfil | Tipo de Hardware | Configurações | Qtd. PLanejada | Prazo Estimado | Observação |
|:----:|:----:|:----:|:----:|:----:|:----:|
| Desenvolvedor | Computador | Intel I3; 4gb RAM; | 03 | 18/02/21 | - |

&nbsp;
#### 5.2. Software  
| Perfil | Tipo de Software | Nome da Ferramenta | Versão | Qtd. Licensas | Prazo Estimado | Observação |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| Desenvolvedor | Gerenciador de versionamento e repositórios | GitHub | - | Free | Satisfeito | - |
| Desenvolvedor | Editor de texto | VSCode | - | Free | Satisfeito | - |
| Desenvolvedor | Deploy | Azure | - | Free | 05/04/2021 | - |
| *Product Owner*, *Scrum Master* e Desenvolvedores | Comunicação | Microsoft Teams | - | 03 licenças de estudantes UnB | Satisfeito | - | 

&nbsp;
### 6. Processo de Gerência de Projeto  
O **Equilibrium** utilizará como premissa organizacional de projeto de desenvolvimento de software o modelo ágil *Lean Kanbam*. Estrutura que permite uma entrega rápida, contínua e flexível de valor ao produto. Por se espelhar em uma cultura *Kanbam*, um quadro de Backlog será alimentado e cada história terá sua prioridade diante das demais.

&nbsp;
#### 6.1. Planejamento das Fases e Iterações do Projeto  
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

&nbsp;
#### 6.2. Processo de Desenvolvimento e Mensuração   
O *Lean Kanbam* é um método para a implantação de mudanças que não prescreve papéis ou práticas específicas. Em vez disso, oferece uma série de princípios que buscam melhorar o desempenho e reduzir desperdício, eliminando atividades que não agregam valor para a equipe/projeto. Para controlar estas atividades, regularmente, **histórias de usuários** serão escritas e **pontuadas** de forma que haja uma **priorização** na execução visando, sempre, o êxito do **MVP** no menor prazo possível.

&nbsp;
#### 6.3. Matriz de Comunicação  
| Descrição | Área/Envolvidos | Periodicidade | Produtos Gerados |
| :----: | :----: | :----: | :----: |
| Sprint | Todos da equipe | Semanal | Atividades propostas para a semana |
| Planejamento | Todos da equipe | Definido na seção 6.1 | Planejamento de Backlog para a próxima Sprint |
| Revisão | Todos da equipe | Definido na seção 6.1 | Revisão das entregas propostas pelo plajamento de Sprint |
| Grooming | Todos da equipe | Definido na seção 6.1 | *Brainstorm* de requisitos do produto |
| Homologação | Todos da equipe | Definido na seção 6.1 | Conferência das entregas frente ao proposto no MVP |

&nbsp;
#### 6.4. Escalabilidade do Projeto  
Como proposta de escalabilidade do projeto **Equilibrium** definiu-se como hierarquia de decisões:

| Função | Prioridade nas Decisões |
| :---: | :---: |
| *Product Owner* | Regras de negócio |
| *Scrum Master* | Relativas à execução, planejamento e revisão das Sprints |
| Mentor | Consultor com prioridade máxima em todas as áreas |

&nbsp;
#### 6.5. Gerenciamento de Riscos  
O gerenciamento de risco tem como objetivo descrever e acompanhar quais são os riscos do projeto, com uso de indicadores de gestão de risco para avaliar a probabilidade e os impactos dessas ameaças ao projeto.


| Risco | Descrição |  Mitigação | Indicador de Monitoramento | *Threshold*
| :---- | :-- | :-- | :--: | :--: |
| R1 | Limitação técnica de membros da equipe| Mobilização da equipe para realizar treinamentos e KTs (*Knowledge Transfer* - Transferência de conhecimento)| Heatmap de conhecimentos | Estagnação em baixo nível | 
| R2 | Falta de comprometimento da equipe com o projeto| Envolver e motivar os membros da equipe relembrando a missão do projeto| Burndown| Finalizar sprint sem entregar o que foi proposto |
| R3 | Planejamento ineficiente |  Analisar os pontos falhos do planejamento prévio e corrigir os posteriores | Entregas sem geração de valor para o negócio | Realease 1.0 distante de MVP|
| R4 | Dependência de um ou mais membros do time para o andamento do projeto| Fazer pareamento dos membros mais experientes com os menos experientes| WIP (*Work in Progress*) | História altamente dependente de WIP |
| R5 | Falha na comunicação entre os membros da equipe| Deixar claro todos os canais de comunicação e dar maior abertura para todos os membros | Quadro Kanbam | Mais de um desenvolvedor trabalhando na mesma história |
| R6 | Membros atarefados em outras disciplinas| Criação de um cronograma em conjunto que possa ponderar a capacidade de entrega individual e manter a entrega contínua para o projeto | Agenda | Excessivos conflitos de entregas|
| R8 | Desistência de membros | Realocação das tarefas | Aviso prévio | - |

&nbsp;
### 7. Lições Aprendidas
Desde o princípio do projeto situações adversas se mostraram presentes e, diante disso, uma série de pontos foram levantados e consequentemente resolvidos. Algumas premissas básicas para que a execução se tornasse uma realidade foram tomando forma e mostrando que, para este projeto, fazer o que se foi proposto e depois refinar é mais eficiente que fazer com perfeita execução desde o começo. Viu-se na prática que entrega contínua gera valor e que todos são capazes de as fazer. Por último mas não menos importante: se o problema é de ninguém, ele é seu! 

&nbsp;
### 8. Referências 
1. [Texto descritivo sobre a estrutura e objetivo dos tópicos do documento de visão](https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html.) - Acessado em 11/02/2021

2. [Scrum  é  uma  metodologia  ágil  para  gestão  e  planejamento  de  projetos  de software]( https://www.desenvolvimentoagil.com.br/scrum/) - Acessado 11/02/2021

3. [Lean Kanbam](https://setecnet.com.br/home/diferenca-do-kanban-lean-para-o-kanban-agile/) - Acessado 10/03/2021
