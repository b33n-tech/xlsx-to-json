import streamlit as st
import pandas as pd
import json
from io import BytesIO

st.set_page_config(page_title="Convertisseur CSV/XLSX → JSON", page_icon="📄", layout="centered")

st.title("📄 Convertisseur CSV/XLSX → JSON")

uploaded_file = st.file_uploader("Téléverse ton fichier (.csv ou .xlsx)", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # Lecture selon le type de fichier
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("✅ Fichier chargé avec succès !")
        st.dataframe(df.head())

        # Conversion en JSON
        json_str = df.to_json(orient="records", force_ascii=False, indent=2)

        # Affichage du JSON brut
        st.subheader("Aperçu du JSON :")
        st.code(json_str[:1000] + "..." if len(json_str) > 1000 else json_str, language="json")

        # Bouton de téléchargement
        st.download_button(
            label="⬇️ Télécharger en JSON",
            data=json_str.encode('utf-8'),
            file_name=uploaded_file.name.rsplit('.', 1)[0] + ".json",
            mime="application/json"
        )

    except Exception as e:
        st.error(f"Erreur lors du traitement du fichier : {e}")

else:
    st.info("💡 Uploade un fichier CSV ou Excel pour commencer.")
