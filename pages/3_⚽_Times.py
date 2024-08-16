import streamlit as st
from utils.translate import translate_column_name, translate_columns, translate_position, translate_preferred_foot

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

club = df_filtered.iloc[0]["Club"]
logo_url = df_filtered.iloc[0]["Club Logo"]

st.markdown(f"""
    <div style="display: flex; align-items: center;">
        <img src="{logo_url}" style="width: auto; height: auto; margin-right: 10px;" />
        <h2>{club}</h2>
    </div>
""", unsafe_allow_html=True)

original_columns = [
    'Age', 'Photo', 'Flag', 'Overall', 'Value(£)', 'Wage(£)', 
    'Preferred Foot', 'Position', 'Kit Number', 'Year_Joined', 
    'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)'
]

translation_dict = translate_columns(original_columns)

df_filtered['Preferred Foot'] = df_filtered['Preferred Foot'].apply(translate_preferred_foot)
df_filtered['Height(cm.)'] = df_filtered['Height(cm.)'].astype(float) / 100
df_filtered['Weight(lbs.)'] = (df_filtered['Weight(lbs.)'].astype(float) * 0.453592).round(2)
df_filtered['Position'] = df_filtered['Position'].apply(translate_position)

df_filtered = df_filtered.rename(columns=translation_dict)

columns = list(translation_dict.values())

st.dataframe(df_filtered[columns],
             column_config={
                 "Geral": st.column_config.ProgressColumn(
                     "Geral", format="%d", min_value=0, max_value=100
                 ),
                 "Salário Semanal (£)": st.column_config.ProgressColumn("Salário Semanal", format="£%f", min_value=0, max_value=df_filtered["Salário Semanal (£)"].max()),
                 "Foto": st.column_config.ImageColumn(),
                 "Bandeira": st.column_config.ImageColumn("País"),
             })