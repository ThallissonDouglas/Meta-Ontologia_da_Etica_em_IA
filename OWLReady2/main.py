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
    # ================================================================
    # Pegando as classes
    # ================================================================

    ClassAgente      = obter_classe("Agente")
    ClassAgenteMoral = obter_classe("AgenteMoral")

    ClassAgenteHumano = obter_classe("AgenteHumano")
    ClassUsuario      = obter_classe("Usuario")
    ClassEspecialista = obter_classe("Especialista")

    ClassAgenteArtificial = obter_classe("AgenteArtificial")

    ClassAgenteOrganizacional  = obter_classe("AgenteOrganizacional")
    ClassOrganizacaoReguladora = obter_classe("OrganizacaoReguladora")

    ClassRestricaoDeontica = obter_classe("RestricaoDeontica")

    ClassObrigacao = obter_classe("Obrigacao")
    ClassPermissao = obter_classe("Permissao")
    ClassProibicao = obter_classe("Proibicao")

    ClassValor = obter_classe("Valor")

    ClassNorma = obter_classe("Norma")

    ClassAcao      = obter_classe("Acao")
    ClassAcaoMoral = obter_classe("AcaoMoral")
    ClassOmissao   = obter_classe("Omissao")

    ClassAplicacaoNormativa = obter_classe("AplicacaoNormativa")

    ClassEcossistemaDeIA = obter_classe("EcossistemaDeIA")

    ClassQuebraNormativa = obter_classe("QuebraNormativa")

    ClassResponsabilizacao = obter_classe("Responsabilizacao")

    ClassAplicacaoDeResponsabilidade = obter_classe("AplicacaoDeResponsabilidade")

    PropResponsabiliza = getattr(onto, "responsabiliza", None)


    # ================================================================
    # Populando a Ontologia
    #          e
    #  Definindo Relacoes
    # ================================================================

    decidir_candidato_mais_qualificado = ClassAcao("Decidir_Candidato_Mais_Qualificado")

    revelar_banco_de_dados_de_usuarios = ClassAcao("Revelar_Banco_De_Dados_De_Usuarios")

    negar_realizacao_de_acao = ClassOmissao("Negar_Realizacao_De_Acao")



    agente_artificial_1 = ClassAgenteArtificial("Artificial_1")
    hasattr(agente_artificial_1, "participatedIn")
    agente_artificial_1.participatedIn.append(decidir_candidato_mais_qualificado)

    agente_artificial_2 = ClassAgenteArtificial("Artificial_2")
    hasattr(agente_artificial_2, "participatedIn")
    agente_artificial_2.participatedIn.append(revelar_banco_de_dados_de_usuarios)



    usuario_1 = ClassUsuario("Usuario_1")
    hasattr(usuario_1, "participatedIn")
    usuario_1.participatedIn.append(decidir_candidato_mais_qualificado)
    hasattr(usuario_1, "interage_com")
    usuario_1.interage_com.append(agente_artificial_1)

    usuario_2 = ClassUsuario("Usuario_2")
    hasattr(usuario_2, "participatedIn")
    usuario_2.participatedIn.append(revelar_banco_de_dados_de_usuarios)
    hasattr(usuario_2, "interage_com")
    usuario_2.interage_com.append(agente_artificial_2)



    ecossistema_1 = ClassEcossistemaDeIA("Ecossistema_1")
    hasattr(ecossistema_1, "mediates")
    ecossistema_1.mediates.append(usuario_1)
    ecossistema_1.mediates.append(agente_artificial_1)
    hasattr(ecossistema_1, "manifestedIn")
    ecossistema_1.manifestedIn.append(decidir_candidato_mais_qualificado)

    ecossistema_2 = ClassEcossistemaDeIA("Ecossistema_2")
    hasattr(ecossistema_2, "mediates")
    ecossistema_2.mediates.append(usuario_2)
    ecossistema_2.mediates.append(agente_artificial_2)
    hasattr(ecossistema_2, "manifestedIn")
    ecossistema_2.manifestedIn.append(revelar_banco_de_dados_de_usuarios)



    especialista_filosofo = ClassEspecialista("Especialista_Filosofo")



    valor_nao_maleficencia = ClassValor("Nao_Maleficencia1")
    valor_justica = ClassValor("Justica1")
    valor_beneficencia = ClassValor("Beneficencia1")

    hasattr(valor_nao_maleficencia, "historicallyDependsOn")
    valor_nao_maleficencia.historicallyDependsOn.append(especialista_filosofo)

    hasattr(valor_justica, "historicallyDependsOn")
    valor_justica.historicallyDependsOn.append(especialista_filosofo)

    hasattr(valor_beneficencia, "historicallyDependsOn")
    valor_beneficencia.historicallyDependsOn.append(especialista_filosofo)


    restricao_deontica = ClassRestricaoDeontica("Restricao_Deontica")
    hasattr(restricao_deontica, "historicallyDependsOn")
    restricao_deontica.historicallyDependsOn.append(especialista_filosofo)



    permissao = ClassPermissao("Deontica_Permissao")

    obrigacao = ClassObrigacao("Deontica_Obrigacao")

    proibicao = ClassProibicao("Deontica_Proibicao")
    hasattr(proibicao, "manifestedIn")
    proibicao.manifestedIn.append(negar_realizacao_de_acao)



    aplicacao_normativa_1 = ClassAplicacaoNormativa("Aplicacao_Normativa_1")

    aplicacao_normativa_2 = ClassAplicacaoNormativa("Aplicacao_Normativa_2")



    norma_imparcialidade = ClassNorma("Seja_Imparcial_Em_Suas_Decisoes")
    hasattr(norma_imparcialidade, "mediates")
    norma_imparcialidade.mediates.append(usuario_1)
    norma_imparcialidade.mediates.append(agente_artificial_1)
    hasattr(norma_imparcialidade, "historicallyDependsOn")
    norma_imparcialidade.historicallyDependsOn.append(especialista_filosofo)
    hasattr(norma_imparcialidade, "manifestedIn")
    norma_imparcialidade.manifestedIn.append(ClassAcaoMoral("Decidir_Imparcialmente"))



    norma_privacidade = ClassNorma("Nao_Revelar_Dados_Pessoais_De_Usuarios")
    hasattr(norma_privacidade, "mediates")
    norma_privacidade.mediates.append(usuario_2)
    norma_privacidade.mediates.append(agente_artificial_2)

    hasattr(norma_privacidade, "historicallyDependsOn")
    norma_privacidade.historicallyDependsOn.append(especialista_filosofo)

    hasattr(norma_privacidade, "manifestedIn")
    norma_privacidade.manifestedIn.append(ClassAcaoMoral("Proibir_Acesso_A_Dados_Pessoais"))

    hasattr(norma_privacidade, "wasCreatedIn")



    hasattr(obrigacao, "inheresIn")
    obrigacao.inheresIn = norma_imparcialidade

    hasattr(proibicao, "inheresIn")
    proibicao.inheresIn = norma_privacidade



    hasattr(valor_justica, "inheresIn")
    valor_justica.inheresIn = norma_imparcialidade

    hasattr(valor_nao_maleficencia, "inheresIn")
    valor_nao_maleficencia.inheresIn = norma_privacidade



    #
    # agente_artificial = None
    # agente_humano = None
    # agente_organizacional = None
    #
    # if ClassAgenteArtificial:
    #     agente_artificial = ClassAgenteArtificial("SRI_Robo_Medico")
    #     agente_artificial = ClassAgenteArtificial("ChatBot")
    #
    #
    #
    # if ClassAgenteHumano:
    #     agente_humano = ClassAgenteHumano("Dr_Ana_Silva_Auditora")
    #
    # if ClassEcossistemaDeIA:
    #     ClassEcossistemaDeIA("Ambiente_Algoritmico_Financeiro")
    #
    # if ClassNorma:
    #     ClassNorma("Diretriz_de_Transparencia_Algoritmica")
    #
    # if ClassValor:
    #     ClassValor("Principio_da_Equidade_Social")
    #
    # if ClassRestricaoDeontica:
    #     ClassRestricaoDeontica("Proibicao_de_Decisao_Autonoma_Letal")
    #
    # if ClassAcao:
    #     ClassAcao("Decisao_de_Aprovacao_de_Credito")
    #
    # if ClassResponsabilizacao:
    #     ClassResponsabilizacao("Processo_Auditoria_Algoritmica_001")
    #
    # if ClassObrigacao:
    #     ClassObrigacao("Obrigacao_de_Explicabilidade")
    #
    # if ClassAplicacaoNormativa:
    #     ClassAplicacaoNormativa("Validacao_de_Vies_Positiva")
    #
    # if ClassQuebraNormativa:
    #     ClassQuebraNormativa("Vazamento_de_Dados_Nao_Autorizado")
    #
    # organizacao_reguladora = None
    #
    # if ClassOrganizacaoReguladora:
    #     organizacao_reguladora = ClassOrganizacaoReguladora("Comite_Europeu_de_Etica")
    #
    # if (
    #         organizacao_reguladora
    #         and agente_artificial
    #         and hasattr(organizacao_reguladora, "responsabiliza")
    # ):
    #     organizacao_reguladora.responsabiliza.append(agente_artificial)


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
        "Acoes",
        ClassAcao
    )

    imprimir_resultados_api(
        "Acoes Morais",
        ClassAcaoMoral
    )

    imprimir_resultados_api(
        "Omissoes",
        ClassOmissao
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
executar_consultas_owlready()
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