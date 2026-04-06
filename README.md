# Meta-ontologia da Ética em IA

## 1 Propósito

O propósito principal da ontologia é fornecer os alicerces conceituais necessários para representar formalmente princípios éticos de agência artificial de forma computável. O objetivo central é criar uma estrutura de alto nível que permita a tradução de conceitos filosóficos (como obrigação, valor e agência moral) em requisitos técnicos para sistemas de inteligência artificial, visando o alinhamento ético desses sistemas.

## 2 Escopo

A ontologia terá um escopo de meta-ontologia (ontologia de alto-nível), ou seja, não visa modelar um domínio ético específico, mas sim definir os conceitos fundamentais e suas relações que são comuns a qualquer sistema ético aplicado à IA. O grau de detalhe abrangerá a formalização de conceitos como Agente Moral, Ação Moral, Norma, Valor, Obrigação e Direito. O escopo é uma descrição formal inicial do que se define um agente artificial moral.

## 3 Linguagem de Implementação

A ontologia será implementada em uma linguagem formal que permita a representação de lógica deôntica e raciocínio sobre normas. Primeiro, ela será modelada conceitualmente em OntoUML para garantir o rigor ontológico. depois, formalizada em OWL com extensão para operadores deônticos (OBL, PER, FORB). Por fim, consultada via SPARQL sobre a base RDF resultante.

## 4 Usuários Finais Planejados

* **Engenheiros e Desenvolvedores de IA**\
Para integar restrições éticas e valores no design de sistemas autônomos.

* **Especialistas em Ética e Filosofia**\
Para formalizar teorias éticas de maneira precisa e testável.

* **Pesquisadores em IA Confiável (Trustworthy AI)**\
Para utilizar uma base conceitual comum na avaliação de alinhamento e segurança.

* **Arquitetos de Software e Ontologistas**\
Para construir aplicações ou estender a ontologia para domínios específicos.

## 5 Usos Planejados

* **Detecção e Tratamento de Conflitos Normativos**\
Permitir a identificação automática de situações em que um mesmo agente (genérico) está simultaneamente obrigado e proibido de realizar uma ação, ou obrigado a realizar ações mutuamente exclusivas. A meta-ontologia oferece operadores deônticos e regras de consistência que sinalizam conflitos lógicos, servindo como base para estratégias de resolução (e.g., priorização lexicográfica, ponderação por valores associados).

* **Inferência de Obrigações Derivadas e Cadeias Normativas**\
Possibilitar o encadeamento lógico de normas para derivar obrigações ou permissões não explicitamente declaradas. A partir de axiomas como “se A é obrigatório e A implica B, então B é obrigatório” (princípio de fechamento deôntico), a ontologia suporta a computação de consequências normativas de um conjunto de regras.

* **Verificação de Consistência de Sistemas Normativos**\
Fornecer um método formal para testar se um conjunto de normas (e.g., leis, princípios éticos, políticas organizacionais) é internamente consistente antes de sua implementação em qualquer sistema. A meta-ontologia permite a simulação de mundos possíveis normativos e a verificação de que não há contradições ou consequências indesejadas.

* **Hierarquização e Priorização de Normas**\
Oferecer uma estrutura para representar relações de precedência entre normas (e.g., normas constitucionais prevalecem sobre leis ordinárias; princípios de não-malefício têm prioridade sobre autonomia em situações de emergência). A meta-ontologia permite definir meta-normas de priorização que resolvem conflitos de forma sistemática.

* **Análise de Permissões Implícitas e Lacunas Normativas**\
Permitir a inferência do que é tacitamente permitido pelo silêncio das normas (princípio “tudo o que não é proibido é permitido”) ou, alternativamente, identificar lacunas onde nenhuma norma se aplica. A ontologia pode suportar diferentes políticas de fechamento deôntico, auxiliando na avaliação da completude de um sistema normativo.

* **Comparação e Alinhamento entre Sistemas Normativos Distintos**\
Fornecer uma base conceitual para mapear e comparar normas oriundas de diferentes fontes (e.g., leis de países distintos, códigos de ética profissionais, valores culturais). A meta-ontologia permite identificar correspondências, divergências ou relações de subsunção entre sistemas normativos, sem pressupor que o alinhamento seja realizado por um agente autônomo.

## 6 Requisitos de Ontologia

### Requisitos Não Funcionais

RNF1.
A ontologia deve garantir que não haja inconsistências formais, especialmente ao representar conjuntos de normas conflitantes (ex: uma ação ser obrigatória e proibida simultaneamente). Deve prever mecanismos para tratar conflitos deônticos.
RNF2.
Como uma meta-ontologia, deve ser facilmente extensível para domínios de aplicação específicos (ex: ética para veículos autônomos, para diagnóstico médico, etc.) sem a necessidade de modificar seus axiomas centrais.
RNF3.
Deve existir uma documentação clara que rastreie cada elemento da ontologia (classe, propriedade) até o conceito filosófico que o originou, garantindo que as decisões de formalização sejam transparentes.
RNF4.
A ontologia deve possuir um identificador único e persistente, estar registrada em repositórios reconhecidos e ser descrita com metadados ricos que incluam nome, versão, autores e contexto de criação.
RNF5.
A ontologia deve estar disponível publicamente por meio de um repositório estável e acessível, utilizando protocolos abertos e, se necessário, oferecendo mecanismos de autenticação claros sem comprometer a descoberta básica dos metadados.
RNF6.
A ontologia deve utilizar linguagens formais padronizadas e adotar boas práticas de reutilização de vocabulários consolidados para facilitar a integração com outras ontologias e sistemas.
RNF7.
A ontologia deve ser disponibilizada sob uma licença restrita que exija permissão explícita para qualquer uso comercial do seu conteúdo, conter documentação que explique suas decisões de modelagem e estar estruturada de modo modular para permitir o uso de partes específicas em diferentes contextos.
RNF8.
Fornecer uma estrutura explícita para documentar os pressupostos éticos de um sistema de IA, de modo que as decisões de modelagem, valores assumidos e princípios morais adotados sejam claramente identificáveis e rastreáveis ao longo do ciclo de vida da ontologia.

### Requisitos Funcionais: Grupos de Questões de Competência


* **GQC1. Fundamentos da Agência Moral**\

**QC1.** Quais são os critérios necessários e suficientes para que um sistema de IA seja classificado como um Agente Moral?\
**QC2.** O que constitui uma Ação Moral por parte de um sistema de IA? A omissão (não agir) é considerada uma ação moral?\
**QC3.** Como se representa a responsabilidade em um sistema distribuído onde a decisão é fruto da interação entre IA e humano?\

* **GQC2. Normas, Valores e Deôntica**\

**QC4.** Como uma Norma ética (ex: "não causar dano") pode ser codificada como uma restrição lógica?\
**QC5.** Como um Valor (ex: "privacidade") pode ser formalizado?\
**QC6.** Como representar as relações deônticas: Obrigação (OBL), Permissão (PER) e Proibição (FORB) entre um agente e uma ação?\