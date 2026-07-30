# Laboratorio 2 - Deep Learning (Series de tiempo)

Base de migración de Guatemala (2009 - junio 2026). Avance: modelos LSTM con tuneo de
hiperparámetros para las dos series del laboratorio 1 (total de viajeros y vía aérea).

Se usa PyTorch porque TensorFlow no tiene build para Python 3.14.

## Correr

```bash
python -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/jupyter notebook notebooks/laboratorio2.ipynb
```

## Estructura

- `notebooks/laboratorio2.ipynb` - preprocesamiento, LSTM y tuneo
- `src/preparar_datos.py` - limpieza y armado de las series (genera lo de `data/processed/`)
- `data/raw/` - Excel original, no se modifica
- `data/processed/` - series y split train/test (no se versiona)
