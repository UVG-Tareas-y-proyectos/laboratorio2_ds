"""Limpieza y armado de las series. Genera los csv de data/processed/"""
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

df = pd.read_excel(BASE / "data/raw/Base_Migracion_2009-2026jun.xlsx", sheet_name="Datos")
df.columns = df.columns.str.strip()

df["Año"] = pd.to_numeric(df["Año"], errors="coerce")
df["Mes cod"] = pd.to_numeric(df["Mes cod"], errors="coerce")
df["Viajero"] = pd.to_numeric(df["Viajero"], errors="coerce")
df["Fecha"] = pd.to_datetime(dict(year=df["Año"], month=df["Mes cod"], day=1), errors="coerce")
df = df.dropna(subset=["Fecha", "Viajero"])

# solo turistas y excursionistas, que son las categorias con datos en todo el periodo
base = df[df["Tipo de Viajero"].isin(["Turista", "Excursionista"])].copy()

# serie 1: total mensual de viajeros
serie_total = base.groupby("Fecha")["Viajero"].sum().asfreq("MS", fill_value=0)

# serie 2: solo los que entran por via aerea
serie_aerea = (base[base["Vía"] == "Aérea"].groupby("Fecha")["Viajero"].sum()
               .reindex(serie_total.index, fill_value=0))

# split cronologico 70/30
corte = round(len(serie_total) * 0.70)

(BASE / "data/processed").mkdir(parents=True, exist_ok=True)
base.to_csv(BASE / "data/processed/migracion_limpia.csv", index=False)
serie_total.to_csv(BASE / "data/processed/serie_total.csv")
serie_aerea.to_csv(BASE / "data/processed/serie_aerea.csv")
serie_total.iloc[:corte].to_csv(BASE / "data/processed/train_total.csv")
serie_total.iloc[corte:].to_csv(BASE / "data/processed/test_total.csv")
serie_aerea.iloc[:corte].to_csv(BASE / "data/processed/train_aerea.csv")
serie_aerea.iloc[corte:].to_csv(BASE / "data/processed/test_aerea.csv")

print("filas limpias:", base.shape)
print("serie:", serie_total.index.min().date(), "-", serie_total.index.max().date())
print("corte train/test en:", serie_total.index[corte].date())
