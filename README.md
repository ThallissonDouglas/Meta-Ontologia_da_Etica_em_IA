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

**RNF1.** A ontologia deve ser Localizável (_Findable_), atribuindo-lhe um identificador único, global e persistente (e.g., um DOI) e indexando os seus metadados em catálogos pesquisáveis.

**RNF2.** A ontologia deve ser Acessível (_Accessible_), permitindo a obtenção dos seus artefactos (arquivos OWL, documentação) por meio de um protocolo padronizado e aberto (HTTPS). Dada a licença restrita que requer confirmação para uso, o protocolo pode incluir uma etapa de autenticação ou solicitação de acesso.

**RNF3.** A ontologia deve ser Interoperável (_Interoperable_), empregando linguagens formais amplamente adotadas (OntoUML, OWL) e vinculando-se a vocabulários ou ontologias de referência que também sigam os princípios FAIR.

**RNF4.** A ontologia deve ser Reutilizável (_Reusable_), disponibilizando metadados ricos sobre proveniência, domínio e escopo, e especificando de forma inequívoca a sua licença de uso. A licença é restrita, exigindo confirmação explícita por parte do utilizador antes de qualquer aproveitamento, derivação ou redistribuição.

### Requisitos Funcionais: Grupos de Questões de Competência

* **GQC1. Fundamentos da Agência Moral**

**QC1.** O que faz um dado agente ser classificado como um agente moral?

**QC2.** Quais normas um agente precisa para classificar uma ação como uma ação moral?

**QC3.** É a omissão um tipo de ação moral?

* **GQC2. Ecossistema de IA e Responsabilidade**

**QC4.** O que é um ecossistema de IA?

**QC5.** O que é a responsabilidade moral em um ecossistema de IA?

**QC6.** Como responsabilidades são atribuídas em um ecossistema de IA?

**QC7.** Quem atribui responsabilidades em um ecossistema de IA?

* **GQC3. Normas, Valores e Deôntica**

**QC8.** O que é uma norma ética no contexto da ontologia?

**QC9.** Quais são os componentes lógicos necessários para definir uma norma ética?

**QC10.** Qual norma ética se aplica a uma determinada ação em um contexto específico?

**QC11.** Quais são os valores éticos?

**QC12.** Quem define os valores éticos?

**QC13.** Como um valor se relaciona com uma norma ética?

**QC14.** Uma determinada ação é obrigatória, permitida ou proibida para um determinado agente?
