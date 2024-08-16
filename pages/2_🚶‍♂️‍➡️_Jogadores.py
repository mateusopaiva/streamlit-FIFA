import streamlit as st
from utils.translate import translate_position, translate_preferred_foot

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.markdown(f"""
    <div style="display: flex; align-items: center;">
        <img src="{player_stats['Photo']}" style="margin-right: 15px;" />
        <h2>{player_stats['Name']}</h2>
        <img src="{player_stats['Flag']}" style="margin-left: 5px;" />
    </div><br>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown(f"**Clube:** {player_stats['Club']}")
with col2:
    position = player_stats['Position']
    translated_position = translate_position(position)
    st.markdown(f"**Posição:** {translated_position}")
with col3:
    preferred_foot = player_stats['Preferred Foot']
    translated_foot = translate_preferred_foot(preferred_foot)
    st.markdown(f"**Pé preferido:** {translated_foot}")

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    col1.markdown(f"**Idade:** {player_stats['Age']} anos")
with col2:
    col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100} m")
with col3:
    col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f} kg")

st.divider()

st.subheader(f"Classificação Geral: *{player_stats['Overall']}*")
st.progress(int(player_stats["Overall"]))

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
with col2:
    col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
with col3:
    col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")
