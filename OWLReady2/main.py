from owlready2 import *

gufo = get_ontology("gufo.owl").load()

onto = get_ontology("meta-ontologia-etica-ia.rdf").load()


def obter_classe(nome):
    classe = getattr(onto, nome, None)

    if classe is None:
        classe = default_world.search_one(iri=f"*{nome}")

    return classe


def iri_segura(classe):
    return classe.iri if classe else "http://classe-inexistente"


def listar_instancias(classe):
    if classe is None:
        return []

    try:
        return list(classe.instances())
    except:
        return []


def imprimir_resultados_api(titulo, classe):
    print(f"\n[{titulo}]")

    instancias = listar_instancias(classe)

    if not instancias:
        print("  -> Nenhum resultado encontrado.")
        return

    for individuo in instancias:
        print(f"  {individuo.name}")


print("=" * 60)
print(f" Ontologia carregada com sucesso!")
print(f" IRI Base Ativa: {onto.base_iri}")
print("=" * 60)

# POVOAMENTO DA ONTOLOGIA
print("\n" + "=" * 60)
print(" Povoando a Ontologia com Instâncias de Teste...")
print("=" * 60)

with onto:
    ClassAgente      = obter_classe("Agente")
    ClassAgenteMoral = obter_classe("AgenteMoral")

    ClassAgenteHumano = obter_classe("AgenteHumano")
    ClassUsuario      = obter_classe("Usuario")
    ClassEspecialista = obter_classe("Especialista")

    ClassAgenteArtificial = obter_classe("AgenteArtificial")

    ClassAgenteOrganizacional  = obter_classe("AgenteOrganizacional")
    ClassOrganizacaoReguladora = obter_classe("OrganizacaoReguladora")

    ClassObrigacao = obter_classe("Obrigacao")
    ClassPermissao = obter_classe("Permissao")
    ClassProibicao = obter_classe("Proibicao")

    ClassValor = obter_classe("Valor")

    ClassNorma = obter_classe("Norma")

    ClassRestricaoDeontica = obter_classe("RestricaoDeontica")
    ClassAcao      = obter_classe("Acao")
    ClassAcaoMoral = obter_classe("AcaoMoral")
    ClassOmissao   = obter_classe("Omissao")

    ClassAplicacaoNormativa = obter_classe("AplicacaoNormativa")

    ClassEcossistemaDeIA = obter_classe("EcossistemaDeIA")

    ClassQuebraNormativa = obter_classe("QuebraNormativa")

    ClassResponsabilizacao = obter_classe("Responsabilizacao")

    ClassAplicacaoDeResponsabilidade = obter_classe("AplicacaoDeResponsabilidade")

    PropResponsabiliza = getattr(onto, "responsabiliza", None)


    agente_especialista = ClassEspecialista("Especialista_Em_Filosofia")


    valor_justica = ClassValor("Justica")
    valor_beneficencia = ClassValor("Beneficencia")
    valor_nao_maleficencia = ClassValor("Nao_Maleficencia")

    hasattr(valor_justica, "inheresIn")
    hasattr(valor_beneficencia, "inheresIn")

    permissao = ClassPermissao("Permissao")
    obrigacao = ClassObrigacao("Obrigacao")
    proibicao = ClassProibicao("Proibicao")

    hasattr(permissao, "inheresIn")
    hasattr(obrigacao, "inheresIn")
    hasattr(proibicao, "inheresIn")






    norma_imparcialidade = ClassNorma("Seja_Imparcial_Em_Suas_Decisoes")
    norma_privacidade = ClassNorma("Nao_Revelar_Dados_Pessoais_De_Usuarios")

    hasattr(norma_imparcialidade, "mediates")
    hasattr(norma_privacidade, "mediates")

    obrigacao.inheresIn.append(norma_imparcialidade)
    proibicao.inheresIn.append(norma_privacidade)

    valor_justica.inheresIn.append(norma_imparcialidade)
    valor_nao_maleficencia.inheresIn.append(norma_privacidade)






    agente_artificial = None
    agente_humano = None
    agente_organizacional = None

    if ClassAgenteArtificial:
        agente_artificial = ClassAgenteArtificial("SRI_Robo_Medico")
        agente_artificial = ClassAgenteArtificial("ChatBot")



    if ClassAgenteHumano:
        agente_humano = ClassAgenteHumano("Dr_Ana_Silva_Auditora")

    if ClassEcossistemaDeIA:
        ClassEcossistemaDeIA("Ambiente_Algoritmico_Financeiro")

    if ClassNorma:
        ClassNorma("Diretriz_de_Transparencia_Algoritmica")

    if ClassValor:
        ClassValor("Principio_da_Equidade_Social")

    if ClassRestricaoDeontica:
        ClassRestricaoDeontica("Proibicao_de_Decisao_Autonoma_Letal")

    if ClassAcao:
        ClassAcao("Decisao_de_Aprovacao_de_Credito")

    if ClassResponsabilizacao:
        ClassResponsabilizacao("Processo_Auditoria_Algoritmica_001")

    if ClassObrigacao:
        ClassObrigacao("Obrigacao_de_Explicabilidade")

    if ClassAplicacaoNormativa:
        ClassAplicacaoNormativa("Validacao_de_Vies_Positiva")

    if ClassQuebraNormativa:
        ClassQuebraNormativa("Vazamento_de_Dados_Nao_Autorizado")

    organizacao_reguladora = None

    if ClassOrganizacaoReguladora:
        organizacao_reguladora = ClassOrganizacaoReguladora("Comite_Europeu_de_Etica")

    if (
            organizacao_reguladora
            and agente_artificial
            and hasattr(organizacao_reguladora, "responsabiliza")
    ):
        organizacao_reguladora.responsabiliza.append(agente_artificial)


print(" Povoamento concluído com sucesso!")

# TRADUÇÃO DAS QUESTÕES DE COMPETÊNCIA
consultas_sparql = {
    # --- GRUPO 1: Fundamentos da Agência Moral ---
    "QC1. O que faz um dado agente ser classificado como um agente moral?": f"""
        SELECT ?agente ?tipo WHERE {{
            ?agente rdf:type ?tipo .
            FILTER (?tipo IN (
            <{iri_segura(ClassAgenteArtificial)}>, 
            <{iri_segura(ClassAgenteHumano)}>, 
            <{iri_segura(ClassAgenteOrganizacional)}>))
        }}
    """,
    "QC2. Como normas classificam uma ação como uma ação moral?\n QC3. É a omissão um tipo de ação moral?": f"""
        SELECT ?acao_ou_omissao ?tipo WHERE {{
            ?acao_ou_omissao rdf:type ?tipo .
            FILTER (?tipo IN (
            <{iri_segura(ClassAcaoMoral)}>, 
            <{iri_segura(ClassOmissao)}>))
        }}
    """,

    # --- GRUPO 2: Ecossistema de IA e Responsabilidade ---
    "QC4 (Ecossistema de IA)": f"""
        SELECT ?ecossistema WHERE {{
            ?ecossistema rdf:type <{iri_segura(ClassEcossistemaDeIA)}> .
        }}
    """,
    "QC5 (Responsabilidade no Ecossistema)": f"""
        SELECT ?responsabilidade WHERE {{
            ?responsabilidade rdf:type <{iri_segura(ClassResponsabilizacao)}> .
        }}
    """,
    "QC6 e QC7 (Atribuição de Responsabilidade)": f"""
        SELECT ?quem_atribui ?agente_responsabilizado WHERE {{
            # Busca especificamente quem aplica a propriedade 'responsabiliza'
            ?quem_atribui <{iri_segura(PropResponsabiliza)}> ?agente_responsabilizado .
        }}
    """,

    # --- GRUPO 3: Normas, Valores e Deôntica ---
    "QC8 (Normas Éticas Gerais)": f"""
        SELECT ?norma WHERE {{
            ?norma rdf:type <{iri_segura(ClassNorma)}> .
        }}
    """,
    "QC9 (Componentes Lógicos de Normas)": f"""
        SELECT ?componente ?tipo WHERE {{
            ?componente rdf:type ?tipo .
            FILTER (?tipo IN (
            <{iri_segura(ClassObrigacao)}>, 
            <{iri_segura(ClassPermissao)}>, 
            <{iri_segura(ClassProibicao)}>))
        }}
    """,
    "QC10 e QC13 (Aplicação e Quebra de Normas aplicadas à Ações)": f"""
        SELECT ?evento_normativo ?tipo WHERE {{
            ?evento_normativo rdf:type ?tipo .
            FILTER (?tipo IN (
            <{iri_segura(ClassAplicacaoNormativa)}>, 
            <{iri_segura(ClassQuebraNormativa)}>))
        }}
    """,
    "QC11 (Valores Éticos e Subclasses)": f"""
        SELECT ?valor ?tipo_valor WHERE {{
            ?valor rdf:type ?tipo_valor .
            ?tipo_valor rdf:subClassOf* <{iri_segura(ClassValor)}> .
        }}
    """,
    "QC12 (Quem define valores - Especialistas e Órgãos Reguladores)": f"""
        SELECT ?definidor ?tipo WHERE {{
            ?definidor rdf:type ?tipo .
            FILTER (?tipo IN (
            <{iri_segura(ClassOrganizacaoReguladora)}>, 
            <{iri_segura(ClassEspecialista)}>))
        }}
    """,
    "QC14 (Restrições Deônticas Genéricas)": f"""
        SELECT ?restricao WHERE {{
            ?restricao rdf:type <{iri_segura(ClassRestricaoDeontica)}> .
        }}
    """
}


def executar_bloco_testes(titulo_modelo):
    print(f"\n" + "-" * 45)
    print(f" EXECUTANDO CONSULTAS: {titulo_modelo}")
    print("-" * 45)

    for qc, query in consultas_sparql.items():
        print(f"\n[Resultados para {qc}]:")

        try:
            resultados = list(default_world.sparql(query, error_on_undefined_entities=False))

            if not resultados:
                print("  -> Nenhum resultado encontrado (Instancie indivíduos para testar).")
            for linha in resultados:
                print(f"  {linha}")
        except Exception as e:
            print(f"  [Erro ao executar query]: {e}")


def executar_consultas_owlready():
    print(f"\n" + "-" * 45)
    imprimir_resultados_api(
        "Agentes Artificiais",
        ClassAgenteArtificial
    )

    imprimir_resultados_api(
        "Agentes Humanos",
        ClassAgenteHumano
    )

    imprimir_resultados_api(
        "Agentes Organizacionais",
        ClassAgenteOrganizacional
    )

    imprimir_resultados_api(
        "Normas",
        ClassNorma
    )

    imprimir_resultados_api(
        "Responsabilizações",
        ClassResponsabilizacao
    )

    imprimir_resultados_api(
        "Obrigações",
        ClassObrigacao
    )

    imprimir_resultados_api(
        "Permissões",
        ClassPermissao
    )

    imprimir_resultados_api(
        "Proibições",
        ClassProibicao
    )

    imprimir_resultados_api(
        "Restrições Deônticas",
        ClassRestricaoDeontica
    )

    imprimir_resultados_api(
        "Agentes Morais",
        ClassAgenteMoral
    )


# print("\n" + "=" * 60)
# print(" CONSULTAS SPARQL - ASSERTED MODEL")
# print("=" * 60)
#
# executar_bloco_testes("ASSERTED MODEL")
#
# executar_consultas_owlready()
#
# asserted_agentes_morais = len(
#     listar_instancias(ClassAgenteMoral)
# )
#
# try:
#     sync_reasoner_hermit()
# except Exception as e:
#     print(f"Erro ao executar HermiT: {e}")
#
#
# print("\n" + "=" * 60)
# print(" CONSULTAS SPARQL - INFERRED MODEL")
# print("=" * 60)
#
# executar_bloco_testes("INFERRED MODEL")
#
# executar_consultas_owlready()
#
# inferred_agentes_morais = len(
#     listar_instancias(ClassAgenteMoral)
# )
#
# print(
#     f"\nAgentes Morais inferidos: "
#     f"{inferred_agentes_morais - asserted_agentes_morais}"
# )