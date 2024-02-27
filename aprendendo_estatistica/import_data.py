import pandas as pd
from ucimlrepo import fetch_ucirepo

def load_data():
    """
    Load the student performance dataset from the UCI repository.
    Avaliable in: https://archive.ics.uci.edu/dataset/320/student+performance
    """

    # load dataset 
    student_performance = fetch_ucirepo(id=320) 
    
    # data (as pandas dataframes) 
    features = student_performance.data.features 
    target = student_performance.data.targets

    X = pd.DataFrame(features, columns=student_performance.feature_names)
    y = pd.DataFrame(target, columns=student_performance.target_names)

    data = pd.concat([X, y], axis=1).reset_index(drop=True)

    data.columns = ['escola', 'sexo', 'idade', 'tipo_de_endereço', 'tamanho_da_familia',
                    'convivência_com_os_pais', 'grau_de_formação_da_mãe',
                    'grau_de_formação_do_pai', 'trabalho_da_mãe', 'trabalho_do_pai',
                    'motivo_pra_escolher_escola', 'guardião_do_aluno', 'tempo_para_ir_à_escola',
                    'tempo_de_estudo_semanal', 'número_de_reprovações', 'suporte_educacional',
                    'suporte_familiar_educacional', 'matérias_extras_pagas', 'atividades_extracurriculares',
                    'frequentou_creche', 'quer_cursar_ensino_superior', 'internet_em_casa',
                    'possui_relacionamento_romântico', 'qualidade_das_relações familiares',
                    'tempo_livre_depois_da_escola', 'saídas_com_amigos', 'consumo_de_álcool_durante_semana',
                    'consumo_de_álcool_final_de_semana', 'saúde_física', 'faltas_na_escola', 'notas_do_primeiro_período',
                    'notas_do_segundo_período', 'notas_finais']
    
    # transformations
    data['escola'] = data['escola'].replace('GP', 'Gabriel Pereira')
    data['escola'] = data['escola'].replace('MS', 'Mousinho da Silveira')
    data['tipo_de_endereço'] = data['tipo_de_endereço'].replace('U', 'Urbano')
    data['tipo_de_endereço'] = data['tipo_de_endereço'].replace('R', 'Rural')
    data['tamanho_da_familia'] = data['tamanho_da_familia'].replace('LE3', 'Menor ou igual a 3')
    data['tamanho_da_familia'] = data['tamanho_da_familia'].replace('GT3', 'Maior que 3')
    data['convivência_com_os_pais'] = data['convivência_com_os_pais'].replace('T', 'Juntos')
    data['convivência_com_os_pais'] = data['convivência_com_os_pais'].replace('A', 'Separados')
    data['trabalho_da_mãe'] = data['trabalho_da_mãe'].replace('teacher', 'professora')
    data['trabalho_da_mãe'] = data['trabalho_da_mãe'].replace('health', 'saúde')
    data['trabalho_da_mãe'] = data['trabalho_da_mãe'].replace('services', 'serviços')
    data['trabalho_da_mãe'] = data['trabalho_da_mãe'].replace('at_home', 'em casa')
    data['trabalho_da_mãe'] = data['trabalho_da_mãe'].replace('other', 'outro')
    data['trabalho_do_pai'] = data['trabalho_do_pai'].replace('teacher', 'professor')
    data['trabalho_do_pai'] = data['trabalho_do_pai'].replace('health', 'saúde')
    data['trabalho_do_pai'] = data['trabalho_do_pai'].replace('services', 'serviços')
    data['trabalho_do_pai'] = data['trabalho_do_pai'].replace('at_home', 'em casa')
    data['trabalho_do_pai'] = data['trabalho_do_pai'].replace('other', 'outro')
    data['motivo_pra_escolher_escola'] = data['motivo_pra_escolher_escola'].replace('home', 'proximidade da casa')
    data['motivo_pra_escolher_escola'] = data['motivo_pra_escolher_escola'].replace('reputation', 'reputação')
    data['motivo_pra_escolher_escola'] = data['motivo_pra_escolher_escola'].replace('course', 'curso')
    data['motivo_pra_escolher_escola'] = data['motivo_pra_escolher_escola'].replace('other', 'outro')
    data['guardião_do_aluno'] = data['guardião_do_aluno'].replace('mother', 'mãe')
    data['guardião_do_aluno'] = data['guardião_do_aluno'].replace('father', 'pai')
    data['guardião_do_aluno'] = data['guardião_do_aluno'].replace('other', 'outro')
    data = data.replace('yes', 'sim')
    data = data.replace('no', 'não')

    return data
