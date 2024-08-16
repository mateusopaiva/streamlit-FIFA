def translate_preferred_foot(foot):
    translation = {
        'Right': 'Direito',
        'Left': 'Esquerdo'
    }
    return translation.get(foot, foot)

def translate_position(position):
    position_translation = {
        'SUB': 'Substituto',
        'RES': 'Reserva',
        'LCM': 'Meio-Campista Central Esquerdo',
        'RCM': 'Meio-Campista Central Direito',
        'CM': 'Meio-Campista Central',
        'CDM': 'Volante (Meio-Campista Defensivo)',
        'LDM': 'Volante Esquerdo (Meio-Campista Defensivo Esquerdo)',
        'RDM': 'Volante Direito (Meio-Campista Defensivo Direito)',
        'CAM': 'Meia Ofensivo (Meio-Campista Ofensivo)',
        'LAM': 'Meia Ofensivo Esquerdo',
        'RAM': 'Meia Ofensivo Direito',
        'LB': 'Lateral Esquerdo',
        'RB': 'Lateral Direito',
        'LWB': 'Ala Esquerdo',
        'RWB': 'Ala Direito',
        'LCB': 'Zagueiro Central Esquerdo',
        'RCB': 'Zagueiro Central Direito',
        'CB': 'Zagueiro Central',
        'LW': 'Ponta Esquerda',
        'RW': 'Ponta Direita',
        'LM': 'Meia Esquerda',
        'RM': 'Meia Direita',
        'LS': 'Atacante Esquerdo',
        'RS': 'Atacante Direito',
        'ST': 'Atacante',
        'CF': 'Centroavante',
        'LF': 'Atacante Esquerdo',
        'RF': 'Atacante Direito',
        'GK': 'Goleiro'
    }

    return position_translation.get(position, position)

def translate_column_name(position):
    translation_dict = {
        'Age': 'Idade',
        'Photo': 'Foto',
        'Flag': 'Bandeira',
        'Overall': 'Classificação Geral',
        'Value(£)': 'Valor(£)',
        'Wage(£)': 'Salário Semanal (£)',
        'Preferred Foot': 'Pé Preferido',
        'Position': 'Posição',
        'Kit Number': 'Número da camisa',
        'Year_Joined': 'Ano de Entrada',
        'Height(cm.)': 'Altura (m)',
        'Weight(lbs.)': 'Peso (kg)',
        'Contract Valid Until': 'Contrato Válido Até',
        'Release Clause(£)': 'Cláusula de Liberação (£)'
    }
    return translation_dict.get(position, position)

def translate_columns(columns):
    return {col: translate_column_name(col) for col in columns}