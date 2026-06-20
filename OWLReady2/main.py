from owlready2 import *

# MAPEAMENTO DA gUFO
owlready2.PREDEFINED_ONTOLOGIES["http://purl.org/nemo/gufo#"] = "gufo.owl"
owlready2.PREDEFINED_ONTOLOGIES["http://purl.org/nemo/gufo"] = "gufo.owl"

# CARREGAMENTO DA ONTOLOGIA
nome_arquivo = "meta-ontologia-etica-ia.rdf"
onto = get_ontology(nome_arquivo).load()

print("="*60)
print(f" Ontologia carregada com sucesso!")
print(f" IRI Base Ativa: {onto.base_iri}")
print("="*60)

# POVOAMENTO DA ONTOLOGIA
print("\n" + "="*60)
print(" Povoando a Ontologia com Instâncias de Teste...")
print("="*60)

with onto:
    def obter_classe(nome):
        return getattr(onto, nome, None)

    ClassAcao = obter_classe("Acao")
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
    ClassEcossistema = obter_classe("EcossistemaDeIA")
    ClassNorma = obter_classe("Norma")
    ClassValor = obter_classe("Valor")
    ClassJustica = obter_classe("Justica")
    ClassRestricao = obter_classe("RestricaoDeontica")
    PropResponsabiliza = getattr(onto, "responsabiliza")


    if ClassAgenteArtificial:
        ClassAgenteArtificial("SRI_Robo_Medico")

    if ClassAgenteHumano:
        ClassAgenteHumano("Dr_Ana_Silva_Auditora")

    if ClassAgenteOrganizacional:
        ClassAgenteOrganizacional("Comite_Europeu_de_Etica")

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

    if ClassOrganizacaoReguladora and ClassAgenteArtificial and PropResponsabiliza:
        agente_reg = ClassOrganizacaoReguladora("Comite_Europeu_de_Etica")
        agente_art = ClassAgenteArtificial("SRI_Robo_Medico")
        agente_reg.responsabiliza.append(agente_art)

print(" Povoamento concluído com sucesso!")


# TRADUÇÃO DAS QUESTÕES DE COMPETÊNCIA
consultas_sparql = {
    # --- GRUPO 1: Fundamentos da Agência Moral ---
    "QC1 (Agentes Morais)": f"""
        SELECT ?agente ?tipo WHERE {{
            ?agente <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?tipo .
            FILTER (?tipo IN (<{ClassAgenteArtificial.iri}>, <{ClassAgenteHumano.iri}>, <{ClassAgenteOrganizacional.iri}>))
        }}
    """,
    "QC2 e QC3 (Ações Morais e Omissões)": f"""
        SELECT ?acao_ou_omissao ?tipo WHERE {{
            ?acao_ou_omissao <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?tipo .
            FILTER (?tipo IN (<{ClassAcao.iri}>, <{ClassOmissao.iri}>))
        }}
    """,

    # --- GRUPO 2: Ecossistema de IA e Responsabilidade ---
    "QC4 (Ecossistema de IA)": f"""
        SELECT ?ecossistema WHERE {{
            ?ecossistema <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <{ClassEcossistema.iri}> .
        }}
    """,
    "QC5 (Responsabilidade no Ecossistema)": f"""
        SELECT ?responsabilidade WHERE {{
            ?responsabilidade <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <{ClassResponsabilizacao.iri}> .
        }}
    """,
    "QC6 e QC7 (Atribuição de Responsabilidade)": f"""
        SELECT ?quem_atribui ?agente_responsabilizado WHERE {{
            # Busca especificamente quem aplica a propriedade 'responsabiliza'
            ?quem_atribui <{PropResponsabiliza.iri}> ?agente_responsabilizado .
        }}
    """,

    # --- GRUPO 3: Normas, Valores e Deôntica ---
    "QC8 (Normas Éticas Gerais)": f"""
        SELECT ?norma WHERE {{
            ?norma <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <{ClassNorma.iri}> .
        }}
    """,
    "QC9 (Componentes Lógicos de Normas)": f"""
        SELECT ?componente ?tipo WHERE {{
            ?componente <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?tipo .
            FILTER (?tipo IN (<{ClassObrigacao.iri}>, <{ClassPermissao.iri}>, <{ClassProibicao.iri}>))
        }}
    """,
    "QC10 e QC13 (Aplicação e Quebra de Normas aplicadas à Ações)": f"""
        SELECT ?evento_normativo ?tipo WHERE {{
            ?evento_normativo <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?tipo .
            FILTER (?tipo IN (<{ClassAplicacaoNormativa.iri}>, <{ClassQuebraNormativa.iri}>))
        }}
    """,
    "QC11 (Valores Éticos e Subclasses)": f"""
        SELECT ?valor ?tipo_valor WHERE {{
            ?valor <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?tipo_valor .
            ?tipo_valor <http://www.w3.org/2000/01/rdf-schema#subClassOf>* <{ClassValor.iri}> .
        }}
    """,
    "QC12 (Quem define valores - Especialistas e Órgãos Reguladores)": f"""
        SELECT ?definidor ?tipo WHERE {{
            ?definidor <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?tipo .
            FILTER (?tipo IN (<{ClassOrganizacaoReguladora.iri}>, <{ClassEspecialista.iri}>))
        }}
    """,
    "QC14 (Restrições Deônticas Genéricas)": f"""
        SELECT ?restricao WHERE {{
            ?restricao <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <{ClassRestricao.iri}> .
        }}
    """
}

def executar_bloco_testes(titulo_modelo):
    print(f"\n" + "-"*45)
    print(f" EXECUTANDO CONSULTAS: {titulo_modelo}")
    print("-"*45)

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

executar_bloco_testes("ASSERTED MODEL")

print("\n" + "\\"*45)
print(" Ativando o Raciocinador Lógico (HermiT)...")
print("\\"*45)

sync_reasoner_hermit()

executar_bloco_testes("INFERRED MODEL")