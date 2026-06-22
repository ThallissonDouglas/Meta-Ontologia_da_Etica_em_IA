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
    ClassAcao = obter_classe("Acao")
    ClassAcaoMoral = obter_classe("AcaoMoral")
    ClassOmissao = obter_classe("Omissao")
    ClassResponsabilizacao = obter_classe("Responsabilizacao")
    ClassOrganizacaoReguladora = obter_classe("OrganizacaoReguladora")
    ClassEspecialista = obter_classe("Especialista")
    ClassObrigacao = obter_classe("Obrigacao")
    ClassPermissao = obter_classe("Permissao")
    ClassProibicao = obter_classe("Proibicao")
    ClassAplicacaoNormativa = obter_classe("AplicacaoNormativa")
    ClassQuebraNormativa = obter_classe("QuebraNormativa")
    ClassAgenteArtificial = obter_classe("AgenteArtificial")
    ClassAgenteHumano = obter_classe("AgenteHumano")
    ClassAgenteOrganizacional = obter_classe("AgenteOrganizacional")
    ClassAgenteMoral = obter_classe("AgenteMoral")
    ClassEcossistema = obter_classe("EcossistemaDeIA")
    ClassNorma = obter_classe("Norma")
    ClassValor = obter_classe("Valor")
    ClassJustica = obter_classe("Justica")
    ClassRestricao = obter_classe("RestricaoDeontica")
    PropResponsabiliza = getattr(onto, "responsabiliza", None)

    agente_artificial = None
    agente_humano = None
    agente_organizacional = None

    if ClassAgenteArtificial:
        agente_artificial = ClassAgenteArtificial("SRI_Robo_Medico")

    if ClassAgenteHumano:
        agente_humano = ClassAgenteHumano("Dr_Ana_Silva_Auditora")

    if ClassEcossistema:
        ClassEcossistema("Ambiente_Algoritmico_Financeiro")

    if ClassNorma:
        ClassNorma("Diretriz_de_Transparencia_Algoritmica")

    if ClassJustica:
        ClassJustica("Principio_da_Equidade_Social")
    elif ClassValor:
        ClassValor("Principio_da_Equidade_Social")

    if ClassRestricao:
        ClassRestricao("Proibicao_de_Decisao_Autonoma_Letal")

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
    "QC1 (Agentes Morais)": f"""
        SELECT ?agente ?tipo WHERE {{
            ?agente rdf:type ?tipo .
            FILTER (?tipo IN (
            <{iri_segura(ClassAgenteArtificial)}>, 
            <{iri_segura(ClassAgenteHumano)}>, 
            <{iri_segura(ClassAgenteOrganizacional)}>))
        }}
    """,
    "QC2 e QC3 (Ações Morais e Omissões)": f"""
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
            ?ecossistema rdf:type <{iri_segura(ClassEcossistema)}> .
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
            ?restricao rdf:type <{iri_segura(ClassRestricao)}> .
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
        ClassRestricao
    )

    imprimir_resultados_api(
        "Agentes Morais",
        ClassAgenteMoral
    )


print("\n" + "=" * 60)
print(" CONSULTAS SPARQL - ASSERTED MODEL")
print("=" * 60)

executar_bloco_testes("ASSERTED MODEL")

executar_consultas_owlready()

asserted_agentes_morais = len(
    listar_instancias(ClassAgenteMoral)
)

try:
    sync_reasoner_hermit()
except Exception as e:
    print(f"Erro ao executar HermiT: {e}")


print("\n" + "=" * 60)
print(" CONSULTAS SPARQL - INFERRED MODEL")
print("=" * 60)

executar_bloco_testes("INFERRED MODEL")

executar_consultas_owlready()

inferred_agentes_morais = len(
    listar_instancias(ClassAgenteMoral)
)

print(
    f"\nAgentes Morais inferidos: "
    f"{inferred_agentes_morais - asserted_agentes_morais}"
)